# MCP PDF Assistant

A simple web application that allows users to upload PDF files and ask questions about their content. The application uses LangChain and Streamlit to provide an interactive interface for PDF document analysis.

## Features

- PDF file upload
- Text extraction and processing
- Question answering based on PDF content
- Clean and intuitive web interface

## Setup

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:
```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Upload a PDF file using the file uploader
2. Wait for the PDF to be processed
3. Type your question in the text input field
4. View the answer based on the PDF content

## Technical Details

The application uses:
- Streamlit for the web interface
- LangChain for document processing
- FAISS for efficient similarity search
- HuggingFace embeddings for text processing
- PyPDF2 for PDF parsing

## Note

The application processes PDFs locally and does not store any data permanently. Uploaded files are temporarily stored during processing and automatically cleaned up when the session ends. 