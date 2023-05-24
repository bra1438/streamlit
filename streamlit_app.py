import streamlit as st
from pyarabic.araby import tokenize
from pyarabic.named import *

def analyze_sentence(sentence):
    # تقسيم الجملة إلى كلمات
    words = tokenize(sentence)

    # البحث عن الفعل والفاعل في الجملة
    verb = None
    subject = None

    for word in words:
        if is_verb(word):
            verb = word
        elif is_named_entity(word):
            subject = word

    return verb, subject

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject = analyze_sentence(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)

if __name__ == "__main__":
    main()
