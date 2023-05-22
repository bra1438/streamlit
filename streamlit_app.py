import streamlit as st
import requests

API_URL = 'https://api.openai.com/v1/chat/completions'  # ChatGPT API URL

# Define your OpenAI API key
API_KEY = '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'

# Define the conversation history
conversation = []

# Send user input to the ChatGPT API and get the model's response
def send_message(message):
    payload = {
        'messages': [
            {'role': 'system', 'content': 'You are a user'},
            {'role': 'user', 'content': message}
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    data = response.json()
    model_response = data['choices'][0]['message']['content']
    
    return model_response

# Streamlit app
def main():
    st.title('ChatGPT Streamlit Demo')
    
    # Get user input
    user_input = st.text_input("User Input")
    
    if st.button('Send'):
        # Send user input to the model and get the response
        model_response = send_message(user_input)
        
        # Append user input and model response to the conversation history
        conversation.append(f'User: {user_input}')
        conversation.append(f'ChatGPT: {model_response}')
        
        # Display conversation history
        for message in conversation:
            st.write(message)

# Run the Streamlit app
if __name__ == '__main__':
    main()
