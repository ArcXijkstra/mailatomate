import groq
from typing import Optional, Dict
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os

class GroqCoverLetterGenerator:
    def __init__(self, groq_api_key: str):
        """Initialize the Groq-based cover letter generator"""
        self.client = groq.Client(api_key=groq_api_key)
        self.vector_store_path = vector_store_path
        
        # Initialize embeddings model
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def load_or_create_vector_store(self, 
                                text: str, 
                                store_name: str) -> FAISS:
        """
        Load existing vector store or create new one if it doesn't exist
        """
        store_path = os.path.join(self.vector_store_path, store_name)
        # Try to load existing vector store
        if os.path.exists(store_path):
            try:
                return FAISS.load_local(store_path, self.embeddings, allow_dangerous_deserialization=True)
            except Exception as e:
                print(f"Error loading vector store: {e}")
                # If loading fails, we'll create a new one
        
        # Create new vector store
        chunks = self.text_splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]
        vector_store = FAISS.from_documents(documents, self.embeddings)
        
        # Save vector store
        os.makedirs(self.vector_store_path, exist_ok=True)
        vector_store.save_local(store_path)
        
        return vector_store
    
    def get_relevant_context(self, 
                        vector_store: FAISS, 
                        query: str,
                        k: int = 3) -> str:
        """
        Get relevant context from vector store using similarity search
        """
        documents = vector_store.similarity_search(query, k=k)
        return "\n".join([doc.page_content for doc in documents])
    
    def extract_key_information(self, 
                            resume_store: FAISS, 
                            jd_store: FAISS) -> Dict[str, str]:
        """
        Extract relevant information from both resume and job description
        using vector stores
        """
        queries = {
            "technical_skills": "What are the candidate's technical skills, programming languages, and tools?",
            "soft_skills": "What are the candidate's soft skills, leadership abilities, and interpersonal skills?",
            "experience": "What are the candidate's most relevant work experiences, projects, and achievements?",
            "education": "What is the candidate's educational background, degrees, and certifications?",
            "job_requirements": "What are the key technical requirements and qualifications for this position?",
            "job_responsibilities": "What are the main responsibilities and duties of this role?"
        }
        
        info = {}
        
        # Extract from resume
        for key in ['technical_skills', 'soft_skills', 'experience', 'education']:
            info[key] = self.get_relevant_context(resume_store, queries[key])
        
        # Extract from job description
        for key in ['job_requirements', 'job_responsibilities']:
            info[key] = self.get_relevant_context(jd_store, queries[key])
        
        return info
    
    def generate_cover_letter(self,
                            resume_store: FAISS,
                            jd_store: FAISS,
                            hr_email: str) -> Optional[str]:
        """
        Generate cover letter using existing vector stores
        """
        try:
            # Extract relevant information using vector stores
            info = self.extract_key_information(resume_store, jd_store)
            
            # Create detailed prompt with extracted information
            messages = [
                {
                    "role": "system",
                    "content": """You are a professional cover letter writer. 
                    Your task is to create compelling, personalized cover letters 
                    that match candidate qualifications with job requirements.
                    Don't write any exatra information, just start from subject. Don't need to write lines like "Here is a professional cover letter tailored to the job description and the candidate's resume:" or "Here is a professional cover letter:
" etc."""
                },
                {
                    "role": "user",
                    "content": f"""
                    Create a professional cover letter based on the following matched information:
                    
                    Technical Skills:
                    {info['technical_skills']}
                    
                    Soft Skills:
                    {info['soft_skills']}
                    
                    Relevant Experience:
                    {info['experience']}
                    
                    Education:
                    {info['education']}
                    
                    Job Requirements:
                    {info['job_requirements']}
                    
                    Job Responsibilities:
                    {info['job_responsibilities']}
                    
                    HR Email: {hr_email}
                    
                    Requirements:
                    1. Start with a compelling introduction showing understanding of the role
                    2. Match specific skills and experiences to job requirements
                    3. Use concrete examples from the experience section
                    4. Maintain professional tone while showing enthusiasm
                    5. Format as proper email with subject line
                    6. Include strong call to action
                    7. Keep length between 250-300 words
                    8. End with professional closing
                    9. Use proper grammar and punctuation

                    """
                }
            ]
            
            # Generate completion using Groq
            completion = self.client.chat.completions.create(
                messages=messages,
                model="llama3-70b-8192",
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
                stream=False
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            print(f"Error generating cover letter: {str(e)}")
            return None
