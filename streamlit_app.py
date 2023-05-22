import streamlit as st
import requests

# Streamlit app title
st.title("ChatGPT API Demo")

# ChatGPT API endpoint
api_endpoint = "https://api.openai.com/v1/chat/completions"

# OpenAI API key
api_key = "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"

# User input text field
user_input = st.text_input("Enter your message:")

# Send user input to the ChatGPT API
if user_input:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_input}]
    }

    response = requests.post(api_endpoint, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        chat_response = data["choices"][0]["message"]["content"]

        # Display the response from ChatGPT
        st.text_area("ChatGPT:", value=chat_response, height=200)

# Instructions for the user
st.text("Enter a message, and the assistant will respond.")
