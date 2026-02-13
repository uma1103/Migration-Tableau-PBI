import json
import os

def function_text_from_json(json_file_path):
    """
    Reads the JSON file, extracts Tableau and Power BI inputs,
    and returns a descriptive text summary.
    """

    if not os.path.exists(json_file_path):
        return f"❌ JSON file not found at {json_file_path}"

    with open(json_file_path, "r") as f:
        data = json.load(f)

    # Extract Tableau inputs
    t1 = data["Tableau"].get("Server URL", "")
    t2 = data["Tableau"].get("Site Name", "")
    t3 = data["Tableau"].get("Project Name", "")
    t4 = data["Tableau"].get("Dashboard Name", "")

    # Extract Power BI inputs
    p1 = data["Power BI"].get("Tenant ID", "")
    p2 = data["Power BI"].get("Workspace Name", "")
    p3 = data["Power BI"].get("Report Name", "")

    # Format summary text
    output_text = (
        f"🔹 Tableau Inputs:\n"
        f"- Server URL: {t1}\n"
        f"- Site Name: {t2}\n"
        f"- Project Name: {t3}\n"
        f"- Dashboard Name: {t4}\n\n"
        f"🔹 Power BI Inputs:\n"
        f"- Tenant ID: {p1}\n"
        f"- Workspace Name: {p2}\n"
        f"- Report Name: {p3}\n"
    )

    return output_text
