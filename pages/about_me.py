import streamlit as st

# Function to show the About Me page content
def show_about_me():
    # Remove the default Streamlit menu and footer (NOT the sidebar)
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} /* Hide the header */
        .markdown-text-container p {line-height: 1.5em;} /* Adjust spacing in the text */
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Create a two-column layout: left for the image,
    # Right column: Bio, Certifications, LinkedIn, and Resume Download
    col1, col2 = st.columns([1, 3])

    # Left column: Profile picture (image loaded from GitHub repository)
    image_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg'
    with col1:
        st.image(image_url, width=250)  # Increase the width for a bigger image

    # Right column: Bio and Professional Summary
    with col2:
        # Bio Section
        st.markdown("""
            ## Hi, I'm Purav!
            
            I'm an experienced data analytics professional with a passion for machine learning and AI. 
            My goal is to leverage my technical and leadership skills to drive business insights and innovations. 
            With over 10 years of experience in analytics and supply chain leadership, I excel in optimizing 
            operations, cutting costs, and boosting revenue.
        """)

        # Professional Summary Section (roles)
        st.markdown("""
            **<span style='font-size:1.3em'>Senior Order Fulfillment Analytics Manager</span>**  
            Location: Detroit, United States  
            Time Worked: Jul '21 — Present  

            **<span style='font-size:1.3em'>Order Execution & Logistics Analytics Manager</span>**  
            Location: New York, United States  
            Time Worked: Jan '19 — Jun '21  

            **<span style='font-size:1.3em'>Logistics Analytics Product Owner</span>**  
            Location: Hoboken, United States  
            Time Worked: Oct '16 — Dec '18  

            **<span style='font-size:1.3em'>Logistics & Distribution Leader</span>**  
            Location: Miami, United States  
            Time Worked: Aug '14 — Sep '16  

            **<span style='font-size:1.3em'>Operations Management Leadership Development Program</span>**  
            Location: Waukesha, Wisconsin  
            Time Worked: Jul '12 — Jul '14  
        """, unsafe_allow_html=True)

    # Buttons for LinkedIn, Resume, and Contact
    linkedin_url = "https://www.linkedin.com/in/puravp"
    resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Resume_Purav_Patel.pdf'

    col_linkedin, col_resume, col_contact = st.columns([1, 1, 1])

    # LinkedIn button
    with col_linkedin:
        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>',
                 unsafe_allow_html=True)

    # Resume download button
    with col_resume:
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>',
                 unsafe_allow_html=True)

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

# Call the function directly
show_about_me()
