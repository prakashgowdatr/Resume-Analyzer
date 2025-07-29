import pypdf
import tempfile
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

class ResumeProcessor:
    """Handles all resume processing operations"""
    
    def __init__(self):
        self.analysis_prompts = {
            "summary": "Provide a comprehensive summary of this resume including professional background, key skills, experience, and overall assessment.",
            "strengths": "Analyze the key strengths and standout qualities in this resume. What makes this candidate compelling?",
            "improvements": "Identify areas for improvement in this resume. What could be enhanced or added?",
            "job_titles": "Based on this resume, suggest suitable job titles and career paths for this candidate."
        }
    
    def extract_pdf_text(self, pdf_file):
        """Extract text from uploaded PDF file"""
        try:
            pdf_reader = pypdf.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text if text.strip() else None
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
            return None
    
    def create_vector_store(self, text, api_key):
        """Create vector store from extracted text"""
        try:
            # Split text into manageable chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, 
                chunk_overlap=200
            )
            chunks = splitter.split_text(text)
            
            # Create embeddings and vector store
            embeddings = OpenAIEmbeddings(openai_api_key=api_key)
            temp_dir = tempfile.mkdtemp()
            vector_store = Chroma.from_texts(
                chunks, 
                embeddings, 
                persist_directory=temp_dir
            )
            return vector_store
        except Exception as e:
            st.error(f"Error creating vector store: {str(e)}")
            return None
    
    def get_analysis(self, vector_store, analysis_type, api_key):
        """Generate AI analysis based on type"""
        if analysis_type not in self.analysis_prompts:
            st.error(f"Unknown analysis type: {analysis_type}")
            return None
        
        try:
            # Initialize ChatOpenAI with the provided API key
            llm = ChatOpenAI(
                openai_api_key=api_key, 
                model_name="gpt-3.5-turbo", 
                temperature=0.3
            )
            
            # Create retrieval QA chain
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
                return_source_documents=False
            )
            
            # Get response for the specific analysis type
            response = qa_chain.invoke({
                "query": self.analysis_prompts[analysis_type]
            })
            return response["result"]
        except Exception as e:
            st.error(f"Error getting analysis: {str(e)}")
            return None
    
    def process_resume(self, uploaded_file, api_key):
        """Main method to process uploaded resume"""
        if not uploaded_file or not api_key:
            return None
        
        # Extract text from PDF
        text = self.extract_pdf_text(uploaded_file)
        if not text:
            st.error("Could not extract text from PDF")
            return None
        
        # Create vector store
        vector_store = self.create_vector_store(text, api_key)
        if not vector_store:
            st.error("Failed to create vector store")
            return None
        
        return vector_store
    
    def get_available_analyses(self):
        """Return list of available analysis types"""
        return [
            ("📋 Summary", "summary"),
            ("💪 Strengths", "strengths"), 
            ("🔍 Improvements", "improvements"),
            ("🎯 Job Titles", "job_titles")
        ]