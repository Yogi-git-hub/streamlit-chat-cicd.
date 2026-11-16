
def get_bot_response(user_message):
    """
    Generate a simple response based on user input.
    """

    message = user_message.lower().strip()

    if message == "":
        return "Please enter a message."

    elif "hello" in message or "hi" in message:
        return "Hello! Welcome to my chatbot."

    elif "how are you" in message:
        return "I am doing great! How can I help you?"

    elif "name" in message:
        return "I am a simple Streamlit chatbot."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand. Please try again."


