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

    # Create a two-column layout: left for the image, right for text and buttons
    col1, col2 = st.columns([1, 2])

    # Left column: Profile pictures (images loaded from GitHub repository)
    image1_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg'
    image2_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Wedding_Reception.jpg'
    
    with col1:
        st.image(image1_url, width=250)
        st.image(image2_url, width=250)

    # Right column: Bio and buttons
    with col2:
        st.write("""
        ## Hi, I'm Purav!

        I'm an experienced data analytics professional with a passion for machine learning and AI. My goal is to leverage my technical and leadership skills to drive business insights and innovations. With over 10 years of experience in analytics and supply chain leadership, I excel in optimizing operations, cutting costs, and boosting revenue.

        I built this web app to offer a deeper look into my expertise, showcase the projects I’ve worked on, and connect with other professionals who share similar passions. You’ll find a summary of my professional journey below, and more detailed insights about my roles and projects in the subpages.
        """)

        # Professional Summary
        st.write("""
        ### Senior Order Fulfillment Analytics Manager
        Location: Detroit, United States  
        Time Worked: Jul '21 — Present  

        ### Order Execution & Logistics Analytics Manager
        Location: New York, United States  
        Time Worked: Jan '19 — Jun '21  

        ### Logistics Analytics Product Owner
        Location: Hoboken, United States  
        Time Worked: Oct '16 — Dec '18  

        ### Logistics & Distribution Leader
        Location: Miami, United States  
        Time Worked: Aug '14 — Sep '16  

        ### Operations Management Leadership Development Program
        Location: Waukesha, Wisconsin  
        Time Worked: Jul '12 — Jul '14
        """)

        # Buttons section (organized vertically)
        linkedin_url = "https://www.linkedin.com/in/puravp"
        resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Resume_Purav_Patel.pdf'

        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>', unsafe_allow_html=True)
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>', unsafe_allow_html=True)
        st.write('<a href="mailto:patel.a.purav@gmail.com"><button class="btn btn-primary">Contact Me</button></a>', unsafe_allow_html=True)

# Call the function directly
show_about_me()
