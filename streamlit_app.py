import streamlit as st
from pyarabic.araby import vocalized_word
from pyarabic.araby import tokenize
from pyarabic.araby import strip_tashkeel
from pyarabic.araby import is_arabicrange

def analyze_sentence(sentence):
    tokens = tokenize(sentence)
    analyzed_sentence = ""
    for token in tokens:
        if is_arabicrange(token):
            token = strip_tashkeel(token)
            token = vocalized_word(token)
        analyzed_sentence += token + " "
    return analyzed_sentence.strip()


def main():
    st.title("تطبيق الإعراب")

    sentence = st.text_input("أدخل الجملة العربية:")
    if st.button("إعراب"):
        analyzed_sentence = analyze_sentence(sentence)
        st.write("الجملة العربية المعربة:")
        st.write(analyzed_sentence)

if __name__ == "__main__":
    main()
