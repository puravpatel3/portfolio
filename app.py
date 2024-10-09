import streamlit as st

# Main App layout
def main():
    # Set page title and layout
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message for the default page
    st.title("Welcome to My Portfolio")

    # Left align the text under the title
    st.markdown("""
    <div style='text-align: left'>
        Use the buttons below to navigate through my profiles and connect with me.
    </div>
    """, unsafe_allow_html=True)

    # Buttons section (LinkedIn and Resume arranged vertically)
    linkedin_url = "https://www.linkedin.com/in/puravp"
    resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf'

    # Creating layout for the buttons
    col1, col2, col3 = st.columns([0.5, 1, 0.5])  # Added empty columns for better centering

    with col2:
        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>', unsafe_allow_html=True)
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>', unsafe_allow_html=True)

    # Shrink the width of the text section
    st.markdown("""
    <style>
    .shrink-text {
        max-width: 50%;  /* Shrinking the text width */
    }
    </style>
    """, unsafe_allow_html=True)

    # Additional content with reduced text width
    st.write("""
    <div class="shrink-text">
        ## Hi, I'm Purav!

        I'm an experienced data analytics professional with a passion for machine learning and AI. My goal is to leverage my technical and leadership skills to drive business insights and innovations. With over 10 years of experience in analytics and supply chain leadership, I excel in optimizing operations, cutting costs, and boosting revenue.

        I built this web app to offer a deeper look into my expertise, showcase the projects I’ve worked on, and connect with other professionals who share similar passions. You’ll find a summary of my professional journey below, and more detailed insights about my roles and projects in the subpages.
    </div>
    """, unsafe_allow_html=True)

    # Professional Summary (with styling for role titles and details)
    st.write("""
    <style>
    .role-title {
        font-size: 1.2rem;
        font-weight: bold;
    }
    .role-details {
        font-size: 1rem;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Role titles and descriptions with updated location
    st.write("""
    <p class="role-title">Senior Order Fulfillment Analytics Manager</p>
    <p class="role-details">Location: Glen Mills, PA<br>Time Worked: Jul '21 — Present</p>

    <p class="role-title">Order Execution & Logistics Analytics Manager</p>
    <p class="role-details">Location: Manhattan, NY<br>Time Worked: Jan '19 — Jun '21</p>

    <p class="role-title">Logistics Analytics Product Owner</p>
    <p class="role-details">Location: Hoboken, NJ<br>Time Worked: Oct '16 — Dec '18</p>

    <p class="role-title">Logistics & Distribution Leader</p>
    <p class="role-details">Location: Miami, FL<br>Time Worked: Aug '14 — Sep '16</p>

    <p class="role-title">Operations Management Leadership Development Program</p>
    <p class="role-details">Location: Waukesha, WI<br>Time Worked: Jul '12 — Jul '14</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
