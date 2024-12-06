import streamlit as st
import chat  # Import app.py directly
import about_us  # Import about_us.py directly

# Sidebar for navigation
# Sidebar title with an icon
st.sidebar.markdown(
    """
    <h1 style="display: flex; align-items: center; font-size: 20px;">
        <img src="https://cdn-icons-png.flaticon.com/512/2822/2822098.png" 
             style="width: 30px; margin-right: 10px;"> 
        Growthvision Pathum Chatbot
    </h1>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.selectbox("Page", ["About Us","Chatbot"])

# Route based on the selected page
if page == "About Us":
    about_us.run_about_us()  # Call function from about_us.py
elif page == "Chatbot":
    chat.run_chat() # Call function from app.py