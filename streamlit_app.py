import streamlit as st
from pyarabic.araby import tokenize
from pyarabic.araby import morphological_analysis

def analyze_sentence(sentence):
    tokens = tokenize(sentence)
    analysis = [morphological_analysis(token) for token in tokens]
    return analysis

def main():
    st.title("تحليل إعراب الجملة")

    sentence = st.text_input("أدخل الجملة:")
    if sentence:
        analysis = analyze_sentence(sentence)
        st.write("نتائج التحليل:")
        for token, analysis in zip(tokenize(sentence), analysis):
            st.write(f"{token}: {analysis}")

if __name__ == "__main__":
    main()
