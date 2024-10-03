# Importing necessary packages
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder

# Setting up web app page
st.set_page_config(page_title='Interactive Data Analysis App', page_icon=None, layout="wide")

# Path to the CSV file in your GitHub repository
default_file_path = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/ev_charging_patterns.csv'

# Creating section in sidebar
st.sidebar.write("****A) File upload****")

# User prompt to select file type
ft = st.sidebar.selectbox("*What is the file type?*", ["csv", "Excel"])

# Creating dynamic file upload option in sidebar
uploaded_file = st.sidebar.file_uploader("*Upload file here*", type=['csv', 'xlsx'])

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
        # Use AgGrid to display and manipulate the data
        grid_options = GridOptionsBuilder.from_dataframe(data)
        grid_options.configure_pagination(enabled=True)
        grid_options.configure_selection('multiple', use_checkbox=True)
        grid = AgGrid(data, gridOptions=grid_options.build(), enable_enterprise_modules=True, theme='alpine', height=400)
        selected_rows = grid['selected_rows']
    except Exception as e:
        st.error(f"Error displaying data: {e}")
else:
    st.error("The file wasn't read properly. Please ensure that the input parameters are correctly defined.")

# ================================================================================================
## 2. Understanding the Data
st.write('### 2. Data Exploration')

if 'data' in locals() and data is not None:
    # Creating radio button for different insights about the data
    selected = st.sidebar.radio("**B) What would you like to know about the data?**", 
                                ["Data Dimensions", 
                                 "Field Descriptions", 
                                 "Summary Statistics", 
                                 "Value Counts of Fields"])

    # Showing the shape of the dataframe (Data Dimensions)
    if selected == 'Data Dimensions':
        st.write('###### The data has the dimensions:', data.shape)

    # Showing field types (Field Descriptions)
    elif selected == 'Field Descriptions':
        fd = data.dtypes.reset_index().rename(columns={'index': 'Field Name', 0: 'Field Type'}).sort_values(by='Field Type', ascending=False).reset_index(drop=True)
        st.dataframe(fd, use_container_width=True)

    # Showing summary statistics (Summary Statistics)
    elif selected == 'Summary Statistics':
        ss = pd.DataFrame(data.describe(include='all').round(2).fillna(''))
        st.dataframe(ss, use_container_width=True)

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
    # Allow users to select variables for X and Y axes
    x_axis = st.selectbox("Choose X-axis", options=data.columns)
    y_axis = st.selectbox("Choose Y-axis", options=data.columns)

    # Select chart type
    chart_type = st.selectbox("Select chart type", ["Bar", "Line", "Scatter"])

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
