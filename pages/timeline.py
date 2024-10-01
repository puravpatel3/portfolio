import streamlit as st
import pydeck as pdk  # For map visualization

# List of roles with their corresponding locations
roles = [
    {
        "role": "Operations Management Leadership Development Program",
        "location": "Waukesha, Wisconsin",
        "lat": 43.0117,
        "lon": -88.2315,
        "time": "Jul '12 — Jul '14",
        "accomplishments": [
            "Increased Accessories production line OTD from 45% to 89%.",
            "Reduced work-in-progress inventory by 30 units ($1.5M value).",
            "Implemented process standards reducing $1.1M in inventory."
        ]
    },
    {
        "role": "Logistics & Distribution Leader",
        "location": "Miami, United States",
        "lat": 25.7617,
        "lon": -80.1918,
        "time": "Aug '14 — Sep '16",
        "accomplishments": [
            "Increased on-time delivery by 16% by standardizing logistics carrier work.",
            "Planned and executed 130+ MR shipments to Latin America."
        ]
    },
    {
        "role": "Logistics Analytics Product Owner",
        "location": "Hoboken, United States",
        "lat": 40.7433,
        "lon": -74.0324,
        "time": "Oct '16 — Dec '18",
        "accomplishments": [
            "Overhauled OTM data source reducing load time by 90%.",
            "Created global lead time standards affecting 40% of shipments.",
            "Managed 7 digital projects focused on cost savings and forecasting."
        ]
    },
    {
        "role": "Order Execution & Logistics Analytics Manager",
        "location": "New York, United States",
        "lat": 40.7128,
        "lon": -74.0060,
        "time": "Jan '19 — Jun '21",
        "accomplishments": [
            "Led team to streamline order execution and save $2.5M in costs.",
            "Developed lead time analytics improving adherence by 15%.",
            "Expanded defect reason codes from 4 to 50+."
        ]
    },
    {
        "role": "Senior Order Fulfillment Analytics Manager",
        "location": "Detroit, United States",
        "lat": 42.3314,
        "lon": -83.0458,
        "time": "Jul '21 — Present",
        "accomplishments": [
            "Led cross-functional project to improve order delivery by 10%.",
            "Developed supply chain KPI dashboards resulting in a 20% improvement.",
            "Designed a revenue linearity dashboard leading to a 30% backlog reduction."
        ]
    }
]

# Set up session state to track current role index (start with first role by default)
if 'role_index' not in st.session_state:
    st.session_state['role_index'] = 0  # Start with the first role

# Function to show role details and map location
def show_role_details(role):
    col1, col2 = st.columns([2, 1])

    # Left side: role details
    with col1:
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
                if st.session_state['role_index'] > 0:
                    st.session_state['role_index'] -= 1
        with col_next:
            if st.button("➡️ Next"):
                if st.session_state['role_index'] < len(roles) - 1:
                    st.session_state['role_index'] += 1

    # Right side: Map view
    with col2:
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=role['lat'],
                longitude=role['lon'],
                zoom=10,
                pitch=50,
            )
        ))

# Timeline Page
def show_timeline():
    st.title("Professional Timeline")

    # Filter section (can be expanded as needed)
    st.write("### Filter by Role, Projects, or Skills")
    filter_type = st.selectbox("Filter By", ["All", "Roles", "Projects", "Skills"])

    # Display the current role details and map
    role = roles[st.session_state['role_index']]
    show_role_details(role)

# Main app layout
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Timeline", "Projects"])

    if page == "Timeline":
        show_timeline()

if __name__ == "__main__":
    main()
