import streamlit as st
import requests

def run_chat():
    st.title("Growthvision Pathum")

    API_URL = "http://127.0.0.1:8000/ask"

    # URL ของไอคอน AI และ Human
    AI_ICON_URL = "chatbot.png"
    PEOPLE_ICON_URL = "user.png"

    # Dropdown for input method selection
    input_method = st.sidebar.selectbox("Input Method", ["Upload a File", "Enter Text Manually", "Website URL"])

    # Different input sections based on the selected method
    if input_method == "Upload a File":
        st.sidebar.file_uploader("Upload a file", type=["txt", "docx", "pdf"])
        st.sidebar.button("Upload File")

    elif input_method == "Enter Text Manually":
        st.sidebar.text_area("Text Input", height=200)
        st.sidebar.button("Upload Text")

    elif input_method == "Website URL":
        st.sidebar.text_input("Website URL", placeholder="Enter the website URL here...")
        st.sidebar.button("Upload URL")

    # Add Clear Chat History button in the sidebar
    st.sidebar.markdown("Clear Method")
    if st.sidebar.button("Clear Chat History"):
        # Reset chat history
        st.session_state.chat_history = [
            {"role": "AI", "content": "Hello Sir!, How can I help you?", "avatar": AI_ICON_URL}
        ]
        # Force rerun by clearing an unused session state variable
        st.session_state["force_refresh"] = not st.session_state.get("force_refresh", False)


    with st.expander('What can you answer in chat?'):
        st.write('''
    Guidelines for choosing a business, Q&A about industry trends. business opportunity Potential of the area Investment promotion policy Analyze policy impacts to the economic, 
    social and environmental sectors \n
    
    Tip to Prompt:\n
    • Make sure your question is within the chat limits above. for the accuracy and completeness \n
    • Always review questions before asking to maintain chat efficiency.\n
    ''')

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "AI", "content": "Hello Sir!, How can I help you?", "avatar": AI_ICON_URL}
        ]

    def ask_api_backend(input_text):
        try:
            response = requests.post(API_URL, json={"question": input_text})
            if response.status_code == 200:
                result = response.json()
                return result.get("answer", "No response from API.")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Error connecting to API: {e}"

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"], avatar=message.get("avatar", PEOPLE_ICON_URL if message["role"] == "Human" else AI_ICON_URL)):
            st.write(message["content"])

    user_query = st.chat_input("Please! Say something...")
    if user_query is not None and user_query.strip():
        st.session_state.chat_history.append(
            {"role": "Human", "content": user_query, "avatar": PEOPLE_ICON_URL}
        )

        with st.chat_message("Human", avatar=PEOPLE_ICON_URL):
            st.markdown(user_query)

        # Show a loading spinner while waiting for the response
        with st.spinner("Growthvision Pathum is generating a response..."):
            response = ask_api_backend(user_query)

        with st.chat_message("AI", avatar=AI_ICON_URL):
            st.write(response)

        st.session_state.chat_history.append(
            {"role": "AI", "content": response, "avatar": AI_ICON_URL}
        )

if __name__ == "__main__":
    run_chat()
