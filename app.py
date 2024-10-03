import streamlit as st

# Main App layout
def main():
    st.set_page_config(page_title="My Portfolio", layout="wide")

    # Welcome message for the default page (you can leave this empty or customize it)
    st.title("Welcome to My Portfolio")
    st.write("Use the sidebar to navigate through different sections of the portfolio.")

if __name__ == "__main__":
    main()
