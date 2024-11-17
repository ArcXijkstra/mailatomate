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
                    that match candidate qualifications with job requirements."""
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
                    7. Keep length between 250-400 words
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

# Example usage
if __name__ == "__main__":
    # Initialize generator
    generator = GroqCoverLetterGenerator(
        groq_api_key=os.getenv('GROQ_API_KEY')
    )
    
    # Read resume and job description
    with open('data/resume_with_image.txt', 'r') as f:
        resume_text = f.read()
    with open('data/job_description.txt', 'r') as f:
        job_description = f.read()
    
    # Generate cover letter
    cover_letter = generator.generate_cover_letter(
        resume_text=resume_text,
        job_description=job_description,
        hr_email="hr@company.com"
    )
    
    if cover_letter:
        print("Generated Cover Letter:")
        print("=" * 50)
        print(cover_letter) 