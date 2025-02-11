import streamlit as st

# ------------------- Set Page Configuration -------------------
st.set_page_config(page_title="Welcome", layout="wide")

# ------------------- Custom CSS -------------------
custom_css = """
<style>
/* Hide default Streamlit menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Center main content */
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Banner image styling */
.banner-img {
    width: 100%;
    max-height: 250px;  /* Reduced height */
    object-fit: cover;
}

/* Profile image styling */
.profile-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 50%;
    width: 200px;
}

/* Social icon styling */
.social-icons a {
    margin: 0 10px;
    text-decoration: none;
    font-size: 1.2rem;
    color: #0077b5;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------------- Banner -------------------
# Display the banner image without any overlaid text
st.image("https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/pp_banner_linkedin.jfif", 
         use_column_width=True)

# ------------------- Main Content -------------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Title and Introduction
st.title("Welcome to My Portfolio")

# Create a two-column layout: left for text, right for profile image
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Introduction")
    st.write("""
    I am a Senior Analytics Leader with 10+ years of experience transforming data into actionable insights 
    through business intelligence, machine learning, and artificial intelligence. My career focus has been on 
    solving complex business challenges, optimizing processes, and driving smarter decisions for organizations. 
    My expertise includes:
    """)
    st.write("""
    - **Business Intelligence & Python**: Building predictive models and data-driven solutions to streamline operations and reduce inefficiencies.
    - **Leadership in Process Improvement**: Passionate about cross-functional collaboration, aligning teams, and delivering results that enhance business performance.
    - **Strategic Growth & Innovation**: Skilled in developing dashboards aligned to functional processes, improving decision-making at both operational and executive levels.

    **Key Career Highlights**:
    - **Proven Leadership**: A track record of leading teams and driving strategic growth by leveraging data and analytics to make impactful business decisions.
    - **Advanced Analytics**: Consistently pushing boundaries through the development of machine learning models and AI-driven applications.
    - View my [Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf) or Timeline page to see more details on my career.
    """)
    st.markdown("""
    **[View my LinkedIn](https://www.linkedin.com/in/puravp)**  
    **[View my Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf)**
    """)

with col2:
    st.subheader("Professional Summary")
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

st.markdown("</div>", unsafe_allow_html=True)
