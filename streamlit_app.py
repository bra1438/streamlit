import streamlit as st
from pyarabic.araby import tokenize, strip_tashkeel

def analyze_sentence(sentence):
    # تقسيم الجملة إلى كلمات
    words = tokenize(sentence)

    # استخراج الفعل والفاعل من الجملة
    verb = None
    subject = None

    for word in words:
        word = strip_tashkeel(word)  # إزالة التشكيل
        if word.endswith("ت"):
            verb = word
        elif word.endswith("ى") or word.endswith("ي"):
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
