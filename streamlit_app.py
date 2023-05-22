import streamlit as st
import requests

# Define the API endpoint for ChatGPT
API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'

# Set your OpenAI API key
API_KEY = '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'

# Helper function to send a chat request to ChatGPT API
def send_chat_request(message):
    headers = {
        'Authorization': 'Bearer ' + API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        'messages': [{'role': 'system', 'content': 'user'}, {'role': 'user', 'content': message}]
    }
    response = requests.post(API_ENDPOINT, json=payload, headers=headers)
    return response.json()

# Streamlit app code
def main():
    st.title("ChatGPT Streamlit App")
    st.write("Enter your message below:")

    user_input = st.text_input("User Input")

    if st.button("Send"):
        response = send_chat_request(user_input)
        messages = response['choices'][0]['message']['content']
        st.write("ChatGPT:", messages)

if __name__ == "__main__":
    main()
