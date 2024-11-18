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




def switch_to_guide():
    st.session_state.page = 'guide'

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
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

            generator = GroqCoverLetterGenerator(groq_api_key=os.getenv('GROQ_API_KEY'))
            # Create or load vector stores
            resume_store = generator.load_or_create_vector_store(
                resume_text, 
                "resume_store"
            )
            jd_store = generator.load_or_create_vector_store(
                job_description, 
                "jd_store"
            )
            cover_letter = generator.generate_cover_letter(resume_store=resume_store, jd_store=jd_store, hr_email=mail)

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

    def login_dialog():
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Submit"):
            st.session_state.email = email
            st.session_state.password = password
            st.session_state.logged_in = True
            st.success("Logged in successfully!", icon="✅")
            st.rerun()

    def send_mail():
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in to the email account
        server.login(st.session_state.email, st.session_state.password)

        def extract_content():
            body = st.session_state.content
            return body

        body = extract_content()
        # Send the email
        server.sendmail(st.session_state.email, mail, body)

        # Close the server
        server.quit()
        st.write("Email sent successfully!")

    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Show login dialog if not logged in
    if not st.session_state.logged_in:
        login_dialog()
    else:
        # Button to send the email
        if st.button("Confirm E-mail"):
            send_mail()
            st.write("Your Final E-mail:")
            st.write(st.session_state.content)
    if st.sidebar.button("Guide"):
        switch_to_guide()
elif st.session_state.page == 'guide':
    import guide
    guide.show_guide()
