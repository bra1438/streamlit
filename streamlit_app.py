import streamlit as st
import pyarabic.araby as araby

def parse_sentence(sentence):
    words = araby.tokenize(sentence)
    analysis = []

    for word in words:
        if araby.is_arabicrange(word):
            parsed_word = araby.strip_tashkeel(word)
            analysis.append(f"{word}: {araby.tokenize(parsed_word)}")

    return analysis

def main():
    st.title("Simple Arabic Sentence Parsing")
    sentence = st.text_input("Enter an Arabic sentence:")

    if sentence:
        analysis = parse_sentence(sentence)
        for item in analysis:
            st.write(item)

if __name__ == "__main__":
    main()
