import streamlit as st
import spacy

def analyze_sentence(sentence):
    nlp = spacy.load("xx_ent_wiki_sm")
    doc = nlp(sentence)

    verb = None
    subject = None
    object = None
    oblique = None
    preposition = None

    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
        elif token.dep_ == "nsubj":
            subject = token.text
        elif token.dep_ == "obj":
            object = token.text
        elif token.dep_ == "obl":
            oblique = token.text
            preposition = token.head.text

    return verb, subject, object, oblique, preposition

def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject, object, oblique, preposition = analyze_sentence(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)
        st.write("المفعول به:", object)
        st.write("اسم المجرور:", oblique)
        st.write("الحرف الجر:", preposition)

if __name__ == "__main__":
    main()
