# 🤖 Resume Analyzer AI

A powerful Streamlit application that uses AI to analyze resumes and provide comprehensive insights. Upload a PDF resume and get detailed analysis including summaries, strengths, improvement suggestions, and job recommendations.

## ✨ Features

- **PDF Resume Upload**: Extract and process text from PDF resumes
- **AI-Powered Analysis**: Multiple analysis types using OpenAI's GPT models
- **Interactive Interface**: Clean, user-friendly Streamlit interface
- **Downloadable Results**: Export analysis results as text files
- **Modular Architecture**: Well-organized, maintainable codebase

## 🔍 Analysis Types

- **📋 Resume Summary**: Comprehensive overview of professional background
- **💪 Key Strengths**: Standout qualities and compelling aspects
- **🔍 Areas for Improvement**: Enhancement suggestions and recommendations
- **🎯 Suggested Job Titles**: Suitable career paths and positions

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenAI API key

### Installation

1. **Clone or download the files**
   ```bash
   # Ensure you have these 3 files:
   # - main.py
   # - resume_processor.py
   # - ui_components.py
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pypdf langchain langchain-openai langchain-community chromadb
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Upload Resume**: Click "Upload Resume (PDF)" and select your PDF file
2. **Enter API Key**: Input your OpenAI API key in the password field
3. **Process Resume**: Click "🚀 Process Resume" to extract and prepare the text
4. **Analyze**: Choose from the analysis options:
   - 📋 Summary
   - 💪 Strengths  
   - 🔍 Improvements
   - 🎯 Job Titles
5. **Download**: Save any analysis results as text files

## 🏗️ Project Structure

```
resume-analyzer/
├── main.py              # Main application entry point
├── resume_processor.py  # Resume processing and AI logic
├── ui_components.py     # User interface components
└── README.md           # This file
```

### File Descriptions

- **`main.py`**: Application entry point, session state management, and layout coordination
- **`resume_processor.py`**: Core business logic including PDF processing, vector store creation, and AI analysis
- **`ui_components.py`**: All UI components, styling, and user interaction handling

## 🔧 Configuration

### OpenAI API Key
- Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- Enter it in the sidebar when using the app
- Your key is only stored in the session and not persisted

### Customization
- **Add new analysis types**: Modify `analysis_prompts` in `ResumeProcessor` class
- **Change AI model**: Update `model_name` parameter in `get_analysis` method
- **Modify styling**: Edit CSS in `setup_page_config` function

## 🛠️ Technical Details

- **Framework**: Streamlit for web interface
- **AI/ML**: LangChain + OpenAI for text processing and analysis
- **PDF Processing**: PyPDF for text extraction
- **Vector Storage**: Chroma for document embeddings
- **Text Splitting**: Recursive character text splitter for optimal chunking

## 📝 Requirements

```
streamlit
pypdf
langchain
langchain-openai
langchain-community
chromadb
```

## 🚨 Important Notes

- **API Costs**: This app uses OpenAI's API which incurs costs per request
- **PDF Quality**: Text extraction quality depends on the PDF format
- **API Key Security**: Never commit API keys to version control
- **Internet Required**: Needs internet connection for OpenAI API calls

## 🤝 Contributing

Want to add new features? The modular structure makes it easy:

1. **New analysis types**: Add to `ResumeProcessor.analysis_prompts`
2. **UI improvements**: Modify `ui_components.py`
3. **New file formats**: Extend `ResumeProcessor` class
4. **Additional AI models**: Update the analysis methods

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🆘 Troubleshooting

**Common Issues:**
- **"Error reading PDF"**: Ensure PDF is not password-protected or corrupted
- **"Error creating vector store"**: Check your OpenAI API key is valid
- **"Failed to process resume"**: Verify internet connection and API key

**Need Help?**
- Check that all dependencies are installed correctly
- Ensure your OpenAI API key has sufficient credits
- Try with a different PDF file if processing fails

---

*Powered by LangChain & OpenAI | Process once, analyze multiple times*
