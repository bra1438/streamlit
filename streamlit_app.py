import streamlit as st
import spacy

def analyze_sentence(sentence):
    # تحميل النموذج اللغوي العربي من spaCy
    nlp = spacy.load("xx_ent_wiki_sm")

    # تحليل الجملة باستخدام spaCy
    doc = nlp(sentence)

    # استخراج التعابير النحوية
    word_grammatical_case = {}

    for token in doc:
        word_grammatical_case[token.text] = token._.morph.get("Case")

    return word_grammatical_case

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        word_grammatical_case = analyze_sentence(sentence)
        for word, grammatical_case in word_grammatical_case.items():
            st.write("الكلمة:", word)
            st.write("إعراب الكلمة:", grammatical_case)
            st.write("---")

if __name__ == "__main__":
    main()
