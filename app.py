import streamlit as st
import time
import pandas as pd
from datetime import datetime

# =========================================================
# DUMMY FUNCTIONS - REPLACE THESE WITH YOUR ACTUAL FUNCTIONS
# =========================================================

def migration_function(tableau_path, workspace, data_source, report_name):
    """
    Dummy migration function - Replace with your actual implementation
    
    Args:
        tableau_path (str): Path to Tableau workbook
        workspace (str): Power BI workspace name
        data_source (str): Data source connection string
        report_name (str): Name for the migrated report
    
    Returns:
        dict: {
            'success': bool,
            'message': str,
            'data': dict with migration details
        }
    """
    try:
        # Simulate processing time
        time.sleep(2)
        
        # Simulate some validation
        if not tableau_path or not workspace:
            return {
                'success': False,
                'message': 'Missing required parameters',
                'data': {}
            }
        
        # Return success with migration data
        return {
            'success': True,
            'message': 'Migration completed successfully',
            'data': {
                'data_sources': 24,
                'calculated_fields': 156,
                'dashboards': 18,
                'parameters': 12,
                'filters': 45,
                'visuals': 203,
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
        return {
            'success': False,
            'message': f'Migration failed: {str(e)}',
            'data': {}
        }


def deployment_function(migration_data, enable_rls, schedule_refresh, enable_sharing, send_notification):
    """
    Dummy deployment function - Replace with your actual implementation
    
    Args:
        migration_data (dict): Data from migration step
        enable_rls (bool): Enable row-level security
        schedule_refresh (bool): Schedule dataset refresh
        enable_sharing (bool): Enable report sharing
        send_notification (bool): Send deployment notification
    
    Returns:
        dict: {
            'success': bool,
            'message': str,
            'data': dict with deployment details
        }
    """
    try:
        # Simulate processing time
        time.sleep(2)
        
        # Validate migration data
        if not migration_data or 'report_name' not in migration_data:
            return {
                'success': False,
                'message': 'Invalid migration data',
                'data': {}
            }
        
        # Simulate deployment
        workspace_name = migration_data.get('workspace', 'Unknown')
        report_name = migration_data.get('report_name', 'Unknown')
        
        # Return success with deployment data
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
                'rls_enabled': enable_rls,
                'refresh_scheduled': schedule_refresh,
                'sharing_enabled': enable_sharing
            }
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Deployment failed: {str(e)}',
            'data': {}
        }


def testing_function(deployment_data, test_config):
    """
    Dummy testing function - Replace with your actual implementation
    
    Args:
        deployment_data (dict): Data from deployment step
        test_config (dict): Test configuration with enabled tests
    
    Returns:
        dict: {
            'success': bool,
            'message': str,
            'data': dict with test results
        }
    """
    try:
        # Simulate processing time
        time.sleep(2)
        
        # Validate deployment data
        if not deployment_data or 'report_name' not in deployment_data:
            return {
                'success': False,
                'message': 'Invalid deployment data',
                'data': {}
            }
        
        # Build test results based on configuration
        test_results = []
        
        if test_config.get('data_accuracy', False):
            test_results.append({
                'category': 'Data Accuracy',
                'tests_run': 45,
                'passed': 45,
                'failed': 0,
                'status': 'Passed'
            })
        
        if test_config.get('calculations', False):
            test_results.append({
                'category': 'Calculation Verification',
                'tests_run': 156,
                'passed': 156,
                'failed': 0,
                'status': 'Passed'
            })
        
        if test_config.get('visuals', False):
            test_results.append({
                'category': 'Visual Rendering',
                'tests_run': 72,
                'passed': 72,
                'failed': 0,
                'status': 'Passed'
            })
        
        if test_config.get('performance', False):
            test_results.append({
                'category': 'Performance',
                'tests_run': 28,
                'passed': 28,
                'failed': 0,
                'status': 'Passed'
            })
        
        if test_config.get('interactions', False):
            test_results.append({
                'category': 'Interactions',
                'tests_run': 36,
                'passed': 36,
                'failed': 0,
                'status': 'Passed'
            })
        
        if test_config.get('accessibility', False):
            test_results.append({
                'category': 'Accessibility',
                'tests_run': 15,
                'passed': 15,
                'failed': 0,
                'status': 'Passed'
            })
        
        # Calculate totals
        total_tests = sum(r['tests_run'] for r in test_results)
        total_passed = sum(r['passed'] for r in test_results)
        
        # Return success with test data
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
        return {
            'success': False,
            'message': f'Testing failed: {str(e)}',
            'data': {}
        }

