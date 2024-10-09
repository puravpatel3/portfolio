import streamlit as st

# Main App layout
def main():
    # Set page title and layout
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message for the default page
    st.title("Welcome to My Portfolio")

    # Additional content moved from the 'about me' section
    st.write("""
    I am a Senior Analytics Leader with 10+ years’ experience in transforming data into actionable insights. My passion lies in leveraging the power of business intelligence, machine learning, and artificial intelligence to solve complex business problems. Throughout my career, I have honed my expertise in BI and Python, building predictive models and data-driven solutions that optimize processes, reduce operational inefficiencies, and help organizations make smarter, more informed decisions.

    Beyond the technical skills, I’ve always been driven by a passion for process improvement and cross-functional collaboration. I thrive in environments where I can bring people together, whether it's aligning teams across departments or working with senior leaders to drive strategic growth. My leadership style is rooted in fostering teamwork and clear communication, ensuring that everyone from developers to executives understand the impact of analytics on business performance.

    What excites me the most is tackling large-scale analytics challenges. I’m always looking for ways to push the boundaries of what’s possible, whether through developing dashboards aligned to functional processes, building advanced machine learning models, or exploring cutting-edge AI applications. I’m eager to take on bigger projects that allow me to apply my skills on a larger stage, continuously improving and expanding my knowledge along the way.

    This web app highlights my professional interests and showcases the technical skillsets that drive my work. It serves as a platform for connecting with other professionals and business leaders, offering a glimpse into the innovative solutions I’m developing for the modern world. I invite you to explore my journey and see how data can drive real-world impact.
    """)

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
