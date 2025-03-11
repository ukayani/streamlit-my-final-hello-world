import streamlit as st

# Set page title
st.title("Hello Universe App")

# Display hello universe message
st.write("Hello Universe!")

# Optional: Add some styling
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)