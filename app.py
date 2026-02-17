import streamlit as st
import time
import pandas as pd
from datetime import datetime

# =========================================================
# DUMMY FUNCTIONS
# =========================================================

def migration_function(tableau_path, workspace, data_source, report_name):
    try:
        time.sleep(2)
        if not tableau_path or not workspace:
            return {'success': False, 'message': 'Missing required parameters', 'data': {}}
        
        return {
            'success': True,
            'message': 'Migration completed successfully',
            'data': {
                'data_sources': 24,
                'calculated_fields': 156,
                'dashboards': 18,
                'success_rate': 100,
                'components': [
                    {'name': 'Data Connections', 'original': 24, 'migrated': 24, 'status': 'Complete'},
                    {'name': 'Calculated Fields', 'original': 156, 'migrated': 156, 'status': 'Complete'},
                    {'name': 'Parameters', 'original': 12, 'migrated': 12, 'status': 'Complete'},
                    {'name': 'Dashboard Sheets', 'original': 18, 'migrated': 18, 'status': 'Complete'},
                    {'name': 'Filters & Actions', 'original': 45, 'migrated': 45, 'status': 'Complete'},
                    {'name': 'Visual Formatting', 'original': 203, 'migrated': 203, 'status': 'Complete'},
                ]
            }
        }
    except Exception as e:
        return {'success': False, 'message': f'Migration failed: {str(e)}', 'data': {}}


def deployment_function(migration_data, enable_rls, schedule_refresh, enable_sharing, send_notification):
    try:
        time.sleep(2)
        if not migration_data or 'report_name' not in migration_data:
            return {'success': False, 'message': 'Invalid migration data', 'data': {}}
        
        workspace_name = migration_data.get('workspace', 'Unknown')
        report_name = migration_data.get('report_name', 'Unknown')
        
        return {
            'success': True,
            'message': 'Deployment completed successfully',
            'data': {
                'workspace': workspace_name,
                'report_name': report_name,
                'report_id': 'rpt_' + str(hash(report_name))[-8:],
                'deployment_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': 'Active',
                'report_url': f'https://app.powerbi.com/groups/workspace-{hash(workspace_name)}/reports/{hash(report_name)}',
            }
        }
    except Exception as e:
        return {'success': False, 'message': f'Deployment failed: {str(e)}', 'data': {}}


def testing_function(deployment_data, test_config):
    try:
        time.sleep(2)
        if not deployment_data or 'report_name' not in deployment_data:
            return {'success': False, 'message': 'Invalid deployment data', 'data': {}}
        
        test_results = []
        
        if test_config.get('data_accuracy', False):
            test_results.append({'category': 'Data Accuracy', 'tests_run': 45, 'passed': 45, 'failed': 0, 'status': 'Passed'})
        
        if test_config.get('calculations', False):
            test_results.append({'category': 'Calculation Verification', 'tests_run': 156, 'passed': 156, 'failed': 0, 'status': 'Passed'})
        
        if test_config.get('visuals', False):
            test_results.append({'category': 'Visual Rendering', 'tests_run': 72, 'passed': 72, 'failed': 0, 'status': 'Passed'})
        
        if test_config.get('performance', False):
            test_results.append({'category': 'Performance', 'tests_run': 28, 'passed': 28, 'failed': 0, 'status': 'Passed'})
        
        if test_config.get('interactions', False):
            test_results.append({'category': 'Interactions', 'tests_run': 36, 'passed': 36, 'failed': 0, 'status': 'Passed'})
        
        if test_config.get('accessibility', False):
            test_results.append({'category': 'Accessibility', 'tests_run': 15, 'passed': 15, 'failed': 0, 'status': 'Passed'})
        
        total_tests = sum(r['tests_run'] for r in test_results)
        total_passed = sum(r['passed'] for r in test_results)
        
        return {
            'success': True,
            'message': 'All tests passed successfully',
            'data': {
                'test_results': test_results,
                'total_tests': total_tests,
                'total_passed': total_passed,
                'total_failed': 0,
                'accuracy': 100,
                'calculations_verified': 156,
                'visuals_validated': 18,
                'avg_query_time': 0.8
            }
        }
    except Exception as e:
        return {'success': False, 'message': f'Testing failed: {str(e)}', 'data': {}}

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Visa BI Migration Platform",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="💳"
)

