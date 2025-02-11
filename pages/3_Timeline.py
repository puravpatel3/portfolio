import streamlit as st
import pydeck as pdk  # For map visualization

# List of roles with their corresponding locations and accomplishments
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
        "lat": 39.8918,  # Updated latitude for Glen Mills, PA
        "lon": -75.5346,  # Updated longitude for Glen Mills, PA
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

# ------------------- Session State Initialization -------------------
if 'role_index' not in st.session_state:
    st.session_state['role_index'] = 0  # Start with the first role

# ------------------- Main Title and Role Selector -------------------
st.title("Professional Timeline")
role_names = [role["role"] for role in roles]
selected_role = st.selectbox("Select Role", role_names, index=st.session_state['role_index'])
st.session_state['role_index'] = role_names.index(selected_role)

# ------------------- Function to Show Role Details and Map with Focus -------------------
def show_role_details(role):
    col1, col2 = st.columns([2, 3])

    # Left side: Role Details
    with col1:
        st.write(f"### {role['role']}")
        st.write(f"**Location:** {role['location']}")
        st.write(f"**Time Worked:** {role['time']}")
        st.write("**Top Accomplishments:**")
        for accomplishment in role['accomplishments']:
            st.write(f"- {accomplishment}")
        # Optionally keep Previous/Next buttons if desired
        col_prev, col_next = st.columns([1, 1])
        with col_prev:
            if st.button("⬅️ Previous"):
                st.session_state['role_index'] = (st.session_state['role_index'] - 1) % len(roles)
        with col_next:
            if st.button("➡️ Next"):
                st.session_state['role_index'] = (st.session_state['role_index'] + 1) % len(roles)

    # Right side: Map focused on selected role's location
    with col2:
        # Create markers for all roles
        markers = []
        for r in roles:
            markers.append({
                "lat": r["lat"],
                "lon": r["lon"],
                "role": r["role"],
                "selected": r["role"] == role["role"]
            })
        # Set view state to center on the selected role, zoomed in (e.g., zoom=10)
        view_state = pdk.ViewState(
            latitude=role["lat"],
            longitude=role["lon"],
            zoom=10,
            pitch=0
        )
        # Create a ScatterplotLayer with custom colors/sizes
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=markers,
            get_position='[lon, lat]',
            get_color="(selected ? [255, 165, 0, 255] : [200, 200, 200, 150])",  # Orange for selected, gray for others
            get_radius="(selected ? 15000 : 8000)",
            pickable=True,
        )
        # Create the deck with the view state and layer; reduce the map height
        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{role}"}
        )
        st.pydeck_chart(deck, height=300)

# ------------------- Horizontal Timeline Visualization (Optional) -------------------
def show_horizontal_timeline():
    # Create a simple horizontal timeline using a Plotly scatter plot
    timeline_df = pd.DataFrame({
        "Role": role_names,
        "Index": list(range(len(role_names)))
    })
    fig = px.scatter(timeline_df, x="Index", y=[0]*len(timeline_df), 
                     text="Role", 
                     title="Career Timeline",
                     hover_data={"Index": False, "Role": True},
                     labels={"Index": "Chronological Order"})
    # Update layout to show the timeline horizontally with custom marker size
    fig.update_traces(marker=dict(size=20, color="blue"), textposition="bottom center")
    fig.update_layout(yaxis=dict(visible=False), xaxis=dict(tickmode="linear", tick0=0, dtick=1))
    st.plotly_chart(fig, use_container_width=True)

# ------------------- Main Timeline Page -------------------
def show_timeline():
    # Get the current role based on session state
    current_role = roles[st.session_state['role_index']]
    # Show role details and map
    show_role_details(current_role)
    st.markdown("---")
    # Show horizontal timeline at the bottom
    st.subheader("Career Timeline")
    show_horizontal_timeline()

# Display the timeline
show_timeline()
