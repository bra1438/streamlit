import streamlit as st
import spacy

def extract_verb_subject(sentence):
    # تحميل النموذج اللغوي العربي من spaCy
    nlp = spacy.load("xx_ent_wiki_sm")

    # تحليل الجملة باستخدام spaCy
    doc = nlp(sentence)

    # استخراج الفعل والفاعل
    verb = None
    subject = None

    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
        elif token.dep_ == "nsubj":
            subject = token.text

    return verb, subject

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("استخراج الفعل والفاعل")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject = extract_verb_subject(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)

if __name__ == "__main__":
    main()
