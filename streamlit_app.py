import streamlit as st
import spacy
from pyarabic.araby import vocalized


def ta3reeb(word):
    # تعريب الكلمة باستخدام pyarabic
    return vocalized(word)


def analyze_sentence(sentence):
    # تحميل النموذج اللغوي العربي من spaCy
    nlp = spacy.load("xx_ent_wiki_sm")

    # تحليل الجملة باستخدام spaCy
    doc = nlp(sentence)

    # استخراج المعلومات النحوية
    verb = None
    subject = None
    object = None

    for token in doc:
        if token.pos_ == "VERB":
            verb = ta3reeb(token.text)
        elif token.dep_ == "nsubj":
            subject = ta3reeb(token.text)
        elif token.dep_ == "obj":
            object = ta3reeb(token.text)

    return verb, subject, object


# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject, object = analyze_sentence(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)
        st.write("المفعول به:", object)


if __name__ == "__main__":
    main()
