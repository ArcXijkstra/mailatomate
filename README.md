# AI-Generated Custom Cover Letter Application with RAG Framework and Streamlit
This project focuses on building an intelligent system that automates the creation of custom cover letters for job applications. By analyzing a user's resume and a job description, the application leverages advanced AI techniques to generate tailored cover letters, streamlining the application process.

## Main Objectives
- **Analyze Resumes and Job Descriptions**: Extract and understand relevant details from both inputs.
- **Generate Tailored Cover Letters**: Use state-of-the-art LLMs to produce personalized cover letters.
- **Email Integration**: Simplify the job application process by sending the generated cover letter directly to the HR's email address.
- **Deploy for Ease of Use**: Provide a user-friendly interface for real-time interaction via Streamlit.

## Key Functionalities
- **Resume and Job Description Analysis**: Process and understand user-uploaded files.
- **Custom Cover Letter Generation**: Generate high-quality, role-specific cover letters using the RAG framework and Llama3-70b-8192 model.
- **Email Integration**: Send cover letters directly to the provided HR email address using SMTP.
- **Interactive Web Application**: Streamlit deployment for seamless interaction with users.
- **Usage Guide**: A dedicated guide page to help users understand and navigate the application.

## Overview
The project is organized into two main folders:

### 1. **Client**
   - **app.py**: Hosts the main Streamlit web application for user interaction.
   - **guide.py**: Provides a Streamlit page with instructions on how to use the application.

### 2. **Server**
   - **cover_letter_generator.py**: Combines information from the resume and job description to generate a customized cover letter.
   - **input_processing.py**: Handles the parsing and preprocessing of resume and job description inputs.
   - **text_embedding_and_vector_store.py**: Implements the RAG framework, including text embeddings and FAISS vector storage for document similarity and retrieval.

### Requirements
The `requirements.txt` file includes all necessary dependencies for both the client and server components, ensuring smooth setup and execution.

## Features
- Analyze resumes and job descriptions for key information.
- Generate personalized cover letters based on the input data.
- Send the generated cover letters via email directly to HR.
- Host an intuitive web interface with usage instructions.

## Technologies Used
- **Embeddings**: HuggingFace Transformers and FAISS for similarity search.
- **LLM**: Llama3-70b-8192 for high-quality text generation.
- **RAG Framework**: Retrieval-Augmented Generation for context-aware content generation.
- **Deployment**: Streamlit for web-based interaction.
- **Text Processing**: RecursiveCharacterSplitter for handling lengthy documents.
- **Email Service**: SMTP for sending emails.

## Installation
Follow these steps to set up the project on your local machine.

### Prerequisites
- **Python Version**: Ensure you have Python 3.8 or higher installed.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Med-Time/Gen-email.git
   cd Gen-email
   ```

2. Install dependencies:
   Use the provided `requirements.txt` file to install all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   To launch the main application:
   ```bash
   streamlit run client/app.py
   ```

   To access the usage guide:
   ```bash
   streamlit run client/guide.py
   ```

## Deployment
You can access the deployed version of the application here:  
**https://genmail.streamlit.app**

## Contributors
- **Anmol**  
- **Bhishan**  
- **Sagar**

## Acknowledgements
- Thanks to HuggingFace for providing powerful models and embeddings.
- Special thanks to Groq API, FAISS, and LangChain for their tools and libraries that made this project possible.
