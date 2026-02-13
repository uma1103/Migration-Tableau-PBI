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


def deployment_function(migration_data):
    """
    Dummy deployment function - Replace with your actual implementation
    
    This function generates a development guide document based on the Tableau dashboard
    that users can use to manually develop the Power BI dashboard.
    
    Args:
        migration_data (dict): Data from migration step containing Tableau analysis
    
    Returns:
        dict: {
            'success': bool,
            'message': str,
            'data': dict with deployment guide details
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
        
        # Generate development guide
        workspace_name = migration_data.get('workspace', 'Unknown')
        report_name = migration_data.get('report_name', 'Unknown')
        
        # Create development guide content
        guide_content = f"""POWER BI DEVELOPMENT GUIDE
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Report: {report_name}
Workspace: {workspace_name}

1. DATA SOURCES ({migration_data.get('data_sources', 0)} connections)
   - Follow connection strings from migration analysis
   - Configure data refresh schedules
   
2. CALCULATED FIELDS ({migration_data.get('calculated_fields', 0)} fields)
   - DAX formulas provided in detailed mapping
   - Parameter configurations included
   
3. VISUALIZATIONS ({migration_data.get('dashboards', 0)} dashboards)
   - Layout specifications attached
   - Visual types and configurations mapped
   
4. FORMATTING GUIDELINES
   - Color schemes and branding
   - Font specifications
   - Layout dimensions

