import streamlit as st
from ui_components import setup_page_config, render_sidebar, render_main_content
from resume_processor import ResumeProcessor
import warnings

warnings.filterwarnings('ignore')

def main():
    """Main application entry point"""
    # Setup page configuration and styling
    setup_page_config()
    
    # Initialize session state
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    if 'processor' not in st.session_state:
        st.session_state.processor = None
    
    # Create main layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        render_sidebar()
    
    with col2:
        render_main_content()
    
    # Footer
    st.markdown("---")
    st.markdown("*Powered by LangChain & OpenAI | Process once, analyze multiple times*")

if __name__ == "__main__":
    main()