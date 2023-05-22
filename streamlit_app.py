import streamlit as st
import requests

# Define API endpoint
API_URL = 'https://api.openai.com/v1/chat/completions'

# Set your OpenAI API key
API_KEY = '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'

# Streamlit app configuration
st.title('ChatGPT Demo')
st.subheader('Enter a message and get a response from ChatGPT')

# User input form
user_input = st.text_input('User Input')

if user_input:
    # Make API request to ChatGPT
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': user_input}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        # Get the model-generated response
        chat_response = response.json()['choices'][0]['message']['content']
        st.text_area('ChatGPT Response', value=chat_response, height=100)

