import streamlit as st
import base64
import os
import sys
import smtplib
import yagmail


server_path = os.path.join(os.path.dirname(__file__), '..', 'server')
sys.path.append(server_path)


from input_processing import DocumentProcessor
from text_embedding_and_vector_storage import VectorStore
from cover_letter_generator import GroqCoverLetterGenerator

st.title("Generate E-mail with AI")


job_description = st.text_area("Job Description", key="jd", height=200)

mail = st.text_input("Mail to : ", key="mail",placeholder="Enter the mail to send the generated email")

resume = st.file_uploader("Upload Resume", type=["pdf"])

# Check if inputs are valid
if job_description == "":
    st.error("Please enter a job description")
elif resume is None or resume.type != "application/pdf":
    st.error("Please upload a PDF resume")
else:
    resume_bytes = resume.read()
    resume_base64 = base64.b64encode(resume_bytes).decode("utf-8")
    resume_url = f"data:application/pdf;base64,{resume_base64}"
    st.markdown(
        f'<iframe src="{resume_url}" width="700" height="800" type="application/pdf"></iframe>',
        unsafe_allow_html=True,
    )

    job_description_path = "data/job_description.txt"
    with open(job_description_path, "w") as f:
        f.write(job_description)

    # Save the uploaded PDF to a file
    resume_path = "data/resume.pdf"  
    with open(resume_path, "wb") as f:
        f.write(resume_bytes)

# Generate email content when button is clicked
if st.button("Generate E-mail"):
    # Ensure the resume is saved for processing
    if resume is not None:
        processor = DocumentProcessor()
        processor.process_documents(resume_path)

        vector_store = VectorStore()
        stores = vector_store.process_documents(
            "data/resume.txt",
            "data/job_description.txt"
        )
        with open("data/resume.txt", "r") as f:
            resume_text = f.read()
        cover_letter_generator = GroqCoverLetterGenerator(groq_api_key=os.getenv('GROQ_API_KEY'))
        cover_letter = cover_letter_generator.generate_cover_letter(resume_text, job_description, mail)

        # Save generated email in session state
        st.session_state.content = cover_letter

# Text area for displaying and modifying the email
def update_content():
    st.session_state.content = st.session_state.temp_content


st.text_area(
    "Generated E-mail",
    st.session_state.get("content", ""),  # Show the content in session state or empty if none
    height=300,
    key="temp_content",
    on_change=update_content,  # Update content on change
)

# Function to send the email
def send_mail():
    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    st.session_state.submit = False
    # Log in to the email account
    # @st.dialog("Enter your email and password to log in")
    # def login_dialog():
    #     email = st.text_input("Email")
    #     password = 'ommf wqxk vonr hlum'

    #     st.session_state.email = email
    #     st.session_state.password = password
    #     if st.button("Submit"):
    #         st.session_state.submit = True
    #         return True
        

    # if not st.session_state.submit:
    #     login_dialog()  
    st.session_state.email = 'testmyprojectagain@gmail.com'
    st.session_state.password = "ommf wqxk vonr hlum"
    server.login(st.session_state.email, st.session_state.password)

    def extract_content():
        body = st.session_state.content
        # last_idx = body.find("\n")
        # subject = body[:last_idx]
        # body = body[last_idx+1:]
        return body
    body = extract_content()
    # Send the email
    server.sendmail(st.session_state.email, mail, body)

    # Close the server
    server.quit()
    st.write("Email sent successfully!")

# Button to send the email
if st.button("Confirm E-mail", on_click=send_mail):
    st.write("Your Final E-mail:")
    st.write(st.session_state.content)
