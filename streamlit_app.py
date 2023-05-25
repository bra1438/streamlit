import streamlit as st
import pyarabic.araby as araby
from pyarabic.named import *

def analyze_sentence(sentence):
    # تحليل الجملة إلى كلمات منفردة
    words = araby.tokenize(sentence)

    # استخراج الفعل والفاعل
    verb = None
    subject = None

    for word in words:
        # التحقق مما إذا كانت الكلمة فعلًا
        if is_verb(word):
            verb = word
        # التحقق مما إذا كانت الكلمة فاعلًا
        elif is_name(word):
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
