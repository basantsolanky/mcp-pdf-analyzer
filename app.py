import streamlit as st
import os
from pdf_processor import PDFProcessor
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="MCP PDF Assistant",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("📚 MCP PDF Assistant")
    st.write("Upload a PDF file and ask questions about its content!")

    # Initialize session state for PDF processor
    if 'pdf_processor' not in st.session_state:
        st.session_state.pdf_processor = None

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

    if uploaded_file:
        # Create a temporary file to save the uploaded PDF
        temp_dir = Path("temp")
        temp_dir.mkdir(exist_ok=True)
        temp_path = temp_dir / uploaded_file.name
        
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Initialize PDF processor if not already done
        if st.session_state.pdf_processor is None:
            with st.spinner("Processing PDF..."):
                st.session_state.pdf_processor = PDFProcessor(str(temp_path))
                st.success("PDF processed successfully!")

        # Question input
        question = st.text_input("Ask a question about the PDF:")
        
        if question:
            with st.spinner("Finding answer..."):
                answer = st.session_state.pdf_processor.get_answer(question)
                st.write("### Answer:")
                st.write(answer)

if __name__ == "__main__":
    main() 