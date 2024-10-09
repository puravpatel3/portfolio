import streamlit as st

# Function to show the About Me page content
def show_about_me():
    # Remove the default Streamlit menu and footer (NOT the sidebar)
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;} /* Hide the header */
    .stImage {margin-bottom: -20px;} /* Reduce gap between images and text */
    .css-1lcbmhc {padding: 1rem 1rem 1rem 1rem;} /* Reduce padding in the right column */
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Create a two-column layout: left for the text and right for the image
    col1, col2 = st.columns([2, 1])

    # Left column: Introduction text
    with col1:
        st.write("""
        ## Hi, I'm Purav!

        I'm a data analytics professional with a deep passion for **machine learning**, **AI**, and **business intelligence**. With over 10 years of experience in analytics and supply chain leadership, I’ve honed my skills in creating predictive models and data-driven solutions that **optimize operations**, **reduce inefficiencies**, and **drive smarter decision-making**.

        ### Education:
        - **Executive MBA**, Quantic School of Business and Technology
        - **Bachelors in Industrial Engineering**, Penn State University

        ### Interests:
        - **Fitness**: I enjoy staying active with **Orange Theory**, **Boxing**, and **Weightlifting**.
        - **Stock Trading**: I actively trade the stock market through **Options** and **Swing Trading**.
        - **Politics and the Economy**: I keep up with the latest trends in **politics** and **economic changes**.

        ### How I Use AI in Everyday Life:
        - **Meal Planning**: I use AI to plan meals weekly, create optimized grocery lists, and streamline my meal prep.
        - **Productivity**: AI helps me plan my weeks and months more effectively.
        - **Coding**: I leverage AI to assist with writing and improving my code for various projects.

        This web app serves as a platform to highlight my interests and technical skillsets while connecting with fellow professionals and business leaders. I invite you to explore my work and see how I integrate **data and AI** into everyday solutions.
        """)

    # Right column: Profile picture (Wedding Reception image)
    image_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Wedding_Reception.jpg'
    with col2:
        st.image(image_url, width=250)

# Call the function directly
show_about_me()
