
import streamlit as st
from chatbot_logic import get_bot_response

# Page configuration
st.set_page_config(
    page_title="My Chatbot",
    page_icon="💬"
)

st.title("💬 My First Chatbot")
st.write("Welcome! Start chatting below.")

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input box
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate chatbot response
    bot_response = get_bot_response(user_input)

    # Store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    # Refresh the application
    st.rerun()
