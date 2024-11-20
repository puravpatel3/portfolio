# Importing necessary packages
import streamlit as st
import pandas as pd
import plotly.express as px

# Setting up web app page
st.set_page_config(page_title='Exploratory Data Analysis', page_icon=None, layout="wide")

# Adding the title and structured sections to the top of the app
st.title("**Interactive Exploratory Data Analysis (EDA) Application**")

# Adding Project Summary
st.subheader("Project Summary")
st.write("""
This app demonstrates my expertise in exploratory data analysis (EDA), providing an interactive tool where users can upload CSV or Excel files and automatically receive key EDA outputs. 
Users can preview their dataset, explore field relationships, review summary statistics, and create visualizations based on their data. EDA is a critical step in any data science workflow and forms the foundation of insightful data-driven decision-making.
""")

# Data Source
st.markdown("""
**Data Source**: [Electric Vehicle Charging Patterns Dataset on Kaggle](https://www.kaggle.com/datasets/valakhorasani/electric-vehicle-charging-patterns)

**Download Comprehensive Exploratory Data Analysis Report generated using ydata-profiling here**: [Click Here](https://github.com/puravpatel3/portfolio/blob/ade4c58b1eadc880c3c15ccd0660e40242b24619/files/ev_eda_report.html)

*Click on the 'Download raw file' button in Github to access the report*
""")

# Adding Instructions
st.subheader("Instructions")
st.write("""
By default, the app loads EV data to showcase its functionality. Users can upload their own CSV or Excel files through the 'Upload File Here' section in the sidebar. 
Once uploaded, the app enables users to browse, analyze, and visualize their data. You can review data dimensions, field descriptions, summary statistics, and generate custom visualizations to uncover key insights.
""")

# Adding Use Case
st.subheader("Use Case")
st.write("""
This app is suitable for data professionals, analysts, or businesses looking to quickly explore new datasets. It provides an efficient, no-code method for performing the initial steps of data analysis, particularly in understanding the structure and relationships within a dataset before deeper analysis or model building.
""")

# Adding Key Technologies Used
st.subheader("Key Technologies Used")
st.write("""
- **Pandas**: Essential for data manipulation and preparation.  
- **Plotly**: For generating visualizations for data analysis.  
- **Streamlit**: Used to build the interactive web application for EDA.
""")

# ================================================================================================
# Sidebar for file upload and filtering options
st.sidebar.write("****A) File upload****")

# User prompt to select file type
ft = st.sidebar.selectbox("*What is the file type?*", ["csv", "Excel"])

# Creating dynamic file upload option in sidebar
uploaded_file = st.sidebar.file_uploader("*Upload file here*", type=['csv', 'xlsx'])

# Path to the default CSV file in your GitHub repository
default_file_path = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/ev_charging_patterns.csv'

# Default to loading the CSV from GitHub if no file is uploaded
if uploaded_file is None and ft == 'csv':
    st.info(f"Loading default CSV file from GitHub: {default_file_path}")
    file_path = default_file_path
    data = pd.read_csv(file_path)
elif uploaded_file is not None:
    file_path = uploaded_file

    if ft == 'Excel':
        try:
            # Check sheet names in the Excel file and display them
            excel_file = pd.ExcelFile(file_path)
            st.write("Sheet names found in Excel:", excel_file.sheet_names)

            # User prompt to select sheet name
            sh = st.sidebar.selectbox("*Which sheet name in the file should be read?*", excel_file.sheet_names)
            
            # User prompt to define the header row with column names
            h = st.sidebar.number_input("*Which row contains the column names?*", 0, 100)
            
            # Reading the Excel file with the selected sheet and header row
            data = pd.read_excel(file_path, header=int(h), sheet_name=sh, engine='openpyxl')

        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
            st.stop()

    elif ft == 'csv':
        try:
            # Reading the CSV file
            data = pd.read_csv(file_path)
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            st.stop()

# ================================================================================================
## 1. Dataset Preview
st.write('### 1. Dataset Preview')

if 'data' in locals() and data is not None:
    try:
        # Display the dataset using st.dataframe
        st.dataframe(data, height=400)
    except Exception as e:
        st.error(f"Error displaying data: {e}")
else:
    st.error("The file wasn't read properly. Please ensure that the input parameters are correctly defined.")

# ================================================================================================
## 2. Understanding the Data
st.write('### 2. Data Exploration')

if 'data' in locals() and data is not None:
    # Creating radio button for different insights about the data, with "Summary Statistics" as the default
    selected = st.sidebar.radio("**B) What would you like to know about the data?**", 
                                ["Summary Statistics", 
                                 "Data Dimensions", 
                                 "Field Descriptions", 
                                 "Value Counts of Fields"],
                                index=0)  # Default to "Summary Statistics"

    # Showing summary statistics (Summary Statistics)
    if selected == 'Summary Statistics':
        ss = pd.DataFrame(data.describe(include='all').round(2).fillna(''))
        st.dataframe(ss, use_container_width=True)

    # Showing the shape of the dataframe (Data Dimensions)
    elif selected == 'Data Dimensions':
        st.write('###### The data has the dimensions:', data.shape)

    # Showing field types (Field Descriptions)
    elif selected == 'Field Descriptions':
        fd = data.dtypes.reset_index().rename(columns={'index': 'Field Name', 0: 'Field Type'}).sort_values(by='Field Type', ascending=False).reset_index(drop=True)
        st.dataframe(fd, use_container_width=True)

    # Showing value counts of object fields (Value Counts of Fields)
    elif selected == 'Value Counts of Fields':
        # Creating a radio button to select which object field to investigate
        sub_selected = st.sidebar.radio("*Which field should be investigated?*", data.select_dtypes('object').columns)
        vc = data[sub_selected].value_counts().reset_index().rename(columns={'index': sub_selected, sub_selected: 'Count'}).reset_index(drop=True)
        st.dataframe(vc, use_container_width=True)

# ================================================================================================
## 3. Visualization
st.write('### 3. Create Your Visualization')

if 'data' in locals() and data is not None:
    # Default values for X-axis, Y-axis, and chart type
    x_axis = st.selectbox("Choose X-axis", options=data.columns, index=list(data.columns).index('Vehicle Model'))
    y_axis = st.selectbox("Choose Y-axis", options=data.columns, index=list(data.columns).index('Energy Consumed (kWh)'))
    chart_type = st.selectbox("Select chart type", ["Bar", "Line", "Scatter"], index=2)

    # Toggle for Top X values
    filter_top_x = st.checkbox("Filter on Top X Values")
    top_x = None

    if filter_top_x:
        top_x = st.number_input("Enter the value of X (e.g., 25 for Top 25)", min_value=1, max_value=len(data), value=10)

    # Filter data for Top X values if the option is selected
    if filter_top_x and top_x:
        top_data = data.groupby(x_axis)[y_axis].count().nlargest(top_x).reset_index()
        st.write(f"Displaying Top {top_x} values based on the count of {y_axis}.")
    else:
        top_data = data

    # Generate visualizations based on user selections
    if chart_type == "Bar":
        fig = px.bar(top_data, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(top_data, x=x_axis, y=y_axis)
    elif chart_type == "Scatter":
        fig = px.scatter(top_data, x=x_axis, y=y_axis)

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("No data available for visualization. Please upload a file and try again.")
