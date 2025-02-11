import streamlit as st
import pydeck as pdk  # For map visualization
import pandas as pd
from datetime import datetime
import plotly.express as px

# ------------------- Helper Function to Compute Years in Role -------------------
def compute_years(time_str):
    """
    Computes the number of years between the start and end dates given in time_str.
    The time_str is assumed to be in the format "Mon 'YY — Mon 'YY" or "Mon 'YY — Present".
    """
    try:
        parts = time_str.split("—")
        start_str = parts[0].strip()  # e.g., "Jul '12"
        end_str = parts[1].strip()    # e.g., "Jul '14" or "Present"
        start_date = datetime.strptime(start_str, "%b '%y")
        if end_str.lower() == "present":
            end_date = datetime.now()
        else:
            end_date = datetime.strptime(end_str, "%b '%y")
        return (end_date - start_date).days / 365.25
    except Exception as e:
        return None

# ------------------- List of Roles -------------------
roles = [
    {
        "role": "Operations Management Leadership Development Program",
        "location": "Waukesha, WI",
        "lat": 43.0117,
        "lon": -88.2315,
        "time": "Jul '12 — Jul '14",
        "accomplishments": [
            "Held four separate supply chain roles covering manufacturing, lean, six sigma, order execution, and warehouse ops.",
            "Directed production plan to bring Accessories production line on time delivery from 45% FW13 to 89% FW23.",
            "Implemented process standards in warehouse operations leading to a reduction of $1.1M in inventory.",
            "Executed 100% of Q2 production plan and reduced work-in-progress inventory by 30 MR Cabinets (~$1.5M ICV)."
        ]
    },
    {
        "role": "Logistics & Distribution Leader",
        "location": "Miami, FL",
        "lat": 25.7617,
        "lon": -80.1918,
        "time": "Aug '14 — Sep '16",
        "accomplishments": [
            "Managed logistics operations for Imaging Systems inbound to Miami and outbound to South America.", 
            "Increased on-time delivery by 16% by developing and implementing standard work with primary logistics carriers.",
            "Planned and executed ~130 Magnetic Resonance (MR) shipments inbound to Miami and outbound to Latin America."
        ]
    },
    {
        "role": "Logistics Analytics Product Owner",
        "location": "Hoboken, NJ",
        "lat": 40.7433,
        "lon": -74.0324,
        "time": "Oct '16 — Dec '18",
        "accomplishments": [
            "Developed the global logistics data warehouse providing visibility to $450M annual spend and set up ERP with Oracle Transportation Management (OTM) data architecture.",
            "Created global lead time standards for internal and external customer shipments by mining and modeling 5+ data sources (1M+ rows of data), changing 40% of incorrectly set up lead times.",
            "Defined the data architecture for the new OTM data source and overhauled the existing data source by removing 70% of redundant code and reducing load time by 90%."
        ]
    },
    {
        "role": "Order Execution & Logistics Analytics Manager",
        "location": "Manhattan, NY",
        "lat": 40.7128,
        "lon": -74.0060,
        "time": "Jan '19 — Jun '21",
        "accomplishments": [
            "Led a team of 2 Product Owners focused on developing analytical tools to streamline the order execution process, support logistics cost savings initiatives, and provide visibility to logistics lead times.",
            "Led multiple continuous improvement events to revamp OTD analytics: expanded automated defect reason codes from 4 to 50+, provided visibility to cross-functional defect relationships, and developed function-specific analytics views.",
            "Supported logistics projects (Air to Ocean, Premium Reduction, Consolidations) by developing cost-focused analytical views, helping enable $2.5M in cost savings.",
            "Developed lead time analytical views to identify and rectify manufacturing lead time gaps, improving adherence by 15%."
        ]
    },
    {
        "role": "Senior Order Fulfillment Analytics Manager",
        "location": "Glen Mills, PA",
        "lat": 39.8918,
        "lon": -75.5346,
        "time": "Jul '21 — Present",
        "accomplishments": [
            "Coached a global team of 4 Product Owners focused on analytical reporting and maintaining a pipeline of projects to improve revenue linearity, on-time delivery, cost reduction, and process standard work.",
            "Implemented a machine learning model in Python (sklearn) to predict On-Time Delivery (OTD) with 70% accuracy, enabling proactive order management and fulfillment.",
            "Developed and deployed a machine learning model in Python to predict delivery dates with 74% accuracy, enabling supply chain teams to better anticipate delays and improve delivery reliability.",
            "Engineered a Python-based solution to align aging inventory with open order demand, uncovering a $5M opportunity by optimizing inventory allocation across regions, sub-regions, and distribution organizations.",
            "Hosted a company-wide ‘Intro to AI’ workshop for 200+ employees, demonstrating actionable steps to leverage AI in both professional and personal contexts to drive efficiency across everyday tasks."
        ]
    }
]

# Precompute years for each role and add as a new key "years"
for role in roles:
    role["years"] = compute_years(role["time"])

# ------------------- Session State Initialization -------------------
if 'role_index' not in st.session_state:
    st.session_state['role_index'] = 0  # Start with the first role

# Create a global list of role names
role_names = [role["role"] for role in roles]

# ------------------- Main Title and Role Selector -------------------
st.title("Professional Timeline")
selected_role = st.selectbox("Select Role", role_names, index=st.session_state['role_index'])
st.session_state['role_index'] = role_names.index(selected_role)

# ------------------- Function to Show Role Details and Map -------------------
def show_role_details(role):
    # Define columns: left for details, right for map
    col1, col2 = st.columns([2, 1.5])
    
    # Left side: Role Details
    with col1:
        st.write(f"### {role['role']}")
        st.write(f"**Location:** {role['location']}")
        st.write(f"**Time Worked:** {role['time']}")
        st.write(f"**Years in Role:** {role['years']:.1f} years")
        st.write("**Top Accomplishments:**")
        for accomplishment in role['accomplishments']:
            st.write(f"- {accomplishment}")
    
    # Right side: Map without markers, zoomed in on the selected role's location
    with col2:
        view_state = pdk.ViewState(
            latitude=role["lat"],
            longitude=role["lon"],
            zoom=10,
            pitch=0
        )
        deck = pdk.Deck(
            layers=[],  # No markers displayed
            initial_view_state=view_state
        )
        st.pydeck_chart(deck, height=400)

# ------------------- Horizontal Timeline as a Bar Chart -------------------
def show_horizontal_timeline():
    timeline_df = pd.DataFrame({
        "Role": role_names,
        "Order": [i + 1 for i in range(len(role_names))],
        "Years": [role["years"] for role in roles]
    })
    fig = px.bar(timeline_df, x="Order", y="Years", text="Role", 
                 title="Career Timeline",
                 labels={"Order": "Chronological Order", "Years": "Years in Role"},
                 hover_data={"Role": True, "Years": ":.1f"})
    fig.update_traces(textposition="outside", marker_color="#99ccff")
    fig.update_layout(xaxis=dict(tickmode="linear", tick0=1, dtick=1))
    st.plotly_chart(fig, use_container_width=True)

# ------------------- Main Timeline Page -------------------
def show_timeline():
    current_role = roles[st.session_state['role_index']]
    show_role_details(current_role)
    st.markdown("---")
    st.subheader("Career Timeline")
    show_horizontal_timeline()

show_timeline()