# =========================================================
# CSS STYLING
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --visa-navy: #1A1F71;
    --visa-blue: #00579F;
    --visa-gold: #F7B600;
}

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

#MainMenu, footer, header {visibility: hidden;}

.main {
    background: linear-gradient(180deg, #F9FAFB 0%, #FFFFFF 100%);
}

.block-container {
    padding: 2rem 3rem !important;
    max-width: 1600px;
    margin: 0 auto;
}

/* Header */
.premium-header {
    background: linear-gradient(135deg, var(--visa-navy) 0%, #1434A4 100%);
    padding: 3rem 4rem;
    border-radius: 24px;
    margin-bottom: 3rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.header-title {
    font-size: 44px;
    font-weight: 800;
    color: white;
    margin: 0 0 0.75rem 0;
    letter-spacing: -0.02em;
}

.header-subtitle {
    font-size: 18px;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.85);
    margin: 0 0 1.5rem 0;
}

.header-badges {
    display: flex;
    gap: 12px;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 100px;
    font-size: 13px;
    font-weight: 600;
    color: white;
}

.badge-icon {
    width: 16px;
    height: 16px;
    background: var(--visa-gold);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    color: var(--visa-navy);
}

/* Stepper */
.stepper-container {
    max-width: 1200px;
    margin: 0 auto 3rem auto;
}

.stepper {
    display: flex;
    position: relative;
    justify-content: space-between;
}

.stepper-line {
    position: absolute;
    top: 28px;
    left: 15%;
    right: 15%;
    height: 3px;
    background: #E4E7EB;
    border-radius: 10px;
}

.stepper-line-progress {
    height: 100%;
    background: linear-gradient(90deg, var(--visa-navy) 0%, var(--visa-blue) 50%, var(--visa-gold) 100%);
    border-radius: 10px;
    transition: width 0.6s ease;
}

.step {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    position: relative;
    z-index: 1;
}

.step-circle {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: white;
    border: 3px solid #E4E7EB;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 12px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.step.active .step-circle {
    background: var(--visa-navy);
    border-color: var(--visa-navy);
    color: white;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 0 0 4px rgba(26, 31, 113, 0.1);
    transform: scale(1.08);
}

.step.completed .step-circle {
    background: #059669;
    border-color: #059669;
    color: white;
}

.step-label {
    font-size: 14px;
    font-weight: 600;
    color: #6B7280;
}

.step.active .step-label {
    color: var(--visa-navy);
    font-weight: 700;
}

.step-number {
    font-size: 12px;
    color: #9CA3AF;
    margin-top: 4px;
}

/* Content Card */
.content-card {
    background: white;
    border-radius: 20px;
    padding: 3rem;
    margin-bottom: 2rem;
    border: 1px solid #E4E7EB;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #1A1F36;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 12px;
}

.section-icon {
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, var(--visa-navy) 0%, var(--visa-blue) 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: white;
}

.section-description {
    font-size: 15px;
    color: #6B7280;
    margin-bottom: 2.5rem;
    line-height: 1.6;
}

/* Form Inputs */
.stTextInput > label {
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #1A1F36 !important;
}

.stTextInput > div > div > input {
    border: 1.5px solid #E4E7EB !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    transition: all 0.2s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: var(--visa-navy) !important;
    box-shadow: 0 0 0 3px rgba(26, 31, 113, 0.08) !important;
}

/* Checkboxes */
.stCheckbox {
    background: #FAFBFC;
    padding: 14px 16px;
    border-radius: 10px;
    border: 1.5px solid #E4E7EB;
    transition: all 0.2s ease;
}

.stCheckbox:hover {
    border-color: var(--visa-blue);
    background: white;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(135deg, var(--visa-navy) 0%, var(--visa-blue) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
}

div.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
}

div.stButton > button:disabled {
    background: #E4E7EB !important;
    color: #6B7280 !important;
}

/* Info Box */
.info-box {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border: 1.5px solid #3B82F6;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 1.5rem 0;
    font-size: 14px;
    line-height: 1.6;
    color: #1E40AF;
}

/* Alerts */
.alert {
    border-radius: 12px;
    padding: 16px 20px;
    margin: 1.5rem 0;
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 15px;
    font-weight: 500;
}

.alert-success {
    background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
    border: 1.5px solid #059669;
    color: #047857;
}

.alert-error {
    background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
    border: 1.5px solid #DC2626;
    color: #991B1B;
}

.alert-warning {
    background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
    border: 1.5px solid #F59E0B;
    color: #92400E;
}

.alert-icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    flex-shrink: 0;
}

.alert-success .alert-icon {
    background: #059669;
    color: white;
}

.alert-error .alert-icon {
    background: #DC2626;
    color: white;
}

/* Metric Cards */
.metric-card {
    background: white;
    border: 1.5px solid #E4E7EB;
    border-radius: 16px;
    padding: 1.75rem;
    transition: all 0.3s ease;
}

.metric-card:hover {
    border-color: var(--visa-navy);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    transform: translateY(-2px);
}

.metric-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, var(--visa-navy) 0%, var(--visa-blue) 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: white;
    margin-bottom: 12px;
}

