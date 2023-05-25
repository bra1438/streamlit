import streamlit as st
import pyarabic.arabrepr as arabrepr
import pyarabic.araby as araby
from pyarabic.named import *

def find_verb_subject(sentence):
    words = araby.tokenize(sentence)

    verb = None
    subject = None

    for word in words:
        root_word = strip_tashkeel(word)
        analysis = arabrepr.ArabicRepresentations(root_word)

        if analysis.is_verb():
            verb = word
        elif analysis.is_noun():
            subject = word

    return verb, subject

def main():
    st.title("Finding Verb and Subject in Arabic Sentence")
    sentence = st.text_input("Enter an Arabic sentence:")

    if sentence:
        verb, subject = find_verb_subject(sentence)
        st.write("Verb:", verb)
        st.write("Subject:", subject)

if __name__ == "__main__":
    main()
