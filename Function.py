import streamlit as st
import time
import pandas as pd
from datetime import datetime

# =========================================================
# DUMMY FUNCTIONS  — replace with real implementations
# =========================================================

def discovery_function(config_file, pbi_workspace):
    """Called automatically when user clicks Start Migration."""
    time.sleep(2)
    if not config_file or not pbi_workspace:
        return {"success": False, "reason": "Config file and Power BI workspace are required.", "data": {}}
    return {
        "success": True,
        "reason": "Connected to Tableau Server via config. Full inventory extracted successfully.",
        "data": {
            "workbooks": 42, "datasources": 18, "tables": 134, "columns": 2847, "users": 56,
            "tasks": [
                {"Task": "Connect to Tableau Server via REST API",  "Status": "Completed"},
                {"Task": "Extract workbook inventory",              "Status": "Completed"},
                {"Task": "Identify tables & columns used",          "Status": "Completed"},
                {"Task": "Generate Excel inventory file",           "Status": "Completed"},
                {"Task": "Build UI for server details",             "Status": "In Progress"},
            ]
        }
    }

def data_modelling_function(discovery_data, pbi_workspace):
    time.sleep(2)
    if not pbi_workspace:
        return {"success": False, "reason": "Power BI workspace not provided.", "data": {}}
    return {
        "success": True,
        "reason": "Semantic model created in Power BI Service. Joins and relationships mapped.",
        "data": {
            "tables_modelled": 134, "relationships": 47, "measures_created": 210, "model_size_mb": 84,
            "tasks": [
                {"Task": "Identify Tables & Columns from Tableau",     "Status": "Completed"},
                {"Task": "Create Semantic Model in PBI Service",       "Status": "Completed"},
                {"Task": "Map complex join types & relationships",     "Status": "In Progress (Automation Possible)"},
                {"Task": "Cross-filtering direction configuration",    "Status": "In Progress (Automation Possible)"},
                {"Task": "UI for Tableau dashboard detail input",      "Status": "In Progress"},
            ]
        }
    }

def dashboard_rebuild_function(modelling_data, pbi_workspace):
    time.sleep(2)
    return {
        "success": True,
        "reason": "Tableau metadata extracted. PBI dashboards provisioned from specifications.",
        "data": {
            "dashboards_extracted": 42, "dashboards_built": 38, "dashboards_manual": 4, "visuals_created": 312,
            "tasks": [
                {"Task": "Extract Tableau dashboard metadata to file",  "Status": "Completed"},
                {"Task": "Leverage metadata to build PBI dashboards",   "Status": "Completed"},
                {"Task": "Programmatic PBI dashboard creation",         "Status": "Not Possible (Team exploring)"},
                {"Task": "Format & style PBI dashboards",               "Status": "Not Possible (Team exploring)"},
            ]
        }
    }

def unit_testing_function(rebuild_data, pbi_workspace):
    time.sleep(2)
    if not rebuild_data:
        return {"success": False, "reason": "No rebuild data available for testing.", "data": {}}
    return {
        "success": True,
        "reason": "Data validation passed. Sheet comparison done. Image analysis in progress.",
        "data": {
            "data_passed": 134, "data_failed": 0,
            "sheet_matches": 38, "sheet_mismatches": 4, "images_analysed": 42,
            "tasks": [
                {"Task": "Compare Data: Tableau vs Semantic Model",    "Status": "Completed"},
                {"Task": "Sheet comparison: Tableau vs PBI",           "Status": "In Progress (Automation Possible)"},
                {"Task": "Image comparison: chart types & formatting", "Status": "In Progress (Automation Possible)"},
            ]
        }
    }

def deployment_function(testing_data, pbi_workspace):
    time.sleep(2)
    if not pbi_workspace:
        return {"success": False, "reason": "Power BI workspace not specified.", "data": {}}
    return {
        "success": True,
        "reason": "All PBI files published to respective workspace locations successfully.",
        "data": {
            "files_deployed": 42, "workspace": pbi_workspace,
            "deployment_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tasks": [
                {"Task": "Publish Multiple PBI Files to PBI Service",  "Status": "Completed"},
                {"Task": "Assign to correct workspace locations",       "Status": "Completed"},
                {"Task": "Validate CSV source & destination mapping",   "Status": "Completed"},
            ]
        }
    }


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="BI Migration",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="💳"
)

