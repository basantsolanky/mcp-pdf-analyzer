from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import numpy as np
import os

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.documents = self._load_and_split_pdf()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.document_vectors = self.vectorizer.fit_transform(self.documents)
        
    def _load_and_split_pdf(self):
        """Load PDF and split into chunks."""
        documents = []
        
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page in pdf_reader.pages:
                text = page.extract_text()
                # Split text into chunks of roughly 1000 characters
                chunks = [text[i:i+1000] for i in range(0, len(text), 800)]  # 200 char overlap
                documents.extend(chunks)
        
        return documents
    
    def get_answer(self, question: str) -> str:
        """Get answer for a question about the PDF content."""
        # Transform question using the same vectorizer
        question_vector = self.vectorizer.transform([question])
        
        # Calculate similarities
        similarities = cosine_similarity(question_vector, self.document_vectors)[0]
        
        # Get top 3 most similar chunks
        top_indices = np.argsort(similarities)[-3:][::-1]
        
        if not any(similarities[top_indices] > 0.1):  # Similarity threshold
            return "I couldn't find any relevant information in the PDF to answer your question."
        
        # Combine the relevant text chunks
        relevant_chunks = [self.documents[i] for i in top_indices]
        context = "\n\n".join(relevant_chunks)
        
        return f"Based on the PDF content, here's what I found:\n\n{context}"

    def __del__(self):
        """Cleanup temporary files if needed."""
        try:
            if os.path.exists(self.pdf_path):
                os.remove(self.pdf_path)
        except:
            pass 