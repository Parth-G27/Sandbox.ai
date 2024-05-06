import streamlit as st

# Function to generate response based on user input
def generate_response(question):
    # Here you can implement your logic to generate responses
    response = f"You asked: '{question}'. Sorry, I don't have a response for that yet."
    return response

# Main function to run the Streamlit app
def main():
    st.title("Chat with the AI")

    # Initialize empty list to store chat history
    chat_history = []

    # Text input for users to send questions
    user_input = st.text_input("You:", "")

    # Check if user sent a question
    if st.button("Send"):
        if user_input:
            # Generate response
            response = generate_response(user_input)
            chat_history.append(("You", user_input))
            chat_history.append(("AI", response))

    # Display chat history
    if chat_history:
        st.write("")
        st.write("Chat History:")
        for sender, message in chat_history:
            if sender == "You":
                st.text_input("You:", message, key=message)
            else:
                st.text_input("AI:", message, key=message)

# Run the app
if __name__ == "__main__":
    main()
