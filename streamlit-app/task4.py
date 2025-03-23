import streamlit as st
import pandas as pd
from PIL import Image

# Apply custom CSS for gradient background
st.markdown(
    """
    <style>
        /* Gradient Background */
        body {
            background: linear-gradient(to right, #ff9966, #ff5e62);
            color: white;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #3a1c71, #d76d77, #ffaf7b);
            color: white;
        }

        /* Title Styling */
        .big-title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        /* Table Styling */
        .stTable {
            background-color: rgba(255, 255, 255, 0.8);
            color: black;
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = []

# Define the five-screen workflow
st.sidebar.title("Navigation")
screen = st.sidebar.radio("Go to", ["Home", "Create", "Read", "Update", "Delete"])

# Home Screen
if screen == "Home":
    st.markdown('<h1 class="big-title">📌 Streamlit CRUD App</h1>', unsafe_allow_html=True)
    st.write("Navigate using the sidebar to perform CRUD operations.")
    image = Image.open("crud.jpg")
    st.image(image, caption="Welcome to the App!", width=600)

# Create Screenst.markdown("<h1 style='color:#6C63FF;'>🚀 Create Entry</h1>", unsafe_allow_html=True)

elif screen == "Create":
    st.title("➕ Create Entry")
    with st.form("entry_form"):
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Age", min_value=1, max_value=100, step=1)
        submit = st.form_submit_button("Add Entry")

        if submit:
            st.session_state.data.append({"Name": name, "Age": age})
            st.success("Entry Added Successfully!")

# Read Screen
elif screen == "Read":
    st.title("📋 View Entries")
    df = pd.DataFrame(st.session_state.data)
    st.markdown('<div class="stTable">', unsafe_allow_html=True)
    st.table(df)
    st.markdown('</div>', unsafe_allow_html=True)

# Update Screen
elif screen == "Update":
    st.title("✏️ Update Entry")
    df = pd.DataFrame(st.session_state.data)
    index = st.selectbox("Select Entry to Update", range(len(df)))
    if st.button("Update Age"):
        st.session_state.data[index]["Age"] += 1
        st.success("Age Updated!")

# Delete Screen
elif screen == "Delete":
    st.title("❌ Delete Entry")
    df = pd.DataFrame(st.session_state.data)
    index = st.selectbox("Select Entry to Delete", range(len(df)))
    if st.button("Delete Entry"):
        st.session_state.data.pop(index)
        st.success("Entry Deleted Successfully!")
