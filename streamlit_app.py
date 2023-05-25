import streamlit as st
from pyarabic import araby
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel
from pyarabic.arabrepr import ArabRepr
from pyarabic.number import vocalize

def analyze_sentence(sentence):
    # تحليل النص
    tokens = tokenize(sentence)
    # إعراب الجملة
    repr = ArabRepr()
    analysis = []
    for token in tokens:
        # تحويل الأعداد إلى كلمات
        if is_arabicrange(token):
            token = vocalize(token)
        # إزالة التشكيل
        token = strip_tashkeel(token)
        # الإعراب
        arabic_word = araby.tokenize(token)
        analysis.append((token, repr.repr(arabic_word[0])))

    return analysis

def main():
    st.title("تحليل إعراب الجمل العربية")
    sentence = st.text_input("أدخل الجملة العربية:")
    if sentence:
        analysis = analyze_sentence(sentence)
        for word, analysis_result in analysis:
            st.write(f"{word}: {analysis_result}")

if __name__ == "__main__":
    main()
