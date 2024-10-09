import streamlit as st

# Main App layout
def main():
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message and About Me content
    st.title("Welcome to My Portfolio")

    # Remove the default Streamlit menu and footer (NOT the sidebar)
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;} /* Hide the header */
        .stImage {margin-bottom: -20px;} /* Reduce gap between images and text */
        .css-1lcbmhc {padding: 1rem 1rem 1rem 1rem;} /* Reduce padding in the right column */
        .role-title {
            font-size: 1.2rem;
            font-weight: bold;
        }
        .role-details {
            font-size: 1rem;
            margin-bottom: 10px;
        }
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Create a two-column layout: left for the images and buttons, right for the text
    col1, col2 = st.columns([1, 2])

    # Left column: Profile pictures (images loaded from GitHub repository)
    image1_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg'
    image2_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Wedding_Reception.jpg'
    
    with col1:
        st.image(image1_url, width=250)
        st.image(image2_url, width=250)

        # Buttons section (organized vertically below the second image)
        linkedin_url = "https://www.linkedin.com/in/puravp"
        resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf'

        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>', unsafe_allow_html=True)
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>', unsafe_allow_html=True)
        st.write('<a href="mailto:patel.a.purav@gmail.com"><button class="btn btn-primary">Contact Me</button></a>', unsafe_allow_html=True)

    # Right column: Bio and Professional Summary
    with col2:
        st.write("""
        ## Hi, I'm Purav!

        I'm an experienced data analytics professional with a passion for machine learning and AI. My goal is to leverage my technical and leadership skills to drive business insights and innovations. With over 10 years of experience in analytics and supply chain leadership, I excel in optimizing operations, cutting costs, and boosting revenue.

        I built this web app to offer a deeper look into my expertise, showcase the projects I’ve worked on, and connect with other professionals who share similar passions. You’ll find a summary of my professional journey below, and more detailed insights about my roles and projects in the subpages.
        """)

        # Professional Summary with aligned role titles, locations, and time worked
        st.write("""
        <p class="role-title">Senior Order Fulfillment Analytics Manager</p>
        <p class="role-details">Location: Detroit, United States<br>Time Worked: Jul '21 — Present</p>

        <p class="role-title">Order Execution & Logistics Analytics Manager</p>
        <p class="role-details">Location: New York, United States<br>Time Worked: Jan '19 — Jun '21</p>

        <p class="role-title">Logistics Analytics Product Owner</p>
        <p class="role-details">Location: Hoboken, United States<br>Time Worked: Oct '16 — Dec '18</p>

        <p class="role-title">Logistics & Distribution Leader</p>
        <p class="role-details">Location: Miami, United States<br>Time Worked: Aug '14 — Sep '16</p>

        <p class="role-title">Operations Management Leadership Development Program</p>
        <p class="role-details">Location: Waukesha, Wisconsin<br>Time Worked: Jul '12 — Jul '14</p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
