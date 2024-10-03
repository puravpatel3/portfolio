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

    # Create a two-column layout: left for the image and buttons, right for Bio and Skills
    col1, col2 = st.columns([1, 2])

    # Left column: Profile picture and buttons (image loaded from GitHub repository)
    image_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg'
    with col1:
        st.image(image_url, width=300)  # Adjusted size of the picture

        # LinkedIn, Resume, and Contact buttons (aligned vertically)
        linkedin_url = "https://www.linkedin.com/in/puravp"
        resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Resume_Purav_Patel.pdf'

        st.markdown(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>', unsafe_allow_html=True)

        if st.button("Contact Me"):
            show_contact_form()

    # Right column: Bio and Skills
    with col2:
        # About Me description
        st.write("""
        ## Hi, I'm Purav!
        I'm an experienced data analytics professional with a passion for machine learning and AI. 
        As a Senior Business Intelligence Manager with 10+ years in analytics and supply chain leadership, 
        I leverage advanced analytics and lean methodologies to optimize operations, cut costs, and boost revenue. 
        I'm proficient in Python, SQL, Tableau, and other analytics tools, and I'm skilled at leading cross-functional 
        teams to drive process improvement through KPI dashboards and analytical views.
        """)

        # Skills section (in a 3-column format)
        st.write("### Skills:")
        skills = {
            "Leadership and Management": ["Strategic Growth", "Business Operations", "Analytical Skills"],
            "Programming and Data Analysis": ["Tableau", "SQL", "Python", "Anaconda", "Jupyter Notebook", "Celonis"],
            "Technical": ["AI", "Agile", "Smartsheet", "Rally", "Miro", "XMind", "Alteryx", "Microsoft Suite", "ERP", "BI"]
        }

        # Display skills in a 3-column format
        cols = st.columns(3)
        for i, (category, skillset) in enumerate(skills.items()):
            with cols[i]:
                st.write(f"**{category}**")
                for skill in skillset:
                    st.write(f"- {skill}")

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
