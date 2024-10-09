import streamlit as st

# Main App layout
def main():
    # Set page title and layout
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message for the default page
    st.title("Welcome to My Portfolio")

    # Left align the text
    st.markdown("""
    <div style='text-align: left'>
        Use the buttons below to navigate through my profiles and connect with me.
    </div>
    """, unsafe_allow_html=True)

    # Buttons section (organized horizontally)
    linkedin_url = "https://www.linkedin.com/in/puravp"
    resume_file = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf'
    contact_email = "mailto:patel.a.purav@gmail.com"

    # Creating horizontal layout for the buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f'<a href="{linkedin_url}" target="_blank"><button class="btn btn-primary">LinkedIn Profile</button></a>', unsafe_allow_html=True)

    with col2:
        st.write(f'<a href="{resume_file}" download><button class="btn btn-primary">Resume</button></a>', unsafe_allow_html=True)

    with col3:
        st.write(f'<a href="{contact_email}"><button class="btn btn-primary">Contact Me</button></a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