Please refer to the detailed spreadsheet for complete specifications.
"""
        
        # Return success with deployment guide
        return {
            'success': True,
            'message': 'Development guide generated successfully',
            'data': {
                'workspace': workspace_name,
                'report_name': report_name,
                'guide_content': guide_content,
                'generation_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': 'Ready for Development',
                'components': migration_data.get('components', [])
            }
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Guide generation failed: {str(e)}',
            'data': {}
        }


def testing_function(deployment_data, test_config):
    """
    Dummy testing function - Replace with your actual implementation
    
    Performs validation tests on the manually developed Power BI dashboard:
    - Data Validation: Verify data accuracy and completeness
    - Visual Validation: Check visual types and configurations
    - Layout Comparison: Compare layout with Tableau original
    - Color/Font Comparison: Verify branding consistency
    
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
        
        if test_config.get('data_validation', False):
            test_results.append({
                'category': 'Data Validation',
                'tests_run': 85,
                'passed': 85,
                'failed': 0,
                'status': 'Passed',
                'details': 'Row counts, column types, aggregations verified'
            })
        
        if test_config.get('visual_validation', False):
            test_results.append({
                'category': 'Visual Validation',
                'tests_run': 42,
                'passed': 42,
                'failed': 0,
                'status': 'Passed',
                'details': 'Chart types, legends, axes configurations matched'
            })
        
        if test_config.get('layout_comparison', False):
            test_results.append({
                'category': 'Layout Comparison',
                'tests_run': 28,
                'passed': 28,
                'failed': 0,
                'status': 'Passed',
                'details': 'Dashboard structure, visual placement, sizing verified'
            })
        
        if test_config.get('color_font_comparison', False):
            test_results.append({
                'category': 'Color/Font Comparison',
                'tests_run': 36,
                'passed': 36,
                'failed': 0,
                'status': 'Passed',
                'details': 'Color schemes, fonts, branding elements matched'
            })
        
        # Calculate totals
        total_tests = sum(r['tests_run'] for r in test_results)
        total_passed = sum(r['passed'] for r in test_results)
        total_failed = sum(r['failed'] for r in test_results)
        
        # Calculate accuracy percentage
        accuracy = 100 if total_tests > 0 else 0
        
        # Return success with test data
        return {
            'success': True,
            'message': 'All validation tests passed successfully',
            'data': {
                'test_results': test_results,
                'total_tests': total_tests,
                'total_passed': total_passed,
                'total_failed': total_failed,
                'accuracy': accuracy,
                'data_match_score': 100,
                'visual_match_score': 100,
                'layout_match_score': 100,
                'branding_match_score': 100
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
step2_icon = "✓" if st.session_state.deployment_complete else "📄"
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
        <div class="progress-label">Dev Guide</div>
    </div>
    <div class="{step3_class}">
        <div class="progress-circle">{step3_icon}</div>
        <div class="progress-label">Validation</div>
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
    if st.button("📍 Dev Guide", key="nav2", disabled=not st.session_state.migration_complete, use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()

with col3:
    if st.button("📍 Validation", key="nav3", disabled=not st.session_state.deployment_complete, use_container_width=True):
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
    <div class="step-title">🚀 Development Guide Generation</div>
    <div class="step-description">
        Generate a comprehensive development guide based on your Tableau dashboard analysis. 
        This document will help you manually develop the Power BI dashboard with all necessary specifications.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.migration_complete:
        st.markdown('<div class="warning-alert">⚠️ Please complete the Migration step before proceeding to Development Guide.</div>', unsafe_allow_html=True)
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
        
        # Information about the development guide
        st.markdown("""
        <div class="info-box">
            <strong>📝 Development Guide:</strong> This guide contains detailed specifications for developing 
            the Power BI dashboard including data connections, DAX formulas, visual configurations, layout specifications, 
            and branding guidelines. Use this document as a reference to manually build your Power BI dashboard.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-alert">
            <strong>⚠️ Note:</strong> Automatic deployment is currently in progress and will be available in future releases. 
            For now, please use the downloadable development guide to manually create your Power BI dashboard.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("📄 Generate Development Guide", key="start_deploy", use_container_width=True):
            
            with st.spinner("Generating development guide..."):
                # Call the deployment function (now generates guide)
                result = deployment_function(st.session_state.migration_data)
            
            if result['success']:
                # Store deployment data for next step
                st.session_state.deployment_data = result['data']
                st.session_state.deployment_complete = True
                
                st.markdown(f'<div class="success-alert">✅ {result["message"]}</div>', unsafe_allow_html=True)
                
                # Display guide details
                st.markdown("### 📊 Development Guide Details")
                st.markdown(f"**Report Name:** {result['data'].get('report_name', 'N/A')}")
                st.markdown(f"**Workspace:** {result['data'].get('workspace', 'N/A')}")
                st.markdown(f"**Generated:** {result['data'].get('generation_time', 'N/A')}")
                st.markdown(f"**Status:** 🟢 {result['data'].get('status', 'Unknown')}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Display component mapping
                if 'components' in result['data'] and result['data']['components']:
                    st.markdown("### 📋 Component Mapping")
                    components_df = pd.DataFrame(result['data']['components'])
                    components_df.columns = ['Component', 'Original Count', 'Migrated', 'Status']
                    components_df['Status'] = '✅ ' + components_df['Status']
                    st.dataframe(components_df, use_container_width=True, hide_index=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Download button for development guide
                guide_content = result['data'].get('guide_content', 'Development guide content')
                st.download_button(
                    label="📥 Download Development Guide (TXT)",
                    data=guide_content,
                    file_name=f"PowerBI_Development_Guide_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
                # Create and download Excel specification
                if 'components' in result['data'] and result['data']['components']:
                    components_df = pd.DataFrame(result['data']['components'])
                    excel_buffer = pd.ExcelWriter('temp.xlsx', engine='xlsxwriter')
                    components_df.to_excel(excel_buffer, sheet_name='Components', index=False)
                    excel_buffer.close()
                    
                    with open('temp.xlsx', 'rb') as f:
                        excel_data = f.read()
                    
                    st.download_button(
                        label="📥 Download Detailed Specifications (Excel)",
                        data=excel_data,
                        file_name=f"PowerBI_Specifications_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                
                st.markdown("""
                <div class="info-box">
                    <strong>📊 Next Steps:</strong><br>
                    1. Download the development guide and specifications<br>
                    2. Use the documents to manually develop your Power BI dashboard<br>
                    3. Once development is complete, proceed to Testing for validation
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Continue to Validation →", key="goto_test", use_container_width=True):
                    st.session_state.current_step = 3
                    st.rerun()
            
            else:
                # Guide generation failed
                st.markdown(f'<div class="error-alert">❌ {result["message"]}</div>', unsafe_allow_html=True)
                st.error("Please check the migration data and try again.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STEP 3: TESTING
# =========================================================

elif st.session_state.current_step == 3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-title">🧪 Dashboard Validation & Comparison</div>
    <div class="step-description">
        Validate your manually developed Power BI dashboard against the original Tableau dashboard. 
        Run comprehensive tests to ensure data accuracy, visual fidelity, layout consistency, and branding compliance.
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.deployment_complete:
        st.markdown('<div class="warning-alert">⚠️ Please complete the Development Guide step before proceeding to Testing.</div>', unsafe_allow_html=True)
    else:
        st.markdown("### 🔧 Validation Configuration")
        
        st.markdown("""
        <div class="info-box">
            <strong>💡 About Validation:</strong> These tests compare your developed Power BI dashboard 
            against the original Tableau dashboard to ensure accurate migration and maintain consistency 
            in data, visuals, layout, and branding.
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            test_data_validation = st.checkbox("Data Validation", value=True, 
                help="Verify row counts, column types, data accuracy, and aggregation calculations")
            test_visual_validation = st.checkbox("Visual Validation", value=True,
                help="Check chart types, legends, axes, tooltips, and visual configurations")
        with col2:
            test_layout_comparison = st.checkbox("Layout Comparison", value=True,
                help="Compare dashboard structure, visual placement, sizing, and alignment")
            test_color_font_comparison = st.checkbox("Color/Font Comparison", value=True,
                help="Verify color schemes, fonts, branding elements, and styling")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🧪 Run Validation Suite", key="start_test", use_container_width=True):
            
            # Prepare test configuration
            test_config = {
                'data_validation': test_data_validation,
                'visual_validation': test_visual_validation,
                'layout_comparison': test_layout_comparison,
                'color_font_comparison': test_color_font_comparison
            }
            
            with st.spinner("Running validation tests..."):
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
                        <div class="metric-value">{result['data'].get('data_match_score', 0)}%</div>
                        <div class="metric-label">Data Match</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('visual_match_score', 0)}%</div>
                        <div class="metric-label">Visual Match</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('layout_match_score', 0)}%</div>
                        <div class="metric-label">Layout Match</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{result['data'].get('branding_match_score', 0)}%</div>
                        <div class="metric-label">Branding Match</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Display test results table
                if 'test_results' in result['data'] and result['data']['test_results']:
                    st.markdown("### 📊 Detailed Validation Results")
                    
                    test_df = pd.DataFrame(result['data']['test_results'])
                    test_df.columns = ['Test Category', 'Tests Run', 'Passed', 'Failed', 'Status', 'Details']
                    test_df['Status'] = '✅ ' + test_df['Status']
                    
                    st.dataframe(test_df, use_container_width=True, hide_index=True)
                    
                    # Summary stats
                    st.markdown("<br>", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Tests", result['data'].get('total_tests', 0))
                    with col2:
                        st.metric("Tests Passed", result['data'].get('total_passed', 0), 
                                delta=f"{result['data'].get('accuracy', 0)}%")
                    with col3:
                        st.metric("Tests Failed", result['data'].get('total_failed', 0))
                    
                    csv = test_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Validation Report",
                        data=csv,
                        file_name=f"Validation_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                
                st.markdown("""
                <div class="info-box">
                    <strong>🎉 Validation Complete!</strong><br>
                    Your Power BI dashboard has been validated against the original Tableau dashboard. 
                    All validation tests have passed, confirming that data accuracy, visual configurations, 
                    layout structure, and branding elements match the original specifications.
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
# FOOTER new
# =========================================================

st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 13px; padding: 2rem 0; margin-top: 3rem;">
    <strong>Visa BI Migration Platform</strong> • Enterprise Edition • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Documentation</a> • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Support</a> • 
    <a href="#" style="color: #1A1F71; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)