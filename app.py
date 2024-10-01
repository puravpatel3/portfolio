import streamlit as st

# Main page structure with a sidebar for navigation
def main():
    st.set_page_config(page_title="My Portfolio", layout="wide")
    st.sidebar.title("Navigation")
    
    # Create navigation links for each page
    page = st.sidebar.radio("Go to", ["About Me", "Timeline", "Projects"])
    
    if page == "About Me":
        # Import the about_me page from the pages folder
        import pages.about_me as about_me
        about_me.show_about_me()
    elif page == "Timeline":
        import pages.timeline as timeline
        timeline.show_timeline()
    elif page == "Projects":
        import pages.projects as projects
        projects.show_projects()

if __name__ == "__main__":
    main()
