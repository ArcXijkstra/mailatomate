import streamlit as st

def show_guide():
    if st.sidebar.button("Home"):
        st.session_state.page = 'main'

    st.title("Application User Guide")
    st.write("""
    Welcome to the guide for using our application! This page will walk you through the features and how to use them effectively.
    """)

    st.header("📄 What We Do")
    st.write("""
    We simplify the process of sending professional emails to HR representatives of companies by:
    - Allowing you to upload your resume and input the job description.
    - Helping you compose and send tailored emails quickly and efficiently.
    - Ensuring a smooth, hassle-free communication channel with HR.
    """)

    # Section 2: How to Use the Application
    st.header("🛠 How to Use")
    st.write("""
    1. **Upload Your Resume**: Click on the "Browse files" button to upload your resume (in PDF format).
    2. **Input Job Description**: Enter the job description in the text area provided for analysis.
    3. **Enter HR's Email**: Provide the HR's email address for sending your resume.
    4. **Generate Your Email**: The app will generate an email with the job description and resume attached for you to send.
    
    But you need to enter the Google app password to access the generated mail, so get your app password beforehand.
    """)

    st.header("🔑 Create and Use App Password")
    st.write("""
    1. **Sign in to your Google Account**:
    - Go to [Google Account](https://myaccount.google.com).
    - Sign in with your Google credentials (email and password).

    2. **Go to Security Settings**:a
    - On the left-hand side, click on **Security**.

    3. **Enable 2-Step Verification (if not already enabled)**:
    - Scroll down to the "Signing in to Google" section.
    - If **2-Step Verification** is not enabled, click on it and follow the steps to set it up.

    4. **Generate App Password**:
    - Under the "Signing in to Google" section, find **App passwords**.
    - Click on **App passwords** (you may be prompted to enter your password again).

    5. **Set the App**:
    - To create a new app specific password, type a app name for it.

    6. **Generate the Password**:
    - Click on **Generate**.
    - A 16-character app password will appear.

    7. **Use the App Password**:
    - Copy the generated app password.
    - Paste this password into the main application page to retrieve the generated mail.

    8. **Finish**:
    - Once you've entered the app password, you should be able to access the app or service.

    For further understanding, you can visit [Google's official guide on App passwords](https://support.google.com/accounts/answer/185833?hl=en).
    """)

    # Section 5: Contact
    st.header("📧 Contact Us")
    st.write("""
    For any questions or support, feel free to reach out to us at:
    - **General Inquiries**: anmolbhusal1804@gmail.com
    - **Technical Support**: bhishan.cd22@bmsce.ac.in
    - **Feedback & Suggestions**: sagar.cd22@bmsce.ac.in
    """)

    st.write("Thank you for choosing our application!")

