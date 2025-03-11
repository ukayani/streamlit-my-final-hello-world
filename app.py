import streamlit as st

# Set page title
st.title("Hello World App")

# Display hello world message
st.write("Hello World!")

# Optional: Add some styling
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)