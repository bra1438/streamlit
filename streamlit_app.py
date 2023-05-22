import streamlit as st
import requests

API_URL = "https://api.openai.com/v1/chat/completions"

def get_chat_response(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

def main():
    st.title("ChatGPT API Demo")
    user_input = st.text_input("Enter your message")
    
    if user_input:
        response = get_chat_response(user_input)
        st.text_area("AI's Reply", value=response, height=200)
    else:
        st.info("Please enter a message to start the conversation.")

if __name__ == "__main__":
    main()
