import streamlit as st
import base64

st.title("Generate E-mail with AI")

# Input for Job Description
job_description = st.text_input("Job Description", key="jd")

# Upload Resume
resume = st.file_uploader("Upload Resume", type=["pdf"])

# Check if inputs are valid
if job_description == "":
    st.error("Please enter a job description")
elif resume is None or resume.type != "application/pdf":
    st.error("Please upload a PDF resume")
else:
    # Show the uploaded resume
    resume_bytes = resume.read()
    resume_base64 = base64.b64encode(resume_bytes).decode("utf-8")
    resume_url = f"data:application/pdf;base64,{resume_base64}"
    st.markdown(
        f'<iframe src="{resume_url}" width="700" height="800" type="application/pdf"></iframe>',
        unsafe_allow_html=True,
    )

# Generate email content when button is clicked
if st.button("Generate E-mail"):
    generated_email = f"""Hello, I am writing to express my interest in the {job_description} position at your company. 
        I am confident that my skills and experience make me a great fit for this role. I have a strong background in 
        {job_description} and have worked on similar projects in the past. I am excited about the opportunity to 
        work with your team and contribute to the success of your company. Thank you for considering my application.
        I look forward to hearing from you soon. Best regards, Your Name"""
    
    # Save generated email in session state if it's not already there
    if "content" not in st.session_state:
        st.session_state.content = generated_email

def update_content():
    st.session_state.content = st.session_state.temp_content

st.text_area(
    "Generated E-mail",
    st.session_state.get("content", ""),  # Show the content in session state or empty if none
    height=200,
    key="temp_content",
    on_change=update_content,  # Update content on change
)

if st.button("Confirm E-mail"):
    st.write("Your Final E-mail:")
    st.write(st.session_state.content)
