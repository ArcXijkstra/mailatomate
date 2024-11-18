import streamlit as st

# Title and Introduction
st.title("Application User Guide")
st.write("""
Welcome to the guide for using our application! This page will walk you through the features and how to use them effectively.
""")

# Section 1: What We Do
st.header("📄 What We Do")
st.write("""
We simplify the process of sending professional emails to HR representatives of companies by:
- Allowing you to upload your resume and input the job description.
- Helping you compose and send tailored emails quickly and efficiently.
- Ensuring a smooth, hassle-free communication channel with HR.
""")

# Section 2: How to Use the Application
st.header("🛠 How to Use")
with st.container():
    st.write("##### 1. **Upload Your Resume:**") 
    uploaded_file = st.file_uploader("Upload Your Resume", type=["docx", "pdf"], help="Supported formats: .docx, .pdf") 
    st.write("""As shown above similar section appears where we can drag and drop file here or click on `Browse files`.
                Supported formats are: `.docx`, `.pdf`.
                Maximum file size: 200MB. """)
    
with st.container():
    st.write("##### 2.  **Input Job Description:**") 
    st.write("""Similarly Copy-paste the job description text into the provided text box below: """)
    job_description = st.text_area("Paste the Job Description", placeholder="Enter the job description here...", height=150)

with st.container():
    st.write("##### 3.  **Enter HR's Email:**") 
    email_hr = st.text_input("Enter HR's Email", placeholder="hr@example.com")

with st.container():
    st.write("##### 4.  **Enter your Email:**") 
    email_user = st.text_input("Enter Your Email", placeholder="yourname@example.com")

with st.container():
    st.write("##### 5.  **App Password Generation:**") 
    app_password = st.text_input("App Password", placeholder="Generated password will appear here...")
    st.write("Your email will be used for app password generation once you click the `Generate` button below:")
    # Button to Generate App Password
    if st.button("Generate"):
        if email_user and email_hr and uploaded_file and job_description:
            # Simulate generating a password (example only, use secure methods in production)
            generated_password = "AppPass1234"
            st.success(f"App Password Generated: {generated_password}")
            # Display generated password in the disabled input
            st.text_input("App Password", value=generated_password, disabled=True)
        else:
            st.error("Please fill in all fields and upload your resume to generate a password.")
with st.container():
    st.write("##### 6.  **Generate Email:**") 
    st.write("When you click the `Generate Email` your professional email will be generated and ready to go.")
    st.button("Generate Email")

# Section 4: FAQs
st.header("❓ FAQs")

# FAQ 1 - Data Security
with st.expander("Is my data secure?"):
    st.write("""
    Yes, your data is processed securely and not shared with any third party. 
    We use industry-standard encryption and follow best practices to ensure your information stays private.
    """)

# FAQ 2 - File Upload Support
with st.expander("What types of files can I upload?"):
    st.write("""
    We support the following file formats for uploading your resume:
    - `.docx`
    - `.pdf`
    
    If you have any issues uploading your files, please contact support.
    """)

# FAQ 3 - Email Usage
with st.expander("How is my email used?"):
    st.write("""
    Your email is required for app-password generation and communication with HR. 
    We do not share your email with any third party, and it will only be used for application-related purposes.
    """)

# FAQ 4 - App Password Generation
with st.expander("How is my app password generated?"):
    st.write("""
    Your app password is generated based on your email, which is used to create a unique identifier. 
    It is a secure and temporary password that you can use for login purposes.
    """)

# FAQ 5 - Encountering Issues
with st.expander("What if I encounter issues?"):
    st.write("""
    If you encounter any issues, use the "Contact Us" section available at the bottom of this page.
    """)

# Section 5: Contact
st.header("📧 Contact Us")
st.write("""
For any questions or support, feel free to reach out to us at:
- **General Inquiries**: anmol.cd22@bmsce.ac.in
- **Technical Support**: bhishan.cd22@bmsce.ac.in
- **Feedback & Suggestions**: sagar.cd22@bmsce.ac.in
""")

st.write("Thank you for choosing our application!")


