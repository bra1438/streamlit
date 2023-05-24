import streamlit as st
import pyarabic.araby as araby
import stanza

def analyze_word(word):
    # تحميل نموذج اللغة العربية من stanza
    stanza.download('ar')
    nlp = stanza.Pipeline('ar')

    # تحويل الكلمة إلى شكل معرب
    arabic_word = araby.tokenize(word)[0]

    # تحليل الاعراب باستخدام stanza
    doc = nlp(arabic_word)
    sentence = doc.sentences[0]
    words = sentence.words

    # استخراج الاعراب للكلمة
    for word_info in words:
        if word_info.text == arabic_word:
            return word_info.xpos

    return None

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل اعراب الكلمات العربية")
    word = st.text_input("أدخل الكلمة:")

    if word:
        analysis = analyze_word(word)
        if analysis:
            st.write("اعراب الكلمة:", analysis)
        else:
            st.write("تعذر تحليل الكلمة")

if __name__ == "__main__":
    main()
