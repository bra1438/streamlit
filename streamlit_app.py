import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Set up Streamlit layout
st.title("Arabic Sentence Analysis")

# Get user input
sentence = st.text_input("Enter an Arabic sentence:")

# Define the CHAGPT prompt
prompt = f"""
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Define the sentence
sentence = "{sentence}"

# Load the CHAGPT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("mofawzy/chagpt")

model = AutoModelForTokenClassification.from_pretrained("mofawzy/chagpt")

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)

# Classify the tokens
inputs = tokenizer.encode(sentence, return_tensors="pt")

outputs = model(inputs)[0].argmax(2)[0]

# Map the labels to their corresponding tokens
labels = [model.config.id2label[label] for label in outputs]

# Combine tokens with labels
token_labels = list(zip(tokens, labels))

# Get the i'rab
irab = " ".join([f"{token}/{label}" for token, label in token_labels])

# Return the i'rab
irab
"""

# Call the OpenAI API to execute the code
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5
)

# Get the result from the API response
result = response.choices[0].text.strip()

# Display the i'rab
st.header("i'rab Analysis:")
st.write(result)
