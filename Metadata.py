import streamlit as st
import tableauserverclient as TSC
import pandas as pd
import io
from datetime import datetime
import smtplib
from email.message import EmailMessage
import requests
import io
from datetime import datetime
from tableauserverclient.server.endpoint.exceptions import ServerResponseError
import ast



# ==================================================
# BASIC HELPERS
# ==================================================
def safe_datetime(v):
    return v.isoformat() if hasattr(v, "isoformat") else None


def get_connection_mode(conn):
    return "Extract" if conn.connection_type.lower() == "hyper" else "Live"


def get_view_hits(view):
    return view.usage.total_view_count if hasattr(view, "usage") and view.usage else 0


def sum_workbook_hits(views):
    return sum(get_view_hits(v) for v in views)


# ==================================================
# METADATA API
# ==================================================
def get_metadata_token(server_url, site, pat_name, pat_secret):
    auth = TSC.PersonalAccessTokenAuth(pat_name, pat_secret, site)
    server = TSC.Server(server_url, use_server_version=True)
    with server.auth.sign_in(auth):
        return server.auth_token







# ==================================================
# LINEAGE WITH FALLBACK (CRITICAL FIX)
# ==================================================



# ==================================================
# CORE EXTRACTION
# ==================================================
def extract_tableau_metadata(server_url, site, pat_name, pat_secret):

    auth = TSC.PersonalAccessTokenAuth(pat_name, pat_secret, site)
    server = TSC.Server(server_url, use_server_version=True)

    projects = []
    workbooks_w = []
    views_v = []
    dashboards = []
    wb_conns = []
    ds_conns = []
    datasources = []
    lineage = []
    user_level_permissions = []
    output = []
    subscriptions_output = []
    all_users = []
    

    metadata_token = get_metadata_token(server_url, site, pat_name, pat_secret)

    with server.auth.sign_in(auth):

        # PROJECTS
        prjs, _ = server.projects.get()
        pmap = {p.id: p.name for p in prjs}

        for p in prjs:
            projects.append({
                "Project ID": p.id,
                "Project Name": p.name,
                "Parent Project ID": p.parent_id
            })

        # ALL WORKBOOKS (pagination)
        req = TSC.RequestOptions(pagesize=1000)
        all_wbs = []

        while True:
            page, pg = server.workbooks.get(req)
            all_wbs.extend(page)
            if pg.page_number * pg.page_size >= pg.total_available:
                break
            req.page_number += 1

        for wb in all_wbs:
            server.workbooks.populate_views(wb)
            server.workbooks.populate_connections(wb)

            workbooks_w.append({
                "Workbook ID": wb.id,
                "Workbook Name": wb.name,
                "Project Name": pmap.get(wb.project_id),
                "Owner ID": wb.owner_id,
                "Created At": safe_datetime(wb.created_at),
                "Updated At": safe_datetime(wb.updated_at),
                "Total Hits": sum_workbook_hits(wb.views)
            })

            for v in wb.views:
                vtype = "Dashboard" if v.sheet_type == "dashboard" else "Worksheet"
                views_v.append({
                    "View ID": v.id,
                    "View Name": v.name,
                    "View Type": vtype,
                    "Workbook Name": wb.name,
                    "Project Name": pmap.get(wb.project_id),
                    "Number of Hits": get_view_hits(v)
                })

            for conn in wb.connections:
                wb_conns.append({
                    "Workbook Name": wb.name,
                    "Connection Mode": get_connection_mode(conn),
                    "Connection Type": conn.connection_type,
                    "Server Address": getattr(conn, "server_address", None),
                    "Database Name": getattr(conn, "database_name", None),
                    "Schema": getattr(conn, "schema", None),
                    "Username": getattr(conn, "username", None)
                })

        # DATASOURCES
        dss, _ = server.datasources.get()
        for ds in dss:
            datasources.append({
                "Datasource ID": ds.id,
                "Datasource Name": ds.name,
                "Project Name": pmap.get(ds.project_id),
                "Owner ID": ds.owner_id
            })

            server.datasources.populate_connections(ds)
            for conn in ds.connections:
                ds_conns.append({
                    "Datasource Name": ds.name,
                    "Connection Mode": get_connection_mode(conn),
                    "Connection Type": conn.connection_type,
                    "Server Address": getattr(conn, "server_address", None),
                    "Database Name": getattr(conn, "database_name", None),
                    "Schema": getattr(conn, "schema", None)
                })

        

        print("🔄 Fetching new code...")
        req = TSC.RequestOptions(pagesize=1000)
        while True:
            users, p = server.users.get(req)
            all_users.extend(users)
            if p.page_number * p.page_size >= p.total_available:
                break
            req.page_number += 1
        user_map = {u.id: u.name for u in all_users}

        # ---- GROUPS (ALL) ----
        all_groups = []
        req = TSC.RequestOptions(pagesize=1000)
        while True:
            groups, p = server.groups.get(req)
            all_groups.extend(groups)
            if p.page_number * p.page_size >= p.total_available:
                break
            req.page_number += 1
        group_map = {g.id: g.name for g in all_groups}

        # Group → users
        group_users_map = {}
        for g in all_groups:
            server.groups.populate_users(g)
            group_users_map[g.id] = [u.id for u in g.users]

        # ---- WORKBOOKS (ALL) ----
        all_workbooks = []
        req = TSC.RequestOptions(pagesize=1000)
        while True:
            workbooks, p = server.workbooks.get(req)
            all_workbooks.extend(workbooks)
            if p.page_number * p.page_size >= p.total_available:
                break
            req.page_number += 1

        # ---- PROCESS EACH WORKBOOK (NO SKIPS) ----
        for wb in all_workbooks:

            base_row = {
                "workbook_name": wb.name,
                "project": wb.project_name,
                "user_id": None,
                "user_name": None,
                "group_id": None,
                "group_name": None,
                "access_via": None,
                "capabilities": None,
                "permission_flag": None
            }

            try:
                server.workbooks.populate_permissions(wb)

                # CASE 1: No explicit permissions
                if not wb.permissions:
                    row = base_row.copy()
                    row["access_via"] = "Inherited"
                    row["permission_flag"] = "Inherited from Project"
                    user_level_permissions.append(row)
                    continue

                # CASE 2: Explicit permissions
                for perm in wb.permissions:
                    grantee_id = perm.grantee.id
                    grantee_type = perm.grantee.tag_name

                    if grantee_type == "user":
                        row = base_row.copy()
                        row.update({
                            "user_id": grantee_id,
                            "user_name": user_map.get(grantee_id, "Unknown User"),
                            "access_via": "Direct",
                            "capabilities": str(perm.capabilities),
                            "permission_flag": "Explicit Permission"
                        })
                        user_level_permissions.append(row)

                    elif grantee_type == "group":
                        group_name = group_map.get(grantee_id, "Unknown Group")
                        for uid in group_users_map.get(grantee_id, []):
                            row = base_row.copy()
                            row.update({
                                "user_id": uid,
                                "user_name": user_map.get(uid, "Unknown User"),
                                "group_id": grantee_id,
                                "group_name": group_name,
                                "access_via": "Group",
                                "capabilities": str(perm.capabilities),
                                "permission_flag": "Explicit Permission"
                            })
                            user_level_permissions.append(row)

            except ServerResponseError as e:
                # 🔴 CRITICAL FIX: DO NOT SKIP
                if e.code.startswith("403"):
                    row = base_row.copy()
                    row["access_via"] = "Restricted"
                    row["permission_flag"] = "Permission Metadata Not Accessible"
                    user_level_permissions.append(row)
                else:
                    raise

        df= pd.DataFrame(user_level_permissions)

        def safe_parse_capabilities(x):
            if pd.isna(x):
                return {}
            return ast.literal_eval(x)

        df["capabilities_dict"] = df["capabilities"].apply(safe_parse_capabilities)
        capabilities_df = pd.json_normalize(df["capabilities_dict"])
        capabilities_df.index = df.index   # 🔑 CRITICAL LINE
        final_df = pd.concat(
            [df.drop(columns=["capabilities", "capabilities_dict"]), capabilities_df],
            axis=1
        )
        final_df = final_df.fillna("Not Set")
        permission_data = final_df[final_df['user_name']!='Not Set']
        

        # ----------------------------
        # 1️⃣ Fetch ALL workbooks
        # ----------------------------
        print("🔄 Fetching all workbooks...")
        workbooks = list(TSC.Pager(server.workbooks))
        print(f"✅ Found {len(workbooks)} workbooks\n")

        workbook_map = {wb.id: wb for wb in workbooks}

        # ----------------------------
        # 2️⃣ Fetch ALL tasks
        # ----------------------------
        print("🔄 Fetching background tasks...")
        tasks = list(TSC.Pager(server.tasks))
        print(f"✅ Found {len(tasks)} tasks\n")

        # ----------------------------
        # 3️⃣ Identify refresh-scheduled workbooks
        # ----------------------------
        refresh_workbooks = set()

        for t in tasks:
            if t.task_type in ("extractRefresh", "RefreshExtractViaBridgeTask"):
                if t.target and t.target.type == "workbook":
                    refresh_workbooks.add(t.target.id)

        print(f"✅ Workbooks with refresh schedules: {len(refresh_workbooks)}\n")

        # ----------------------------
        # 4️⃣ Build final output
        # ----------------------------
        print("🔄 Building output...")
        for wb in workbooks:
            server.workbooks.populate_connections(wb)

            connection_types = {c.connection_type.lower() for c in wb.connections}
            a = connection_types

            connection_type = "Extract" if "hyper" in connection_types else "Live"

            output.append({
                "workbook_id": wb.id,
                "workbook_name": wb.name,
                "project": wb.project_name,
                "connection_type": connection_type,
                "Database" : a,
                "has_refresh_schedule": "Yes" if wb.id in refresh_workbooks else "No"
            })

        print("\n✅ Dashboard connection & refresh info extracted")

        extract  = pd.DataFrame(output)
        
        
        
        
        
                # ----------------------------
        # Lookups (PAGINATED)
        # ----------------------------
        views = list(TSC.Pager(server.views))
        view_name_map = {v.id: v.name for v in views}
        view_to_workbook = {v.id: v.workbook_id for v in views}

        workbooks = list(TSC.Pager(server.workbooks))
        workbook_map = {wb.id: wb.name for wb in workbooks}

        users = list(TSC.Pager(server.users))
        user_map = {u.id: u.name for u in users}

        # ----------------------------
        # Subscriptions (PAGINATED)
        # ----------------------------
        subscriptions = list(TSC.Pager(server.subscriptions))

        for sub in subscriptions:
            if not sub.target:
                continue  # safety check

            view_id = sub.target.id
            workbook_id = view_to_workbook.get(view_id)

            # Tableau Cloud–safe way
            user_id = getattr(sub, "_user_id", None)

            subscriptions_output.append({
                "workbook_id": workbook_id,
                "workbook_name": workbook_map.get(workbook_id, "Unknown Workbook"),
                "view_id": view_id,
                "subscriptions_view_name": view_name_map.get(view_id, "Unknown View"),
                "user_id": sub.user_id,
                "user_name": user_map.get(sub.user_id, "Unknown User"),
                "subscriptions_delivery_type": "PDF" if sub.attach_pdf else "Image"
            })

        


    return {
        "Projects": pd.DataFrame(projects),
        "Workbooks": pd.DataFrame(workbooks_w),
        "views": pd.DataFrame(views_v),
        #"Dashboards": pd.DataFrame(dashboards),
        "Workbook Connections": pd.DataFrame(wb_conns),
        "Published Data Sources": pd.DataFrame(datasources),
        "Datasource Connections": pd.DataFrame(ds_conns),
        #"Lineage (DB → Table → Column)": pd.DataFrame(lineage),
        "User level permissions":pd.DataFrame(permission_data),
        "Extract":pd.DataFrame(extract),
        "Subscription":pd.DataFrame(subscriptions_output)
    }









