# AI-Generated Custom Cover Letter Application

## Overview

This repository contains the code and resources for an AI-powered application designed to generate custom cover letters for job applications. The application leverages Generative AI (Gen-AI) and Retrieval-Augmented Generation (RAG) techniques to produce personalized cover letters based on a user's resume and a specific job description.

### Key Features
- **Resume and Job Description Analysis**: The user uploads their resume and a job description they are interested in. The application analyzes these documents to understand the user's skills and the requirements of the job.
- **AI-Driven Cover Letter Generation**: Using state-of-the-art open-source Large Language Models (LLMs), the application generates a tailored cover letter highlighting the most relevant experiences and skills.
- **Email Integration**: The generated cover letter can be sent directly to the HR's email provided by the user, simplifying the job application process.
- **Customization and User Feedback**: Users can review, edit, and modify the generated content before sending it, ensuring a high level of customization.

### Technologies Used
- **Gen-AI & LLMs**: Freely available models for text generation, including **Llama3-70b-8192** for chat-based generation.
- **RAG Framework**: Retrieval-Augmented Generation for incorporating relevant details from the resume.
- **groq API**: Used for data retrieval and processing.
- **FAISS**: For efficient similarity search and indexing.
- **HuggingFace Embedding**: For embedding the resume and job descriptions for better context understanding.
- **RecursiveCharacterSplitter**: For handling long documents efficiently.
- **Streamlit**: For deployment and building a user-friendly web interface.
- **smtplib**: For sending the generated cover letter via email.
  
### Objective
The primary goal of this project is to streamline the job application process by automating the creation of high-quality, custom cover letters, enhancing the chances of a successful job application.

### Deployment
- The application is deployed on Streamlit for seamless interaction and real-time processing.
- You can access the deployed version of the application here:  
  **[Insert Deployment Link]**