.metric-label {
    font-size: 13px;
    font-weight: 600;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 36px;
    font-weight: 800;
    color: var(--visa-navy);
    line-height: 1;
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(135deg, var(--visa-gold) 0%, #FFD700 100%) !important;
    color: var(--visa-navy) !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* Responsive */
@media (max-width: 768px) {
    .block-container {
        padding: 1.5rem !important;
    }
    
    .premium-header {
        padding: 2rem;
    }
    
    .header-title {
        font-size: 32px;
    }
    
    .stepper {
        flex-direction: column;
        gap: 1.5rem;
    }
    
    .stepper-line {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "current_step" not in st.session_state:
    st.session_state.current_step = 1

if "migration_complete" not in st.session_state:
    st.session_state.migration_complete = False

if "deployment_complete" not in st.session_state:
    st.session_state.deployment_complete = False

if "testing_complete" not in st.session_state:
    st.session_state.testing_complete = False

if "migration_data" not in st.session_state:
    st.session_state.migration_data = {}

if "deployment_data" not in st.session_state:
    st.session_state.deployment_data = {}

if "testing_data" not in st.session_state:
    st.session_state.testing_data = {}

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="premium-header">
    <div class="header-title">Visa BI Migration Platform</div>
    <div class="header-subtitle">Enterprise-Grade Tableau to Power BI Migration Automation</div>
    <div class="header-badges">
        <div class="badge">
            <div class="badge-icon">✓</div>
            <span>Enterprise Secure</span>
        </div>
        <div class="badge">
            <div class="badge-icon">⚡</div>
            <span>Automated</span>
        </div>
        <div class="badge">
            <div class="badge-icon">🛡</div>
            <span>Validated</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# STEPPER
# =========================================================

def get_progress_width():
    if st.session_state.current_step == 1:
        return "0%"
    elif st.session_state.current_step == 2:
        return "50%"
    else:
        return "100%"

step1_class = "step active" if st.session_state.current_step == 1 else "step"
step2_class = "step active" if st.session_state.current_step == 2 else "step"
step3_class = "step active" if st.session_state.current_step == 3 else "step"

if st.session_state.migration_complete:
    step1_class += " completed"
if st.session_state.deployment_complete:
    step2_class += " completed"
if st.session_state.testing_complete:
    step3_class += " completed"

step1_icon = "✓" if st.session_state.migration_complete else "1"
step2_icon = "✓" if st.session_state.deployment_complete else "2"
step3_icon = "✓" if st.session_state.testing_complete else "3"

st.markdown(f"""
<div class="stepper-container">
    <div class="stepper">
        <div class="stepper-line">
            <div class="stepper-line-progress" style="width: {get_progress_width()};"></div>
        </div>
        <div class="{step1_class}">
            <div class="step-circle">{step1_icon}</div>
            <div class="step-label">Migration</div>
            <div class="step-number">Configure & Extract</div>
        </div>
        <div class="{step2_class}">
            <div class="step-circle">{step2_icon}</div>
            <div class="step-label">Deployment</div>
            <div class="step-number">Publish & Configure</div>
        </div>
        <div class="{step3_class}">
            <div class="step-circle">{step3_icon}</div>
            <div class="step-label">Testing</div>
            <div class="step-number">Validate & Verify</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← Migration", key="nav1", use_container_width=True):
        st.session_state.current_step = 1
        st.rerun()
with col2:
    if st.button("Deployment", key="nav2", disabled=not st.session_state.migration_complete, use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()
with col3:
    if st.button("Testing →", key="nav3", disabled=not st.session_state.deployment_complete, use_container_width=True):
        st.session_state.current_step = 3
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# STEP 1: MIGRATION
# =========================================================

if st.session_state.current_step == 1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-title">
        <div class="section-icon">🔄</div>
        <span>Migration Configuration</span>
    </div>
    <div class="section-description">
        Configure your Tableau to Power BI migration settings. Our automation engine will handle the complete conversion process.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        tableau_path = st.text_input(
            "Tableau Workbook Path",
            value=st.session_state.migration_data.get('tableau_path', ''),
            placeholder="/tableau/workbooks/financial_dashboard.twbx"
        )
        
        data_source = st.text_input(
            "Data Source Connection",
            value=st.session_state.migration_data.get('data_source', ''),
            placeholder="sqlserver://prod-db.visa.com"
        )
    
    with col2:
        workspace = st.text_input(
            "Power BI Workspace",
            value=st.session_state.migration_data.get('workspace', ''),
            placeholder="Finance-Analytics-Prod"
        )
        
        report_name = st.text_input(
            "Report Name",
            value=st.session_state.migration_data.get('report_name', ''),
            placeholder="Q1 Financial Dashboard"
        )
    
    st.markdown("""
    <div class="info-box">
        <strong>💡 Migration Intelligence:</strong> Our engine extracts all data sources, calculated fields, parameters, 
        and dashboard layouts from Tableau, then intelligently converts them to Power BI equivalents.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Start Migration Process", key="start_migration", use_container_width=True):
        if tableau_path and workspace and data_source and report_name:
            
            with st.spinner("Processing migration..."):
                result = migration_function(tableau_path, workspace, data_source, report_name)
            
            if result['success']:
                st.session_state.migration_data = {
                    "tableau_path": tableau_path,
                    "workspace": workspace,
                    "data_source": data_source,
                    "report_name": report_name,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    **result['data']
                }
                
                st.session_state.migration_complete = True
                st.rerun()
            
            else:
                st.markdown(f"""
                <div class="alert alert-error">
                    <div class="alert-icon">✕</div>
                    <div>{result["message"]}</div>
                </div>
                """, unsafe_allow_html=True)
            
        else:
            st.error("⚠️ Please fill in all required fields")
    
    # Show results if migration is complete
    if st.session_state.migration_complete and st.session_state.migration_data:
        st.markdown("""
        <div class="alert alert-success">
            <div class="alert-icon">✓</div>
            <div>Migration completed successfully</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Metrics
        cols = st.columns(4)
        metrics = [
            ("📊", "Data Sources", st.session_state.migration_data.get('data_sources', 0)),
            ("📐", "Calculated Fields", st.session_state.migration_data.get('calculated_fields', 0)),
            ("📈", "Dashboards", st.session_state.migration_data.get('dashboards', 0)),
            ("✓", "Success Rate", f"{st.session_state.migration_data.get('success_rate', 0)}%")
        ]
        
        for idx, (icon, label, value) in enumerate(metrics):
            with cols[idx]:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Component table
        if 'components' in st.session_state.migration_data:
            st.markdown("<br>", unsafe_allow_html=True)
            components_df = pd.DataFrame(st.session_state.migration_data['components'])
            components_df.columns = ['Component', 'Original Count', 'Migrated', 'Status']
            components_df['Status'] = '✅ ' + components_df['Status']
            
            st.dataframe(components_df, use_container_width=True, hide_index=True)
            
            csv = components_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Migration Report",
                data=csv,
                file_name=f"Migration_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Continue to Deployment →", key="goto_deploy", use_container_width=True):
            st.session_state.current_step = 2
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 2: DEPLOYMENT
# =========================================================

elif st.session_state.current_step == 2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-title">
        <div class="section-icon">🚀</div>
        <span>Power BI Deployment</span>
    </div>
    <div class="section-description">
        Deploy your migrated report to Power BI Service with enterprise security and configurations.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.migration_complete:
        st.markdown("""
        <div class="alert alert-warning">
            <div class="alert-icon">⚠</div>
            <div>Please complete the Migration step first</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### 📋 Migration Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Report Name:** {st.session_state.migration_data.get('report_name', 'N/A')}")
            st.markdown(f"**Source:** {st.session_state.migration_data.get('tableau_path', 'N/A')}")
        with col2:
            st.markdown(f"**Target Workspace:** {st.session_state.migration_data.get('workspace', 'N/A')}")
            st.markdown(f"**Migration Time:** {st.session_state.migration_data.get('timestamp', 'N/A')}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### ⚙️ Deployment Configuration")
        col1, col2 = st.columns(2)
        with col1:
            enable_rls = st.checkbox("Enable Row-Level Security", value=True)
            schedule_refresh = st.checkbox("Schedule Dataset Refresh", value=True)
        with col2:
            enable_sharing = st.checkbox("Enable Report Sharing", value=False)
            send_notification = st.checkbox("Send Deployment Notification", value=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Deploy to Power BI Service", key="start_deploy", use_container_width=True):
            
            with st.spinner("Deploying to Power BI..."):
                result = deployment_function(
                    st.session_state.migration_data,
                    enable_rls,
                    schedule_refresh,
                    enable_sharing,
                    send_notification
                )
            
            if result['success']:
                st.session_state.deployment_data = result['data']
                st.session_state.deployment_complete = True
                st.rerun()
            
            else:
                st.markdown(f"""
                <div class="alert alert-error">
                    <div class="alert-icon">✕</div>
                    <div>{result["message"]}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Show results if deployment is complete
        if st.session_state.deployment_complete and st.session_state.deployment_data:
            st.markdown("""
            <div class="alert alert-success">
                <div class="alert-icon">✓</div>
                <div>Deployment completed successfully</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📊 Deployment Details")
            st.markdown(f"**Workspace:** {st.session_state.deployment_data.get('workspace', 'N/A')}")
            st.markdown(f"**Report:** {st.session_state.deployment_data.get('report_name', 'N/A')}")
            st.markdown(f"**Report ID:** {st.session_state.deployment_data.get('report_id', 'N/A')}")
            st.markdown(f"**Status:** 🟢 {st.session_state.deployment_data.get('status', 'N/A')}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            report_url = st.session_state.deployment_data.get('report_url', 'https://app.powerbi.com')
            st.link_button("🔗 Open Report in Power BI", report_url, use_container_width=True)
            
            st.markdown("""
            <div class="info-box">
                <strong>📊 Report Access:</strong> Your report is now live in Power BI Service. 
                Access it through the workspace or embed it in enterprise applications.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Continue to Testing →", key="goto_test", use_container_width=True):
                st.session_state.current_step = 3
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 3: TESTING
# =========================================================

elif st.session_state.current_step == 3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-title">
        <div class="section-icon">🧪</div>
        <span>Automated Testing & Validation</span>
    </div>
    <div class="section-description">
        Run comprehensive validation tests to ensure data accuracy and performance standards.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.deployment_complete:
        st.markdown("""
        <div class="alert alert-warning">
            <div class="alert-icon">⚠</div>
            <div>Please complete the Deployment step first</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### 🔧 Test Configuration")
        
        col1, col2 = st.columns(2)
        with col1:
            test_data_accuracy = st.checkbox("Data Accuracy Validation", value=True)
            test_calculations = st.checkbox("Calculation Verification", value=True)
            test_visuals = st.checkbox("Visual Rendering Tests", value=True)
        with col2:
            test_performance = st.checkbox("Performance Benchmarking", value=True)
            test_interactions = st.checkbox("Interaction & Filter Tests", value=True)
            test_accessibility = st.checkbox("Accessibility Compliance", value=False)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🧪 Run Validation Suite", key="start_test", use_container_width=True):
            
            test_config = {
                'data_accuracy': test_data_accuracy,
                'calculations': test_calculations,
                'visuals': test_visuals,
                'performance': test_performance,
                'interactions': test_interactions,
                'accessibility': test_accessibility
            }
            
            with st.spinner("Running validation tests..."):
                result = testing_function(st.session_state.deployment_data, test_config)
            
            if result['success']:
                st.session_state.testing_data = result['data']
                st.session_state.testing_complete = True
                
                st.markdown(f"""
                <div class="alert alert-success">
                    <div class="alert-icon">✓</div>
                    <div>{result["message"]}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Metrics
                cols = st.columns(4)
                metrics = [
                    ("📊", "Accuracy", f"{result['data'].get('accuracy', 0)}%"),
                    ("📐", "Calculations", f"{result['data'].get('calculations_verified', 0)}/156"),
                    ("📈", "Visuals", f"{result['data'].get('visuals_validated', 0)}/18"),
                    ("⚡", "Query Time", f"{result['data'].get('avg_query_time', 0)}s")
                ]
                
                for idx, (icon, label, value) in enumerate(metrics):
                    with cols[idx]:
                        st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-icon">{icon}</div>
                            <div class="metric-label">{label}</div>
                            <div class="metric-value">{value}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Results table
                if 'test_results' in result['data']:
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    test_df = pd.DataFrame(result['data']['test_results'])
                    test_df.columns = ['Test Category', 'Tests Run', 'Passed', 'Failed', 'Status']
                    test_df['Status'] = '✅ ' + test_df['Status']
                    
                    st.dataframe(test_df, use_container_width=True, hide_index=True)
                    
                    csv = test_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Test Report",
                        data=csv,
                        file_name=f"Test_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                
                st.markdown("""
                <div class="info-box">
                    <strong>🎉 Migration Complete!</strong><br>
                    Your Tableau workbook has been successfully migrated, deployed, and validated. 
                    The Power BI report is now ready for production use.
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🔄 Start New Migration", key="reset", use_container_width=True):
                    st.session_state.current_step = 1
                    st.session_state.migration_complete = False
                    st.session_state.deployment_complete = False
                    st.session_state.testing_complete = False
                    st.session_state.migration_data = {}
                    st.session_state.deployment_data = {}
                    st.session_state.testing_data = {}
                    st.rerun()
            
            else:
                st.markdown(f"""
                <div class="alert alert-error">
                    <div class="alert-icon">✕</div>
                    <div>{result["message"]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: #6B7280; font-size: 13px; margin-top: 3rem; border-top: 1px solid #E4E7EB;">
    <strong>Visa BI Migration Platform</strong> • Enterprise Edition v1.0<br>
    <a href="#" style="color: var(--visa-navy); text-decoration: none;">Documentation</a> • 
    <a href="#" style="color: var(--visa-navy); text-decoration: none;">Support</a> • 
    <a href="#" style="color: var(--visa-navy); text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)