# ==================================================
# STREAMLIT UI
# ==================================================
st.set_page_config("Tableau Metadata", layout="centered")
st.title("📊 Tableau Metadata Extractor")

server_url = st.text_input("Tableau Server URL")
site = st.text_input("Site Content URL (blank = Default)")
pat_name = st.text_input("PAT Name")
pat_secret = st.text_input("PAT Secret", type="password")

# ---------------- RUN EXTRACTION ----------------
if st.button("Run Extraction"):
    if not all([server_url, pat_name, pat_secret]):
        st.warning("Please fill all required fields")
    else:
        with st.spinner("Extracting metadata..."):
            dfs = extract_tableau_metadata(
                server_url, site, pat_name, pat_secret
            )

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            for sheet, df in dfs.items():
                df.to_excel(writer, sheet_name=sheet[:31], index=False)

        output.seek(0)
        st.session_state["excel_file"] = output.getvalue()
        st.session_state["completed"] = True

        st.success("✅ Extraction completed")

# ==================================================
# POST-EXECUTION UI (ONLY AFTER COMPLETION)
# ==================================================
if st.session_state.get("completed"):

    st.divider()

    st.subheader("⬇ Download Report")
    st.download_button(
        "Download Excel",
        st.session_state["excel_file"],
        f"tableau_metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.divider()

    st.subheader("📧 Email Report")
    email = st.text_input("Recipient Email", key="email_input")

    if st.button("Send Email"):
        if not email:
            st.warning("Please enter recipient email")
        else:
            try:
                msg = EmailMessage()
                msg["Subject"] = "Tableau Server Metadata Inventory Report"
                msg["From"] = "svc_power_bi_poc@Blend360.com"
                msg["To"] = email
                msg.set_content("Please find the Excel report attached.")

                msg.add_attachment(
                    st.session_state["excel_file"],
                    maintype="application",
                    subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    filename="report.xlsx"
                )

                with smtplib.SMTP("smtp.office365.com", 587) as server:
                    server.starttls()
                    server.login("svc_power_bi_poc@Blend360.com", "Blend@360")
                    server.send_message(msg)

                st.success("✅ Email sent successfully!")

            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
               