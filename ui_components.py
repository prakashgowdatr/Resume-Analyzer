import streamlit as st
from resume_processor import ResumeProcessor

def setup_page_config():
    """Configure page settings and apply custom CSS styling"""
    st.set_page_config(page_title='Resume Analyzer AI', layout="wide")
    
    # Custom CSS styling
    st.markdown("""
    <style>
    .main-header { 
        text-align: center; 
        color: #2E86AB; 
        margin-bottom: 2rem; 
    }
    .analysis-box { 
        background-color: #f8f9fa; 
        padding: 1.5rem; 
        border-radius: 8px; 
        border-left: 4px solid #2E86AB; 
        color: #333333 !important;
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .analysis-box p, .analysis-box div, .analysis-box span {
        color: #333333 !important;
    }
    .section-header {
        color: #2E86AB;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown('<h1 class="main-header">🤖 Resume Analyzer AI</h1>', unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar with upload and processing controls"""
    st.markdown("### 📁 Setup")
    
    # File upload section
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=['pdf'])
    
    # API key input
    api_key = st.text_input(
        "OpenAI API Key", 
        type="password", 
        value=st.session_state.api_key or "",
        help="Enter your OpenAI API key to process the resume"
    )
    
    # Process resume button
    if st.button("🚀 Process Resume", type="primary"):
        handle_resume_processing(uploaded_file, api_key)
    
    # Analysis section
    st.markdown("### 🔍 Analysis Options")
    render_analysis_buttons()

def handle_resume_processing(uploaded_file, api_key):
    """Handle the resume processing workflow"""
    if not uploaded_file or not api_key:
        st.warning("Please upload a PDF and enter API key")
        return
    
    with st.spinner("Processing resume..."):
        # Initialize processor if not exists
        if st.session_state.processor is None:
            st.session_state.processor = ResumeProcessor()
        
        # Process the resume
        vector_store = st.session_state.processor.process_resume(uploaded_file, api_key)
        
        if vector_store:
            st.session_state.vector_store = vector_store
            st.session_state.api_key = api_key
            st.success("✅ Resume processed successfully!")
        else:
            st.error("Failed to process resume")

def render_analysis_buttons():
    """Render analysis option buttons"""
    if st.session_state.processor is None:
        st.session_state.processor = ResumeProcessor()
    
    analysis_options = st.session_state.processor.get_available_analyses()
    
    for label, analysis_type in analysis_options:
        if st.button(label, disabled=st.session_state.vector_store is None):
            handle_analysis_request(analysis_type, label)

def handle_analysis_request(analysis_type, label):
    """Handle analysis request and store results"""
    if not st.session_state.vector_store or not st.session_state.api_key:
        st.error("Please process a resume first")
        return
    
    with st.spinner(f"Generating {label.lower()}..."):
        analysis = st.session_state.processor.get_analysis(
            st.session_state.vector_store, 
            analysis_type, 
            st.session_state.api_key
        )
        if analysis:
            st.session_state[f'analysis_{analysis_type}'] = analysis

def render_main_content():
    """Render the main content area with analysis results"""
    st.markdown("### 📊 Analysis Results")
    
    if st.session_state.vector_store is None:
        render_welcome_message()
    else:
        render_analysis_results()

def render_welcome_message():
    """Render welcome message when no resume is processed"""
    st.info("👈 Upload your resume and enter API key to get started")
    
    # Instructions
    st.markdown("""
    **How to use:**
    1. Upload a PDF resume in the sidebar
    2. Enter your OpenAI API key
    3. Click "Process Resume" 
    4. Choose analysis options to get insights
    """)

def render_analysis_results():
    """Render all available analysis results"""
    analysis_types = [
        ("analysis_summary", "📋 Resume Summary"),
        ("analysis_strengths", "💪 Key Strengths"),
        ("analysis_improvements", "🔍 Areas for Improvement"),
        ("analysis_job_titles", "🎯 Suggested Job Titles")
    ]
    
    for key, title in analysis_types:
        if key in st.session_state:
            render_analysis_section(key, title)

def render_analysis_section(key, title):
    """Render individual analysis section with download option"""
    st.markdown(f"#### {title}")
    
    # Render analysis content in styled box
    with st.container():
        st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
        st.write(st.session_state[key])
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Download button
    st.download_button(
        f"📥 Download {title}",
        st.session_state[key],
        f"{title.lower().replace(' ', '_')}.txt",
        mime="text/plain"
    )
    st.markdown("---")