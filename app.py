import streamlit as st

# Main App layout
def main():
    # Set page title and layout
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message for the default page
    st.title("Welcome to My Portfolio")

    # Left align the intro text
    st.markdown("""
    <div style='text-align: left'>
        I am a Senior Analytics Leader with 10+ years of experience transforming data into actionable insights 
        through business intelligence, machine learning, and artificial intelligence. My career focus has been on 
        solving complex business challenges, optimizing processes, and driving smarter decisions for organizations. 
        My expertise includes:
    </div>
    """, unsafe_allow_html=True)

    # Adding bullet points for career highlights
    st.write("""
    - **Business Intelligence & Python**: Building predictive models and data-driven solutions to streamline operations and reduce inefficiencies.
    - **Leadership in Process Improvement**: Passionate about cross-functional collaboration, aligning teams, and delivering results that enhance business performance.
    - **Strategic Growth & Innovation**: Skilled in developing dashboards aligned to functional processes, improving decision-making at both operational and executive levels.
    
    **Key Career Highlights**:
    - **Proven Leadership**: A track record of leading teams and driving strategic growth by leveraging data and analytics to make impactful business decisions.
    - **Advanced Analytics**: Consistently pushing boundaries through the development of machine learning models and AI-driven applications.
    - View my [Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf) or [Timeline page](/Timeline) to see more details on my career.
    """)

    # Professional Summary title and career history
    st.subheader("Professional Summary")
    
    # Professional history using markdown for formatting
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

    # Displaying professional history in the right column
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

    # Adding hyperlinks for LinkedIn and Resume
    st.markdown("""
    **[View my LinkedIn](https://www.linkedin.com/in/puravp)**  
    **[View my Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf)**
    """)

if __name__ == "__main__":
    main()
