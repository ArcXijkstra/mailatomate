import os
import pdfplumber

class DocumentProcessor:
    def __init__(self):
        # Create the 'data' directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')
        
    def parse_pdf_with_pdfplumber(self, pdf_path: str) -> str:
        """Extract text from PDF using pdfplumber"""
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    
    def save_text_to_file(self, text: str, file_name: str) -> None:
        """Save extracted text to a file in the 'data' directory"""
        try:
            with open(f"data/{file_name}.txt", 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Text successfully saved to 'data/{file_name}.txt'")
        except Exception as e:
            print(f"Error saving the file: {e}")

    def process_documents(self, resume_path: str) -> None:
        """Process the resume and save the extracted text to a file"""
        resume_text = ""
        
        if resume_path.endswith('.pdf'):
            resume_text = self.parse_pdf_with_pdfplumber(resume_path)
        else:
            raise ("Unsupported file type. Please use PDF files.")
        
        # Extract the base name of the file without the extension
        file_name = os.path.splitext(os.path.basename(resume_path))[0]
        
        # Save the extracted text to a file in 'data' directory
        self.save_text_to_file(resume_text, file_name)
        print(f"Text from {resume_path} has been saved as 'data/{file_name}.txt'")

