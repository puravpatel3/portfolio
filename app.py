import streamlit as st

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Welcome", layout="wide")

# Custom CSS to center images and adjust layout
custom_css = """
<style>
/* Hide Streamlit default menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Center the main content */
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Style for banner image */
.banner-img {
    width: 100%;
    max-height: 400px;
    object-fit: cover;
}

/* Center the profile image */
.profile-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 50%;
    width: 200px;
}

/* Style the social icons */
.social-icons a {
    margin: 0 10px;
    text-decoration: none;
    font-size: 1.2rem;
    color: #0077b5; /* LinkedIn blue; customize as needed */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------------- Main Content -------------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Banner Image (optional)
st.image("https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/banner.jpg", 
         use_column_width=True)

st.title("Welcome to My Portfolio")

# Professional Introduction (centered)
st.subheader("Introduction")
st.write("""
I am a Senior Analytics Leader with 10+ years of experience transforming data into actionable insights 
through business intelligence, machine learning, and artificial intelligence. My career focuses on solving 
complex business challenges, optimizing processes, and driving smarter decisions for organizations.
""")

# Profile Image (centered)
st.image("https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/profile.jpg", 
         width=200, output_format="auto", clamp=True, use_column_width=False, caption="Purav Patel")

# Professional Summary (resume, LinkedIn links)
st.subheader("Professional Summary")
st.write("""
I specialize in developing predictive models and creating data-driven solutions that streamline operations, 
reduce inefficiencies, and drive strategic growth. My experience spans across various industries, and I have a proven track record 
of leading teams and delivering results.
""")
st.markdown("""
**[View my LinkedIn](https://www.linkedin.com/in/puravp) | [View my Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf)**
""")

st.markdown("</div>", unsafe_allow_html=True)

# Navigation to other pages (if using multipage app, these would be in the sidebar)
st.markdown("---")
st.write("Use the sidebar to navigate to other sections of my portfolio.")
