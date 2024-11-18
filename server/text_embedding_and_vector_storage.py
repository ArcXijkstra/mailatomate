from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from typing import List, Dict, Optional

class VectorStore:
    def __init__(self, index_dir: str = "vector_indices"):
        """Initialize vector store with storage directory"""
        self.index_dir = index_dir
        os.makedirs(index_dir, exist_ok=True)
        
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
    
    def create_vector_store(self, 
                        texts: List[str], 
                        store_name: str) -> Optional[FAISS]:
        """Create vector store from texts"""
        try:
            # Split texts into chunks
            chunks = self.text_splitter.split_text("\n".join(texts))
            
            # Create vector store
            vector_store = FAISS.from_texts(
                texts=chunks,
                embedding=self.embeddings
            )
            
            # Save vector store
            vector_store.save_local(
                os.path.join(self.index_dir, store_name)
            )
            
            return vector_store
            
        except Exception as e:
            print(f"Error creating vector store: {str(e)}")
            return None
    
    def load_vector_store(self, store_name: str) -> Optional[FAISS]:
        """Load existing vector store"""
        try:
            return FAISS.load_local(
                os.path.join(self.index_dir, store_name),
                self.embeddings
            )
        except Exception as e:
            print(f"Error loading vector store: {str(e)}")
            return None
    
    def process_documents(self, 
                        resume_path: str, 
                        jd_path: str) -> Dict[str, FAISS]:
        """Process resume and job description into vector stores"""
        # Read files
        try:
            with open(resume_path, 'r', encoding='utf-8') as f:
                resume_text = f.read()
            with open(jd_path, 'r', encoding='utf-8') as f:
                jd_text = f.read()
        except Exception as e:
            print(f"Error reading files: {str(e)}")
            return {}
        
        # Create vector stores
        stores = {}
        stores['resume'] = self.create_vector_store(
            [resume_text], 
            'resume_store'
        )
        stores['jd'] = self.create_vector_store(
            [jd_text], 
            'jd_store'
        )
        
        return stores
