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

    # Create a two-column layout: left for the images, right for the text
    col1, col2 = st.columns([1, 3])

    # Left column: Profile pictures (image loaded from GitHub repository)
    image1_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg'
    image2_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Wedding_Reception.jpg'

    with col1:
        # Display the first image
        st.image(image1_url, width=250)
        # Display the second image
        st.image(image2_url, width=250)

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

    # Buttons for LinkedIn, Resume, and Contact Me
    linkedin_url = "https://www.linkedin.com/in/puravp"
    resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Resume_Purav_Patel.pdf'
    email_address = 'mailto:patel.a.purav@gmail.com'

    # Align buttons beneath the text, spaced out neatly
    col_button_linkedin, col_button_resume, col_button_contact = st.columns([1, 1, 1])

    # LinkedIn button
    with col_button_linkedin:
        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>',
                 unsafe_allow_html=True)

    # Resume download button
    with col_button_resume:
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>',
                 unsafe_allow_html=True)

    # Contact Me button with hyperlink
    with col_button_contact:
        st.write(f'<a href="{email_address}" target="_blank"><button class="btn btn-primary">Contact Me</button></a>',
                 unsafe_allow_html=True)

# Call the function directly
show_about_me()
