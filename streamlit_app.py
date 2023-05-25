import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def extract_entities(sentence):
    # Tokenize the sentence into individual words
    words = word_tokenize(sentence)

    # Perform Part-of-Speech (POS) tagging
    tagged_words = pos_tag(words)

    # Initialize variables for verb, subject, and object
    verb = None
    subject = None
    object_ = None

    for word, tag in tagged_words:
        if tag.startswith('V'):  # Verb
            verb = word
        elif tag.startswith('N'):  # Noun
            if subject is None:
                subject = word
            else:
                object_ = word

    return verb, subject, object_

def main():
    st.title("Extraction of Verb, Subject, and Object in Arabic Sentence")
    sentence = st.text_input("Enter an Arabic sentence:")

    if sentence:
        verb, subject, object_ = extract_entities(sentence)
        st.write("Verb:", verb)
        st.write("Subject:", subject)
        st.write("Object:", object_)

if __name__ == "__main__":
    main()
