import streamlit as st
import pydeck as pdk  # For map visualization
import pandas as pd

# List of roles with their corresponding locations
roles = [
    {
        "role": "Senior Order Fulfillment Analytics Manager",
        "location": "Detroit, United States",
        "lat": 42.3314,
        "lon": -83.0458,
        "time": "Jul '21 — Present",
        "accomplishments": [
            "Led cross-functional project to improve order delivery and revenue flow by developing Celonis analytics views for performance insights, automated reason codes, and proactive material visibility, resulting in a 10% delivery improvement.",
            "Enhanced business strategy by developing Supply Chain Key Performance Indicator (KPI) dashboards for tracking standard work compliance, analyzing date changes, and identifying outliers, resulting in a 20% improvement in order delivery times and optimal decision making.",
            "Designed a revenue linearity dashboard identifying past due orders across multiple dimensions and created Standard Operating Procedures for users helping enable a 30% reduction in past due backlog year over year."
        ]
    },
    {
        "role": "Order Execution & Logistics Analytics Manager",
        "location": "New York, United States",
        "lat": 40.7128,
        "lon": -74.0060,
        "time": "Jan '19 — Jun '21",
        "accomplishments": [
            "Led multiple continuous improvement events to revamp OTD analytics: expanded automated defect reason codes from 4 to 50+, provided visibility to cross-functional defect relationships, and developed function specific analytics views.",
            "Supported logistics projects (Air to Ocean, Premium Reduction, Consolidations) by developing cost focused analytical views helping enable $2.5M in cost savings.",
            "Developed lead time analytical views to identify and rectify manufacturing lead time gaps improving adherence by 15%."
        ]
    },
    {
        "role": "Logistics Analytics Product Owner",
        "location": "Hoboken, United States",
        "lat": 40.7433,
        "lon": -74.0324,
        "time": "Oct '16 — Dec '18",
        "accomplishments": [
            "Created global lead time standards for internal and external customer shipments by mining and modeling 5+ data sources (1M+ rows of data) leading to a change in 40% of incorrectly set up lead times.",
            "Defined the data architecture for the new OTM data source and overhauled the existing data source by removing 70% of redundant code and reducing load time by 90%."
        ]
    },
    {
        "role": "Logistics & Distribution Leader",
        "location": "Miami, United States",
        "lat": 25.7617,
        "lon": -80.1918,
        "time": "Aug '14 — Sep '16",
        "accomplishments": [
            "Increased on time delivery by 16% by developing and implementing standard work with primary logistics carriers.",
            "Planned and executed ~130 Magnetic Resonance (MR) shipments inbound to Miami and outbound to Latin America."
        ]
    },
    {
        "role": "Operations Management Leadership Development Program",
        "location": "Waukesha, Wisconsin",
        "lat": 43.0117,
        "lon": -88.2315,
        "time": "Jul '12 — Jul '14",
        "accomplishments": [
            "Held four separate supply chain roles covering manufacturing, lean, six sigma, order execution, and warehouse ops.",
            "Directed production plan to bring Accessories production line on time delivery from 45% FW13 to 89% FW23.",
            "Implemented process standards in warehouse operations leading to a reduction of $1.1M in inventory."
        ]
    }
]

# Set up session state to track current role index (start with first role by default)
if 'role_index' not in st.session_state:
    st.session_state['role_index'] = 0  # Start with the first role

# Function to show role details and map location
def show_role_details(role):
    st.write(f"### {role['role']}")
    st.write(f"**Location:** {role['location']}")
    st.write(f"**Time Worked:** {role['time']}")
    st.write("**Top Accomplishments:**")
    for accomplishment in role['accomplishments']:
        st.write(f"- {accomplishment}")

    # Previous and Next buttons below the role description
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("⬅️ Previous"):
            st.session_state['role_index'] = (st.session_state['role_index'] - 1) % len(roles)
    with col_next:
        if st.button("➡️ Next"):
            st.session_state['role_index'] = (st.session_state['role_index'] + 1) % len(roles)

# Function to show the timeline table
def show_timeline_table():
    # Create a DataFrame for displaying roles in reverse order
    timeline_df = pd.DataFrame(
        [(role['role'], role['location'], role['time']) for role in roles],
        columns=["Role", "Location", "Time Worked"]
    )

    # Reverse the order for most recent role first
    timeline_df = timeline_df.iloc[::-1].reset_index(drop=True)

    # Style the table: bold the first row (header) and remove the index
    st.write("### Professional Timeline")
    st.table(timeline_df.style.set_properties(**{'font-weight': 'bold'}, subset=pd.IndexSlice[:1]))

# Timeline Page
def show_timeline():
    # Layout: Table and Role Details on left, Map on right
    col1, col2 = st.columns([2, 1])

    with col1:
        # Display the timeline table
        show_timeline_table()

        # Display the current role details
        role = roles[st.session_state['role_index']]
        show_role_details(role)

    # Right side: Map view (centered relative to Table and Role Details)
    with col2:
        role = roles[st.session_state['role_index']]
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=role['lat'],
                longitude=role['lon'],
                zoom=10,
                pitch=50,
            )
        ))

# Call show_timeline directly since this is part of the pages directory
show_timeline()