# =========================================================
# STREAMLIT APP CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Visa BI Migration Platform",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS STYLING
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(135deg, #F4F6FA 0%, #E8EBF5 100%);
    padding: 2rem 1rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.top-banner {
    background: linear-gradient(135deg, #1A1F71 0%, #3B4CC0 100%);
    padding: 2.5rem 3rem;
    border-radius: 20px;
    margin-bottom: 3rem;
    box-shadow: 0 10px 40px rgba(26, 31, 113, 0.25);
    position: relative;
    overflow: hidden;
}

.top-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: rgba(247, 182, 0, 0.1);
    border-radius: 50%;
}

.banner-content {
    position: relative;
    z-index: 1;
}

.banner-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.banner-subtitle {
    color: rgba(255, 255, 255, 0.85);
    font-size: 18px;
    font-weight: 500;
    margin-bottom: 1rem;
}

.banner-badge {
    display: inline-block;
    background: #F7B600;
    color: #1A1F71;
    padding: 8px 20px;
    border-radius: 25px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.progress-tracker {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 900px;
    margin: 3rem auto 2.5rem auto;
    position: relative;
}

.progress-line {
    position: absolute;
    top: 28px;
    left: 10%;
    right: 10%;
    height: 4px;
    background: #E5E7EB;
    z-index: 0;
}

.progress-line-fill {
    height: 100%;
    background: linear-gradient(90deg, #1A1F71 0%, #3B4CC0 100%);
    transition: width 0.5s ease;
}

.progress-step {
    flex: 1;
    text-align: center;
    position: relative;
    z-index: 1;
}

.progress-circle {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: white;
    border: 4px solid #E5E7EB;
    margin: 0 auto 12px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.progress-step.active .progress-circle {
    background: linear-gradient(135deg, #1A1F71 0%, #3B4CC0 100%);
    border-color: #1A1F71;
    box-shadow: 0 6px 20px rgba(26, 31, 113, 0.3);
    transform: scale(1.1);
    color: white;
}

.progress-step.completed .progress-circle {
    background: #10B981;
    border-color: #10B981;
    color: white;
}

.progress-label {
    font-size: 15px;
    font-weight: 600;
    color: #6B7280;
    margin-top: 8px;
}

.progress-step.active .progress-label {
    color: #1A1F71;
    font-weight: 700;
}

.content-card {
    background: white;
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    margin-bottom: 2rem;
}

.step-title {
    font-size: 32px;
    font-weight: 800;
    color: #1A1F71;
    margin-bottom: 0.5rem;
}

.step-description {
    font-size: 16px;
    color: #6B7280;
    margin-bottom: 2.5rem;
    line-height: 1.6;
}

div.stButton > button {
    background: linear-gradient(135deg, #1A1F71 0%, #3B4CC0 100%);
    color: white;
    border-radius: 12px;
    padding: 16px 32px;
    font-weight: 700;
    font-size: 16px;
    border: none;
    transition: all 0.3s ease;
    width: 100%;
    box-shadow: 0 4px 16px rgba(26, 31, 113, 0.25);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(26, 31, 113, 0.35);
}

div.stButton > button:disabled {
    background: #E5E7EB;
    color: #9CA3AF;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
}

.stTextInput > div > div > input {
    border: 2px solid #E5E7EB;
    border-radius: 12px;
    padding: 14px 18px;
    font-size: 15px;
    transition: all 0.3s ease;
    background: #F9FAFB;
}

.stTextInput > div > div > input:focus {
    border-color: #1A1F71;
    background: white;
    box-shadow: 0 0 0 3px rgba(26, 31, 113, 0.1);
}

.stTextInput label {
    font-weight: 600;
    color: #374151;
    font-size: 14px;
}

.info-box {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border-left: 4px solid #3B82F6;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 1.5rem 0;
    color: #1E40AF;
    font-size: 14px;
    line-height: 1.6;
}

.status-item {
    background: white;
    padding: 18px 20px;
    border-radius: 12px;
    margin-bottom: 12px;
    border-left: 4px solid #F7B600;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    font-size: 15px;
    color: #374151;
    font-weight: 500;
}

.success-alert {
    background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
    border: 2px solid #10B981;
    padding: 20px 24px;
    border-radius: 16px;
    margin: 2rem 0;
    font-size: 18px;
    font-weight: 700;
    color: #047857;
    box-shadow: 0 4px 16px rgba(16, 185, 129, 0.15);
}

.error-alert {
    background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
    border: 2px solid #EF4444;
    padding: 20px 24px;
    border-radius: 16px;
    margin: 2rem 0;
    font-size: 18px;
    font-weight: 700;
    color: #991B1B;
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.15);
}

.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    border: 2px solid #E5E7EB;
    text-align: center;
    transition: all 0.3s ease;
}

.metric-card:hover {
    border-color: #1A1F71;
    box-shadow: 0 4px 16px rgba(26, 31, 113, 0.1);
}

.metric-value {
    font-size: 32px;
    font-weight: 800;
    color: #1A1F71;
    margin-bottom: 4px;
}

.metric-label {
    font-size: 14px;
    color: #6B7280;
    font-weight: 600;
}

.warning-alert {
    background: #FEF3C7;
    border: 2px solid #F59E0B;
    padding: 18px 22px;
    border-radius: 12px;
    color: #92400E;
    font-weight: 600;
    margin: 1.5rem 0;
}

@media (max-width: 768px) {
    .banner-title {
        font-size: 28px;
    }
    .content-card {
        padding: 1.5rem;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE INITIALIZATION
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
<div class="top-banner">
    <div class="banner-content">
        <div class="banner-title">Visa BI Migration Platform</div>
        <div class="banner-subtitle">Enterprise-Grade Tableau → Power BI Migration Automation</div>
        <div class="banner-badge">SECURE • AUTOMATED • VALIDATED</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PROGRESS TRACKER
# =========================================================

def get_progress_width():
    if st.session_state.current_step == 1:
        return "0%"
    elif st.session_state.current_step == 2:
        return "50%"
    else:
        return "100%"

step1_class = "progress-step active" if st.session_state.current_step == 1 else "progress-step"
step2_class = "progress-step active" if st.session_state.current_step == 2 else "progress-step"
step3_class = "progress-step active" if st.session_state.current_step == 3 else "progress-step"

if st.session_state.migration_complete:
    step1_class += " completed"
if st.session_state.deployment_complete:
    step2_class += " completed"
if st.session_state.testing_complete:
    step3_class += " completed"

step1_icon = "✓" if st.session_state.migration_complete else "🔄"
step2_icon = "✓" if st.session_state.deployment_complete else "🚀"
step3_icon = "✓" if st.session_state.testing_complete else "🧪"

st.markdown(f"""
<div class="progress-tracker">
    <div class="progress-line">
        <div class="progress-line-fill" style="width: {get_progress_width()};"></div>
    </div>
    <div class="{step1_class}">
        <div class="progress-circle">{step1_icon}</div>
        <div class="progress-label">Migration</div>
    </div>
    <div class="{step2_class}">
        <div class="progress-circle">{step2_icon}</div>
        <div class="progress-label">Deployment</div>
    </div>
    <div class="{step3_class}">
        <div class="progress-circle">{step3_icon}</div>
        <div class="progress-label">Testing</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📍 Migration", key="nav1", use_container_width=True):
        st.session_state.current_step = 1
        st.rerun()

with col2:
    if st.button("📍 Deployment", key="nav2", disabled=not st.session_state.migration_complete, use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()

with col3:
    if st.button("📍 Testing", key="nav3", disabled=not st.session_state.deployment_complete, use_container_width=True):
        st.session_state.current_step = 3
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# STEP 1: MIGRATION
# =========================================================

if st.session_state.current_step == 1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-title">🔄 Migration Configuration</div>
    <div class="step-description">
        Configure your Tableau to Power BI migration settings. Our automation engine will handle the complete conversion process.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        tableau_path = st.text_input(
            "Tableau Workbook Path",
            value=st.session_state.migration_data.get('tableau_path', ''),
            placeholder="e.g., /tableau/workbooks/financial_dashboard.twbx",
            help="Full path to your Tableau workbook file"
        )
        
        data_source = st.text_input(
            "Data Source Connection",
            value=st.session_state.migration_data.get('data_source', ''),
            placeholder="e.g., sqlserver://prod-db.visa.com",
            help="Connection string for your data source"
        )
    
    with col2:
        workspace = st.text_input(
            "Power BI Workspace",
            value=st.session_state.migration_data.get('workspace', ''),
            placeholder="e.g., Finance-Analytics-Prod",
            help="Target Power BI workspace name"
        )
        
        report_name = st.text_input(
            "Report Name",
            value=st.session_state.migration_data.get('report_name', ''),
            placeholder="e.g., Q1 Financial Dashboard",
            help="Name for the migrated Power BI report"
        )
    
    st.markdown("""
    <div class="info-box">
        <strong>💡 Migration Process:</strong> Our engine will extract all data sources, calculated fields, parameters, 
        and dashboard layouts from Tableau, then intelligently convert them to Power BI equivalents using best practices 
        for DAX formulas and visual optimization.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Start Migration", key="start_migration", use_container_width=True):
        if tableau_path and workspace and data_source and report_name:
            
            with st.spinner("Running migration process..."):
                # Call the migration function
                result = migration_function(tableau_path, workspace, data_source, report_name)
            
            if result['success']:
                # Store migration data for next steps
                st.session_state.migration_data = {
                    "tableau_path": tableau_path,
                    "workspace": workspace,
                    "data_source": data_source,
                    "report_name": report_name,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    **result['data']
                }
                
                st.session_state.migration_complete = True
                
                st.markdown(f'<div class="success-alert">✅ {result["message"]}</div>', unsafe_allow_html=True)
                
                # Display metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('data_sources', 0)}</div>
                        <div class="metric-label">Data Sources</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('calculated_fields', 0)}</div>
                        <div class="metric-label">Calculated Fields</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('dashboards', 0)}</div>
                        <div class="metric-label">Dashboards</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('success_rate', 0)}%</div>
                        <div class="metric-label">Success Rate</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display component details
                if 'components' in result['data']:
                    components_df = pd.DataFrame(result['data']['components'])
                    components_df.columns = ['Component', 'Original Count', 'Migrated', 'Status']
                    components_df['Status'] = '✅ ' + components_df['Status']
                    
                    st.markdown("<br>", unsafe_allow_html=True)
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
            
            else:
                # Migration failed
                st.markdown(f'<div class="error-alert">❌ {result["message"]}</div>', unsafe_allow_html=True)
                st.error("Please check your inputs and try again.")
            
        else:
            st.error("⚠️ Please fill in all required fields to start migration.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 2: DEPLOYMENT
# =========================================================

elif st.session_state.current_step == 2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-title">🚀 Power BI Deployment</div>
    <div class="step-description">
        Deploy your migrated report to Power BI Service. The deployment process includes authentication, 
        dataset publishing, and report configuration.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.migration_complete:
        st.markdown('<div class="warning-alert">⚠️ Please complete the Migration step before proceeding to Deployment.</div>', unsafe_allow_html=True)
    else:
        # Display migration summary
        st.markdown("### 📋 Migration Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Report Name:** {st.session_state.migration_data.get('report_name', 'N/A')}")
            st.markdown(f"**Source:** {st.session_state.migration_data.get('tableau_path', 'N/A')}")
        with col2:
            st.markdown(f"**Target Workspace:** {st.session_state.migration_data.get('workspace', 'N/A')}")
            st.markdown(f"**Migration Time:** {st.session_state.migration_data.get('timestamp', 'N/A')}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Deployment configuration
        col1, col2 = st.columns(2)
        with col1:
            enable_rls = st.checkbox("Enable Row-Level Security", value=True)
            schedule_refresh = st.checkbox("Schedule Dataset Refresh", value=True)
        with col2:
            enable_sharing = st.checkbox("Enable Report Sharing", value=False)
            send_notification = st.checkbox("Send Deployment Notification", value=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Deploy to Power BI", key="start_deploy", use_container_width=True):
            
            with st.spinner("Running deployment process..."):
                # Call the deployment function
                result = deployment_function(
                    st.session_state.migration_data,
                    enable_rls,
                    schedule_refresh,
                    enable_sharing,
                    send_notification
                )
            
            if result['success']:
                # Store deployment data for next step
                st.session_state.deployment_data = result['data']
                st.session_state.deployment_complete = True
                
                st.markdown(f'<div class="success-alert">✅ {result["message"]}</div>', unsafe_allow_html=True)
                
                # Display deployment details
                st.markdown("### 📊 Deployment Details")
                st.markdown(f"**Workspace:** {result['data'].get('workspace', 'N/A')}")
                st.markdown(f"**Report:** {result['data'].get('report_name', 'N/A')}")
                st.markdown(f"**Report ID:** {result['data'].get('report_id', 'N/A')}")
                st.markdown(f"**Deployment Time:** {result['data'].get('deployment_time', 'N/A')}")
                st.markdown(f"**Status:** 🟢 {result['data'].get('status', 'Unknown')}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Report link
                report_url = result['data'].get('report_url', 'https://app.powerbi.com')
                st.link_button("🔗 Open Report in Power BI", report_url, use_container_width=True)
                
                st.markdown("""
                <div class="info-box">
                    <strong>📊 Report Preview:</strong> Your report is now live in Power BI Service. 
                    Click the button above to view it in your workspace. You can also embed this report 
                    in SharePoint, Teams, or other applications.
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Continue to Testing →", key="goto_test", use_container_width=True):
                    st.session_state.current_step = 3
                    st.rerun()
            
            else:
                # Deployment failed
                st.markdown(f'<div class="error-alert">❌ {result["message"]}</div>', unsafe_allow_html=True)
                st.error("Please check the deployment configuration and try again.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 3: TESTING
# =========================================================

elif st.session_state.current_step == 3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-title">🧪 Automated Testing & Validation</div>
    <div class="step-description">
        Run comprehensive validation tests to ensure your migrated report maintains data accuracy, 
        performance standards, and visual fidelity.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.deployment_complete:
        st.markdown('<div class="warning-alert">⚠️ Please complete the Deployment step before proceeding to Testing.</div>', unsafe_allow_html=True)
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
            
            # Prepare test configuration
            test_config = {
                'data_accuracy': test_data_accuracy,
                'calculations': test_calculations,
                'visuals': test_visuals,
                'performance': test_performance,
                'interactions': test_interactions,
                'accessibility': test_accessibility
            }
            
            with st.spinner("Running test suite..."):
                # Call the testing function
                result = testing_function(st.session_state.deployment_data, test_config)
            
            if result['success']:
                # Store testing data
                st.session_state.testing_data = result['data']
                st.session_state.testing_complete = True
                
                st.markdown(f'<div class="success-alert">✅ {result["message"]}</div>', unsafe_allow_html=True)
                
                # Display test metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('accuracy', 0)}%</div>
                        <div class="metric-label">Data Accuracy</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('calculations_verified', 0)}/{result['data'].get('calculations_verified', 0)}</div>
                        <div class="metric-label">Calculations Verified</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('visuals_validated', 0)}/{result['data'].get('visuals_validated', 0)}</div>
                        <div class="metric-label">Visuals Validated</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('avg_query_time', 0)}s</div>
                        <div class="metric-label">Avg Query Time</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display test results table
                if 'test_results' in result['data']:
                    st.markdown("### 📊 Detailed Test Results")
                    
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
                    The Power BI report is now ready for production use. All tests have passed with 100% accuracy.
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
                # Testing failed
                st.markdown(f'<div class="error-alert">❌ {result["message"]}</div>', unsafe_allow_html=True)
                st.error("Please review the test configuration and try again.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 13px; padding: 2rem 0; margin-top: 3rem;">
    <strong>Visa BI Migration Platform</strong> • Enterprise Edition • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Documentation</a> • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Support</a> • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)