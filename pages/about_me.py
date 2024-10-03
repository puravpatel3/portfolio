import streamlit as st
import smtplib  # For SMTP (Gmail)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to show the About Me page content
def show_about_me():
    # Remove the default Streamlit menu and footer (NOT the sidebar)
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} /* Hide the header */
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Create a two-column layout: left for the image,

    # Right column: Bio, Certifications, LinkedIn, and Resume Download
    col1, col2 = st.columns([1, 2])

    # Left column: Profile picture
    with col1:
        st.image(r"C:\Users\212068332.HCAD\OneDrive - GEHealthCare\Pictures\Anny Scrapbook\SuShi_Wedding.jpg", width=200)

    # Right column: Bio and Certifications
    with col2:
        st.write("""
        ## Hi, I'm Purav!
        
        I'm an experienced data analytics professional with a passion for machine learning and AI. 
        My goal is to land an Analytics Director role and leverage my technical and leadership skills 
        to drive business insights and innovations.
        """)

        # Certifications
        st.write("### Certifications:")
        st.write("- Certified AI Specialist")
        st.write("- Machine Learning Expert (sklearn, TensorFlow)")
        st.write("- Tableau Expert")

    # Buttons for LinkedIn, Resume, and Contact
    linkedin_url = "https://www.linkedin.com/in/puravp"
    resume_file = r"C:\Users\212068332.HCAD\Box\z_My Folder\2-Resume\1 - Resume - Purav\Resume_Purav Patel.pdf"

    col_linkedin, col_resume, col_contact = st.columns([1, 1, 1])

    # LinkedIn button
    with col_linkedin:
        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>',
                 unsafe_allow_html=True)

    # Resume download button
    with col_resume:
        with open(resume_file, "rb") as file:
            st.download_button(label="Download My Resume", data=file, file_name="Purav_Resume.pdf", mime="application/pdf")

    # Contact Me button
    with col_contact:
        if st.button("Contact Me"):
            show_contact_form()

# Function to show the contact form
def show_contact_form():
    st.write("### Contact Me")

    # Create a form with text inputs for Name, Email, and Message
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")  # New email field
        message = st.text_area("Message")

        # Create Send and Cancel buttons (side by side)
        send_button = st.form_submit_button(label="Send")
        cancel_button = st.form_submit_button(label="Cancel")

        if send_button:
            if name and email and message:  # Ensure all fields are filled out
                send_email(name, email, message)
                st.success(f"Message sent by {name}!")
            else:
                st.error("Please fill out all fields before sending.")
        elif cancel_button:
            st.write("Message canceled.")

# Function to send an email using SMTP (Gmail)
def send_email(name, email, message):
    sender_email = "your-email@gmail.com"  # Update this to your Gmail account
    receiver_email = "patel.a.purav@gmail.com"  # Your email address to receive messages
    password = "your-gmail-password"  # Update with your Gmail app password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"New Contact Form Submission from {name}"

    # Email body
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Send the email via Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
        st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"Failed to send message: {e}")

# Call the function directly
show_about_me()
