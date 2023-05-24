import streamlit as st
import spacy

def analyze_sentence(sentence):
    # Load the Arabic language model from spaCy
    nlp = spacy.load("xx_ent_wiki_sm")

    # Analyze the sentence using spaCy
    doc = nlp(sentence)

    # Extract grammatical information
    verb = None
    subject = None

    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
        elif token.dep_ == "nsubj":
            subject = token.text

    return verb, subject

# Configure the user interface using Streamlit
def main():
    st.title("Arabic Sentence Analysis")
    sentence = st.text_input("Enter the sentence:")

    if sentence:
        verb, subject = analyze_sentence(sentence)
        st.write("Verb:", verb)
        st.write("Subject:", subject)

if __name__ == "__main__":
    main()
