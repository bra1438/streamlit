import streamlit as st
from transformers import pipeline

# Set up Streamlit layout
st.title("Arabic Sentence Analysis")

# Get user input
sentence = st.text_input("Enter an Arabic sentence:")

# Load the CHAGPT pipeline for morphological analysis
morph_pipeline = pipeline(
    "text2text-generation",
    model="mofawzany/chagpt-mgb",
    tokenizer="mofawzany/chagpt-mgb"
)

# Perform morphological analysis and extract the i'rab
def analyze_sentence(sentence):
    result = morph_pipeline(sentence, max_length=100)[0]['generated_text']
    return result

# Analyze the sentence and display the i'rab
if sentence:
    irab = analyze_sentence(sentence)
    st.header("Morphological Analysis (i'rab):")
    st.write(irab)
