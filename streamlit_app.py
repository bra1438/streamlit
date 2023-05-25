import streamlit as st
import pyarabic.araby as araby
from pyarabic.araby import tokenize as tokenize_arabic
from pyarabic.araby import strip_tashkeel

def pos_tag_arabic(text):
    tokens = tokenize_arabic(strip_tashkeel(text))
    pos_tags = araby.pos(tokens)
    return list(zip(tokens, pos_tags))

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل تصنيف الكلمات في العربية")
    text = st.text_area("أدخل النص العربي:")

    if text:
        pos_tags = pos_tag_arabic(text)
        for token, pos in pos_tags:
            st.write("الكلمة:", token)
            st.write("تصنيف الكلمة:", pos)
            st.write("---")

if __name__ == "__main__":
    main()
