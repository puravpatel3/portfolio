import streamlit as st

# ------------------- Set Page Configuration -------------------
st.set_page_config(page_title="Welcome", layout="wide")

# Custom CSS to remove default Streamlit elements and tweak spacing
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;} /* Hide the header */
    .stImage {margin-bottom: -20px;} /* Reduce gap between images and text */
    .css-1lcbmhc {padding: 1rem 1rem 1rem 1rem;} /* Adjust right column padding */
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ------------------- Banner with Overlaid Text -------------------
# Use the raw image URL for the banner (update if necessary)
banner_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/2e630dba28609877b479e8ee5e8e65c9b317a883/files/pp_banner_linkedin.jfif"
st.markdown(f"""
<div style="position: relative; text-align: center; color: white;">
  <img src="{banner_url}" style="width:100%; max-height:400px; object-fit: cover;">
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
              font-size: 3rem; font-weight: bold; text-shadow: 2px 2px 4px #000;">
    Welcome to My Portfolio
  </div>
</div>
""", unsafe_allow_html=True)

# ------------------- Main App Content -------------------
def main():
    # Create a two-column layout: left (Introduction) and right (Professional Summary)
    col1, col2 = st.columns([2, 1])

    # Left column: Introduction text
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

    # Right column: Professional Summary
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

if __name__ == "__main__":
    main()