# =========================================================
# CSS — 100% static, no Python variables inside
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header   { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem !important; max-width: 1400px !important; }

/* HEADER */
.vis-header {
    background: linear-gradient(135deg, #1A1F71 0%, #0D47A1 60%, #006E82 100%);
    border-radius: 18px; padding: 2.5rem 3rem; margin-bottom: 2rem;
}
.vis-header h1 {
    font-size: 36px; font-weight: 800; color: #fff;
    margin: 0 0 6px; letter-spacing: -0.02em;
}
.vis-header p  { color: rgba(255,255,255,0.8); font-size: 18px; margin: 0 0 18px; }
.badge-row     { display: flex; gap: 10px; flex-wrap: wrap; }
.badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.22);
    border-radius: 100px; padding: 5px 14px; font-size: 12px; font-weight: 600; color: #fff;
}
.badge-dot { width: 7px; height: 7px; border-radius: 50%; background: #F7B600; }

/* CONFIG LANDING CARD */
.config-card {
    background: #fff; border: 1px solid #E4E7EB; border-radius: 20px;
    padding: 3rem; box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    border-top: 5px solid #1A1F71; max-width: 1400px; margin: 0 auto;
}
.config-title {
    font-size: 22px; font-weight: 800; color: #1A1F36;
    margin-bottom: 6px; letter-spacing: -0.02em;
}
.config-sub {
    font-size: 16px; color: #6B7280; margin-bottom: 2rem; line-height: 1.6;
}
.config-steps {
    display: flex; gap: 0; margin-bottom: 2rem;
    border: 1px solid #E4E7EB; border-radius: 12px; overflow: hidden;
}
.config-step {
    flex: 1; padding: 18px 16px; background: #F7F9FC;
    border-right: 1px solid #E4E7EB; text-align: center;
}
.config-step:last-child { border-right: none; }
.cs-num {
    width: 28px; height: 28px; border-radius: 50%;
    background: #1A1F71; color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700; margin: 0 auto 6px;
}
.cs-lbl { font-size: 16px; font-weight: 600; color: #374151; }
.cs-sub { font-size: 12px; color: #9CA3AF; margin-top: 2px; }

/* STEPPER */
.stepper-wrap {
    background: #fff; border: 1px solid #E4E7EB; border-radius: 14px;
    padding: 1.6rem 2rem; margin-bottom: 1.5rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
}
.stepper { display: flex; align-items: flex-start; position: relative; }
.stepper-track {
    position: absolute; top: 22px; left: 6%; right: 6%;
    height: 3px; background: #E4E7EB; border-radius: 6px; z-index: 0;
}
.step-col {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; position: relative; z-index: 1;
}
.step-circle {
    width: 46px; height: 46px; border-radius: 50%;
    background: #fff; border: 3px solid #E4E7EB;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700; color: #9CA3AF;
    margin-bottom: 9px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: all .25s ease;
}
.step-col.s-active .step-circle {
    background: #1A1F71; border-color: #1A1F71; color: #fff;
    transform: scale(1.1); box-shadow: 0 4px 16px rgba(26,31,113,0.35);
}
.step-col.s-done   .step-circle { background: #059669; border-color: #059669; color: #fff; }
.step-col.s-failed .step-circle { background: #DC2626; border-color: #DC2626; color: #fff; }
.step-name { font-size: 16px; font-weight: 600; color: #9CA3AF; text-align: center; }
.step-col.s-active .step-name  { color: #1A1F71; font-weight: 700; }
.step-col.s-done   .step-name  { color: #059669; }
.step-col.s-failed .step-name  { color: #DC2626; }
.step-sub { font-size: 13px; color: #C4C9D4; text-align: center; margin-top: 2px; }

/* CONTENT CARD */
.scard {
    background: #fff; border: 1px solid #E4E7EB; border-radius: 16px;
    padding: 2.5rem; box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    border-top: 4px solid #1A1F71; margin-bottom: 1rem;
}
.scard-head { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
.scard-icon {
    width: 38px; height: 38px;
    background: linear-gradient(135deg, #1A1F71, #0D47A1);
    border-radius: 10px; display: flex; align-items: center;
    justify-content: center; font-size: 18px; color: #fff; flex-shrink: 0;
}
.scard-title { font-size: 24px; font-weight: 800; color: #1A1F36; letter-spacing: -0.02em; }
.scard-desc  { font-size: 14px; color: #6B7280; line-height: 1.7; margin-bottom: 1.5rem; }

/* CONTEXT BAR — shows config inputs at top of each step */
.ctx-bar {
    display: flex; gap: 24px; align-items: center;
    background: #F7F9FC; border: 1px solid #E4E7EB;
    border-radius: 10px; padding: 12px 18px; margin-bottom: 1.5rem;
}
.ctx-item { display: flex; flex-direction: column; }
.ctx-lbl  { font-size: 11px; font-weight: 600; color: #9CA3AF; text-transform: uppercase; letter-spacing: .06em; }
.ctx-val  { font-size: 14px; font-weight: 600; color: #1A1F36; }

/* METRICS */
.metric-row  { display: flex; gap: 12px; flex-wrap: wrap; margin: 1.2rem 0; }
.metric-tile {
    flex: 1 1 140px; min-width: 140px; background: #F7F9FC;
    border: 1px solid #E4E7EB; border-radius: 12px; padding: 1.1rem 1.3rem;
    transition: all .2s ease;
}
.metric-tile:hover { border-color: #1A1F71; box-shadow: 0 4px 14px rgba(0,0,0,0.08); transform: translateY(-2px); }
.m-icon  { font-size: 22px; margin-bottom: 6px; display: block; }
.m-val   { font-size: 28px; font-weight: 800; color: #1A1F71; line-height: 1; margin-bottom: 3px; }
.m-label { font-size: 11px; font-weight: 600; color: #6B7280; text-transform: uppercase; letter-spacing: .06em; }

/* STATUS BANNERS */
.s-success {
    background: #ECFDF5; border: 1.5px solid #059669; border-radius: 12px;
    padding: 15px 20px; color: #065F46; font-size: 14px; font-weight: 500;
    line-height: 1.6; margin: 1.2rem 0;
}
.s-failed {
    background: #FEF2F2; border: 1.5px solid #DC2626; border-radius: 12px;
    padding: 15px 20px; color: #7F1D1D; font-size: 14px; font-weight: 500;
    line-height: 1.6; margin: 1.2rem 0;
}
.s-locked {
    background: #FEF3C7; border: 1.5px solid #F59E0B; border-radius: 12px;
    padding: 15px 20px; color: #92400E; font-size: 14px; font-weight: 500;
    line-height: 1.6; margin: 1.2rem 0;
}
.s-ttl { font-weight: 700; font-size: 15px; margin-bottom: 3px; }

/* INFO BOX */
.info-box {
    background: #EFF6FF; border: 1.5px solid #3B82F6; border-radius: 10px;
    padding: 14px 18px; color: #1E40AF; font-size: 14px; line-height: 1.6; margin: 1rem 0;
}

/* BUTTONS */
div.stButton > button {
    background: linear-gradient(135deg, #1A1F71 0%, #0D47A1 100%) !important;
    color: #fff !important; border: none !important; border-radius: 10px !important;
    padding: 13px 22px !important; font-size: 14px !important; font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important; transition: all .2s ease !important;
    box-shadow: 0 3px 10px rgba(26,31,113,0.25) !important;
}
div.stButton > button:hover    { transform: translateY(-1px) !important; box-shadow: 0 2px 16px rgba(26,31,113,0.35) !important; }
div.stButton > button:disabled { background: #E4E7EB !important; color: #9CA3AF !important; box-shadow: none !important; transform: none !important; }

/* INPUTS */
.stTextInput > label { font-size: 13px !important; font-weight: 600 !important; color: #374151 !important; }
.stTextInput > div > div > input {
    border: 1.5px solid #E4E7EB !important; border-radius: 10px !important;
    padding: 11px 15px !important; font-size: 14px !important;
    font-family: 'Inter', sans-serif !important; background: #fff !important;
    transition: all .2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #1A1F71 !important; box-shadow: 0 0 0 3px rgba(26,31,113,0.1) !important;
}
.stFileUploader > label { font-size: 13px !important; font-weight: 600 !important; color: #374151 !important; }

/* DOWNLOAD BUTTON */
.stDownloadButton > button {
    background: linear-gradient(135deg, #F7B600 0%, #FFD34E 100%) !important;
    color: #1A1F71 !important; border: none !important; border-radius: 10px !important;
    padding: 11px 20px !important; font-weight: 600 !important; font-size: 14px !important;
    box-shadow: 0 3px 10px rgba(247,182,0,0.3) !important;
}
.stDownloadButton > button:hover { transform: translateY(-1px) !important; }

/* FOOTER */
.app-footer {
    text-align: center; padding: 2rem 0 1rem; font-size: 12px; color: #9CA3AF;
    border-top: 1px solid #E4E7EB; margin-top: 3rem;
}
.app-footer a { color: #1A1F71; text-decoration: none; font-weight: 600; }
</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "view":    "config",    # "config" | "pipeline"
    "step":    1,
    "config":  {},          # stores config_file name + pbi_workspace
    "s1_done": False, "s1_fail": False, "s1": {},
    "s2_done": False, "s2_fail": False, "s2": {},
    "s3_done": False, "s3_fail": False, "s3": {},
    "s4_done": False, "s4_fail": False, "s4": {},
    "s5_done": False, "s5_fail": False, "s5": {},
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# =========================================================
# HEADER  — always visible
# =========================================================

st.markdown("""
<div class="vis-header">
    <h1>Visa BI Migration Platform</h1>
    <p>Enterprise-Grade Tableau &rarr; Power BI Migration Pipeline</p>
    <div class="badge-row">
        <div class="badge"><div class="badge-dot"></div>Enterprise Secure</div>
        <div class="badge"><div class="badge-dot"></div>Automated</div>
        <div class="badge"><div class="badge-dot"></div>Validated</div>
        <div class="badge"><div class="badge-dot"></div>5-Stage Pipeline</div>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HELPER FUNCTIONS  — every one emits complete HTML only
# =========================================================

def card(icon, title, desc):
    st.markdown(
        f'<div class="scard">'
        f'<div class="scard-head">'
        f'<div class="scard-icon">{icon}</div>'
        f'<div class="scard-title">{title}</div>'
        f'</div>'
        f'<div class="scard-desc">{desc}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def ctx_bar():
    """Show config inputs as a read-only context bar at top of each step."""
    cfg = st.session_state.config
    fname = cfg.get("config_file", "—")
    ws    = cfg.get("pbi_workspace", "—")
    st.markdown(
        f'<div class="ctx-bar">'
        f'<div class="ctx-item"><div class="ctx-lbl">Config File</div><div class="ctx-val">📄 {fname}</div></div>'
        f'<div style="width:1px;background:#E4E7EB;align-self:stretch;"></div>'
        f'<div class="ctx-item"><div class="ctx-lbl">Power BI Workspace</div><div class="ctx-val">🏢 {ws}</div></div>'
        f'</div>',
        unsafe_allow_html=True
    )

def ok(msg):
    st.markdown(
        f'<div class="s-success"><div class="s-ttl">&#9989; Step Successful</div>{msg}</div>',
        unsafe_allow_html=True
    )

def fail_banner(msg):
    st.markdown(
        f'<div class="s-failed"><div class="s-ttl">&#10060; Step Failed</div>{msg}</div>',
        unsafe_allow_html=True
    )

def locked_banner():
    st.markdown(
        '<div class="s-locked"><div class="s-ttl">&#128274; Step Locked</div>'
        'Complete the previous step first.</div>',
        unsafe_allow_html=True
    )

def metrics(tiles):
    html = "".join(
        f'<div class="metric-tile">'
        f'<span class="m-icon">{em}</span>'
        f'<div class="m-val">{val}</div>'
        f'<div class="m-label">{lbl}</div>'
        f'</div>'
        for em, val, lbl in tiles
    )
    st.markdown(f'<div class="metric-row">{html}</div>', unsafe_allow_html=True)

def show_tasks(rows):
    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

def dl(rows, prefix):
    if rows:
        csv = pd.DataFrame(rows).to_csv(index=False)
        st.download_button(
            f"📥 Download {prefix} Report", csv,
            f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "text/csv", use_container_width=True
        )

def nxt(label, to):
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(f"{label} →", key=f"nxt{to}", use_container_width=True):
        st.session_state.step = to
        st.rerun()


# =========================================================
# VIEW A — CONFIG LANDING PAGE (step 0)
# =========================================================

if st.session_state.view == "config":

    st.markdown("""
    <div class="config-card">
        <div class="config-title">Configure Your Migration</div>
        <div class="config-sub">
            Provide just two inputs to begin. Everything else is handled automatically
            from your configuration file.
        </div>
        <div class="config-steps">
            <div class="config-step">
                <div class="cs-num">1</div>
                <div class="cs-lbl">Discovery</div>
                <div class="cs-sub">Inventory & connect</div>
            </div>
            <div class="config-step">
                <div class="cs-num">2</div>
                <div class="cs-lbl">Data Modelling</div>
                <div class="cs-sub">Semantic model</div>
            </div>
            <div class="config-step">
                <div class="cs-num">3</div>
                <div class="cs-lbl">Dashboard Rebuild</div>
                <div class="cs-sub">PBI dashboards</div>
            </div>
            <div class="config-step">
                <div class="cs-num">4</div>
                <div class="cs-lbl">Unit Testing</div>
                <div class="cs-sub">Validate & compare</div>
            </div>
            <div class="config-step">
                <div class="cs-num">5</div>
                <div class="cs-lbl">Deployment</div>
                <div class="cs-sub">Publish to PBI</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Center the form inputs below the card
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown("<br>", unsafe_allow_html=True)
        uploaded = st.file_uploader(
            "Upload Config File",
            type=["json", "yaml", "yml", "ini", "cfg", "toml"],
            help="Upload your migration config file containing Tableau server details, credentials, and mappings."
        )

        pbi_workspace = st.text_input(
            "Power BI Workspace",
            placeholder="e.g. Finance-Analytics-Prod",
            help="The target Power BI workspace where reports will be deployed."
        )

        st.markdown("<br>", unsafe_allow_html=True)

        start_clicked = st.button(
            "🚀 Start Migration",
            key="start_migration",
            use_container_width=True,
            disabled=(uploaded is None or not pbi_workspace.strip())
        )

        if uploaded is None or not pbi_workspace.strip():
            st.caption("⬆️ Upload a config file and enter your workspace name to enable migration.")

    if start_clicked and uploaded and pbi_workspace.strip():
        # Save config to session
        st.session_state.config = {
            "config_file":     uploaded.name,
            "pbi_workspace":   pbi_workspace.strip(),
        }

        # Run Discovery automatically in the background
        with st.spinner("Starting migration — running Discovery…"):
            res = discovery_function(uploaded.name, pbi_workspace.strip())

        st.session_state.s1 = {**res.get("data", {}), "reason": res["reason"]}
        st.session_state.s1_done = res["success"]
        st.session_state.s1_fail = not res["success"]
        st.session_state.step    = 1
        st.session_state.view    = "pipeline"
        st.rerun()


# =========================================================
# VIEW B — PIPELINE (steps 1–5)
# =========================================================

else:

    # ── STEPPER ──────────────────────────────────────────

    STEPS = [
        (1, "Discovery",         "Connect & Inventory"),
        (2, "Data Modelling",    "Model & Relationships"),
        (3, "Dashboard Rebuild", "Build & Format"),
        (4, "Unit Testing",      "Validate & Compare"),
        (5, "Deployment",        "Publish & Release"),
    ]

    def _cls(i):
        if st.session_state.get(f"s{i}_done"): return "step-col s-done"
        if st.session_state.get(f"s{i}_fail"): return "step-col s-failed"
        if st.session_state.step == i:         return "step-col s-active"
        return "step-col"

    def _ico(i):
        if st.session_state.get(f"s{i}_done"): return "&#10003;"
        if st.session_state.get(f"s{i}_fail"): return "&#10005;"
        return str(i)

    step_html = "".join(
        f'<div class="{_cls(i)}">'
        f'<div class="step-circle">{_ico(i)}</div>'
        f'<div class="step-name">{name}</div>'
        f'<div class="step-sub">{sub}</div>'
        f'</div>'
        for i, name, sub in STEPS
    )

    st.markdown(
        f'<div class="stepper-wrap">'
        f'<div class="stepper"><div class="stepper-track"></div>{step_html}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Nav buttons
    nb1, nb2, nb3, nb4, nb5 = st.columns(5)
    for col, (idx, name, _) in zip([nb1, nb2, nb3, nb4, nb5], STEPS):
        with col:
            is_locked = idx > 1 and not st.session_state.get(f"s{idx-1}_done", False)
            if st.button(name, key=f"nav{idx}", use_container_width=True, disabled=is_locked):
                st.session_state.step = idx
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── STEP 1: DISCOVERY ────────────────────────────────

    if st.session_state.step == 1:
        card("🔍", "Discovery",
             "Connecting to Tableau Server via REST API to retrieve a complete inventory "
             "of workbooks, data sources, tables, and columns.")

        ctx_bar()

        # Discovery ran automatically — show results immediately
        if st.session_state.s1_done:
            d = st.session_state.s1
            ok(d.get("reason", ""))
            metrics([
                ("🗂️", d.get("workbooks",    0), "Workbooks"),
                ("🔗", d.get("datasources",  0), "Data Sources"),
                ("📋", d.get("tables",       0), "Tables"),
                ("📌", d.get("columns",      0), "Columns"),
                ("👥", d.get("users",        0), "Users"),
            ])
            st.markdown("##### Task Status")
            show_tasks(d.get("tasks", []))
            dl(d.get("tasks", []), "Discovery")
            nxt("Continue to Data Modelling", 2)

        elif st.session_state.s1_fail:
            fail_banner(st.session_state.s1.get("reason", "Discovery failed. Check your config file."))
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("← Back to Configuration", key="back_cfg", use_container_width=True):
                st.session_state.view = "config"
                st.rerun()

    # ── STEP 2: DATA MODELLING ───────────────────────────

    elif st.session_state.step == 2:
        card("🗄️", "Data Modelling",
             "Building the semantic model in Power BI Service from the Tableau inventory. "
             "Covers table mapping, relationship configuration, and DAX measure generation.")

        ctx_bar()

        if not st.session_state.s1_done:
            locked_banner()
        else:
            if st.button("🗄️ Run Data Modelling", key="run2", use_container_width=True):
                with st.spinner("Creating semantic model…"):
                    res = data_modelling_function(
                        st.session_state.s1,
                        st.session_state.config.get("pbi_workspace", "")
                    )
                st.session_state.s2 = {**res.get("data", {}), "reason": res["reason"]}
                st.session_state.s2_done = res["success"]
                st.session_state.s2_fail = not res["success"]
                st.rerun()

            if st.session_state.s2_done:
                d = st.session_state.s2
                ok(d.get("reason", ""))
                metrics([
                    ("📋", d.get("tables_modelled",  0),          "Tables Modelled"),
                    ("🔗", d.get("relationships",    0),          "Relationships"),
                    ("📐", d.get("measures_created", 0),          "DAX Measures"),
                    ("💾", f"{d.get('model_size_mb', 0)} MB",     "Model Size"),
                ])
                st.markdown("##### Task Status")
                show_tasks(d.get("tasks", []))
                dl(d.get("tasks", []), "DataModelling")
                nxt("Continue to Dashboard Rebuild", 3)

            elif st.session_state.s2_fail:
                fail_banner(st.session_state.s2.get("reason", "Data modelling failed."))

    # ── STEP 3: DASHBOARD REBUILD ────────────────────────

    elif st.session_state.step == 3:
        card("📊", "Dashboard Rebuild",
             "Extracting Tableau dashboard metadata and provisioning Power BI dashboards "
             "from the generated specification file.")

        ctx_bar()

        if not st.session_state.s2_done:
            locked_banner()
        else:
            if st.button("📊 Run Dashboard Rebuild", key="run3", use_container_width=True):
                with st.spinner("Extracting metadata and building dashboards…"):
                    res = dashboard_rebuild_function(
                        st.session_state.s2,
                        st.session_state.config.get("pbi_workspace", "")
                    )
                st.session_state.s3 = {**res.get("data", {}), "reason": res["reason"]}
                st.session_state.s3_done = res["success"]
                st.session_state.s3_fail = not res["success"]
                st.rerun()

            if st.session_state.s3_done:
                d = st.session_state.s3
                ok(d.get("reason", ""))
                st.markdown('<div class="info-box"><strong>ℹ️ Note:</strong> Programmatic formatting of PBI dashboards '
                            'is currently under investigation by the team.</div>', unsafe_allow_html=True)
                metrics([
                    ("📤", d.get("dashboards_extracted", 0), "Extracted"),
                    ("✅", d.get("dashboards_built",     0), "Built"),
                    ("⚠️", d.get("dashboards_manual",   0), "Manual Work"),
                    ("📈", d.get("visuals_created",      0), "Visuals"),
                ])
                st.markdown("##### Task Status")
                show_tasks(d.get("tasks", []))
                dl(d.get("tasks", []), "DashboardRebuild")
                nxt("Continue to Unit Testing", 4)

            elif st.session_state.s3_fail:
                fail_banner(st.session_state.s3.get("reason", "Dashboard rebuild failed."))

    # ── STEP 4: UNIT TESTING ─────────────────────────────

    elif st.session_state.step == 4:
        card("🧪", "Unit Testing",
             "Validating migrated Power BI dashboards against the original Tableau source — "
             "data comparison and image analysis.")

        ctx_bar()

        if not st.session_state.s3_done:
            locked_banner()
        else:
            if st.button("🧪 Run Unit Tests", key="run4", use_container_width=True):
                with st.spinner("Running validation suite…"):
                    res = unit_testing_function(
                        st.session_state.s3,
                        st.session_state.config.get("pbi_workspace", "")
                    )
                st.session_state.s4 = {**res.get("data", {}), "reason": res["reason"]}
                st.session_state.s4_done = res["success"]
                st.session_state.s4_fail = not res["success"]
                st.rerun()

            if st.session_state.s4_done:
                d = st.session_state.s4
                ok(d.get("reason", ""))
                metrics([
                    ("✅", d.get("data_passed",      0), "Data Tests Passed"),
                    ("❌", d.get("data_failed",       0), "Data Tests Failed"),
                    ("📄", d.get("sheet_matches",     0), "Sheet Matches"),
                    ("⚠️", d.get("sheet_mismatches", 0), "Sheet Mismatches"),
                    ("🖼️", d.get("images_analysed",  0), "Images Analysed"),
                ])
                st.markdown("##### Task Status")
                show_tasks(d.get("tasks", []))
                dl(d.get("tasks", []), "UnitTesting")
                nxt("Continue to Deployment", 5)

            elif st.session_state.s4_fail:
                fail_banner(st.session_state.s4.get("reason", "Unit testing failed."))

    # ── STEP 5: DEPLOYMENT ───────────────────────────────

    elif st.session_state.step == 5:
        card("🚀", "Deployment",
             "Publishing all Power BI files to the configured workspace in PBI Service.")

        ctx_bar()

        if not st.session_state.s4_done:
            locked_banner()
        else:
            if st.button("🚀 Deploy to Power BI Service", key="run5", use_container_width=True):
                with st.spinner("Publishing PBI files to service…"):
                    res = deployment_function(
                        st.session_state.s4,
                        st.session_state.config.get("pbi_workspace", "")
                    )
                st.session_state.s5 = {**res.get("data", {}), "reason": res["reason"]}
                st.session_state.s5_done = res["success"]
                st.session_state.s5_fail = not res["success"]
                st.rerun()

            if st.session_state.s5_done:
                d = st.session_state.s5
                ok(d.get("reason", ""))
                metrics([
                    ("📦", d.get("files_deployed",    0),  "Files Deployed"),
                    ("🏢", d.get("workspace",        "—"), "Workspace"),
                    ("🕐", d.get("deployment_time",  "—"), "Deployed At"),
                ])
                st.markdown("##### Task Status")
                show_tasks(d.get("tasks", []))
                dl(d.get("tasks", []), "Deployment")

                st.markdown(
                    '<div class="s-success" style="margin-top:1.5rem;">'
                    '<div class="s-ttl">&#127881; Migration Pipeline Complete!</div>'
                    'All 5 stages completed successfully. '
                    'Your Power BI environment is live and validated.'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🔄 Start New Migration", key="reset", use_container_width=True):
                    for k in list(st.session_state.keys()):
                        del st.session_state[k]
                    st.rerun()

            elif st.session_state.s5_fail:
                fail_banner(st.session_state.s5.get("reason",
                    "Deployment failed. Check workspace permissions."))

    # ── Back link ─────────────────────────────────────────

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Edit Configuration", key="edit_cfg", use_container_width=False):
        st.session_state.view = "config"
        st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="app-footer">
    <strong>BI Migration Platform</strong> &middot; Enterprise Edition v2.0 &middot;
    <a href="#">Documentation</a> &middot; <a href="#">Support</a> &middot; <a href="#">Contact</a>
</div>
""", unsafe_allow_html=True)