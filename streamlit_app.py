import streamlit as st
from arabicnlp import ArabicPOS

def tag_pos(text):
    pos_tagger = ArabicPOS()
    tagged_text = pos_tagger.tag(text)
    return tagged_text

def main():
    st.title("POS Tagging for Arabic Text")
    text = st.text_input("Enter Arabic text:")

    if text:
        tagged_text = tag_pos(text)
        for word, tag in tagged_text:
            st.write("Word:", word)
            st.write("POS Tag:", tag)
            st.write("---")

if __name__ == "__main__":
    main()
