import groq
from typing import Optional
import os

class GroqCoverLetterGenerator:
    def __init__(self, groq_api_key: str):
        """Initialize the Groq-based cover letter generator"""
        self.client = groq.Client(api_key=groq_api_key)
    
    def generate_cover_letter(self,
                            resume_text: str,
                            job_description: str,
                            hr_email: str) -> Optional[str]:
        """Generate cover letter using Groq's Llama 2 70B model"""
        try:
            # Create system and user messages
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
                    Create a professional cover letter based on the following:
                    
                    Resume:
                    {resume_text}
                    
                    Job Description:
                    {job_description}
                    
                    HR Email: {hr_email}
                    
                    Requirements:
                    1. Start with a compelling introduction
                    2. Match specific resume qualifications to job requirements
                    3. Use concrete examples from the resume
                    4. Keep professional tone
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
            
            # Extract generated cover letter
            cover_letter = completion.choices[0].message.content
            
            return cover_letter
            
        except Exception as e:
            print(f"Error generating cover letter: {str(e)}")
            return None
