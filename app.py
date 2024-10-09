import streamlit as st

# Main App layout
def main():
    # Set page title and layout
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Title
    st.title("Welcome to My Portfolio")

    # Create two columns for Introduction and Professional Summary
    col1, col2 = st.columns([1, 1])

    # Left column for Introduction
    with col1:
        st.subheader("Introduction")
        st.write("""
        I am a Senior Analytics Leader with 10+ years’ experience in transforming data into actionable insights. 
        My passion lies in leveraging the power of business intelligence, machine learning, and artificial intelligence to solve complex business problems. 
        Throughout my career, I have honed my expertise in BI and Python, building predictive models and data-driven solutions that optimize processes, 
        reduce operational inefficiencies, and help organizations make smarter, more informed decisions.

        Beyond the technical skills, I’ve always been driven by a passion for process improvement and cross-functional collaboration. I thrive in environments 
        where I can bring people together, whether it's aligning teams across departments or working with senior leaders to drive strategic growth. My leadership 
        style is rooted in fostering teamwork and clear communication, ensuring that everyone from developers to executives understands the impact of analytics 
        on business performance.

        What excites me the most is tackling large-scale analytics challenges. I’m always looking for ways to push the boundaries of what’s possible, whether 
        through developing dashboards aligned to functional processes, building advanced machine learning models, or exploring cutting-edge AI applications. 
        I’m eager to take on bigger projects that allow me to apply my skills on a larger stage, continuously improving and expanding my knowledge along the way.

        This web app highlights my professional interests and showcases the technical skillsets that drive my work. It serves as a platform for connecting 
        with other professionals and business leaders, offering a glimpse into the innovative solutions I’m developing for the modern world. I invite you to 
        explore my journey and see how data can drive real-world impact.
        """)

        # Add the LinkedIn and Resume links
        st.markdown("""
        - [View my LinkedIn](https://www.linkedin.com/in/puravp)
        - [View my Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf)
        """)

    # Right column for Professional Summary
    with col2:
        st.subheader("Professional Summary")
        st.write("""
        - **Senior Order Fulfillment Analytics Manager**  
          Glen Mills, PA | Jul '21 — Present  
          Led cross-functional teams to optimize supply chain processes, implement advanced machine learning solutions, 
          and enhance business intelligence strategies.

        - **Order Execution & Logistics Analytics Manager**  
          Manhattan, NY | Jan '19 — Jun '21  
          Spearheaded logistics analytics projects and drove improvements in order execution for multiple global markets.

        - **Logistics Analytics Product Owner**  
          Hoboken, NJ | Oct '16 — Dec '18  
          Managed the development and implementation of global logistics analytics tools and BI dashboards to enhance decision-making.

        - **Logistics & Distribution Leader**  
          Miami, FL | Aug '14 — Sep '16  
          Improved distribution processes, working closely with cross-functional teams to optimize logistics across Latin American markets.

        - **Operations Management Leadership Development Program**  
          Waukesha, WI | Jul '12 — Jul '14  
          Completed rotations in various supply chain functions, including manufacturing, lean six sigma, and warehouse operations.

        - [View my Resume](https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Purav_Patel_Resume.pdf)
        - [View my Timeline page](https://portfolio-ksemrcmfvzxuhoc5384p3t.streamlit.app/timeline)
        """)

if __name__ == "__main__":
    main()
