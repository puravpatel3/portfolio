import streamlit as st
from streamlit_autorefresh import st_autorefresh  # Ensure this package is installed: pip install streamlit_autorefresh
import time

# ---- Remove default Streamlit menu and footer ----
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;} /* Hide the header */
    .stImage {margin-bottom: -20px;} /* Reduce gap between images and text */
    .css-1lcbmhc {padding: 1rem 1rem 1rem 1rem;} /* Reduce padding in the right column */
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---- About Me Content ----
def show_about_me():
    # Create a two-column layout: text on the left, animated images on the right
    col_text, col_image = st.columns([2, 1])
    
    # Left column: Introduction text
    with col_text:
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

        This web app serves as a platform to highlight my personal interests and technical skill sets while connecting with fellow professionals and business leaders. Feel free to explore my work and see how I integrate **data and AI** into everyday solutions.
        """)

    # Right column: Animated, centered images
    with col_image:
        # List of image URLs
        image_urls = [
            'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Wedding_Reception.jpg',
            'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Plus_Rishi.jpg',
            'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/SuShi_Wedding.jpg',
            'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/San_Diego_Bikes.jpg',
            'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/Rob_Rishi_Housewarming.jpg'
        ]

        # Use a container with custom HTML/CSS to center the image vertically and horizontally
        st.markdown("<div style='display: flex; justify-content: center; align-items: center; height: 100%;'>", unsafe_allow_html=True)
        
        # Auto-refresh every 3000 ms (3 seconds) to cycle images
        st_autorefresh(interval=3000, limit=1000, key="image_autorefresh")
        
        # Initialize or update image index in session state
        if 'image_index' not in st.session_state:
            st.session_state['image_index'] = 0
        else:
            # Increment the index automatically; using modulus ensures it cycles
            st.session_state['image_index'] = (st.session_state['image_index'] + 1) % len(image_urls)
        
        # Display the current image (centered)
        st.image(image_urls[st.session_state['image_index']], width=300)
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to show the About Me page
show_about_me()
