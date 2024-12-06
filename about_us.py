import streamlit as st

def run_about_us():
   # Display the title with an icon
    st.markdown(
        """
        <h1 style="display: flex; align-items: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/2822/2822098.png" 
                style="width: 40px; margin-right: 10px;"> 
            Growthvision Pathum Chatbot
        </h1>
        """,
        unsafe_allow_html=True,
    )
    st.write("""
    Welcome to the Growthvision Pathum Chatbot!
    
    This Chatbot is part of Project for DSI314 .
    """)
    st.image("https://www.hotelscombined.com/rimg/dimg/70/90/7c83edf5-city-306158-17304426830.jpg?width=1366&height=768&xhint=1020&yhint=993&crop=true", caption="Pathum Thani")