import streamlit as st
import spacy

def analyze_sentence(sentence):
    # تحميل النموذج اللغوي العربي من spaCy
    nlp = spacy.load("xx_ent_wiki_sm")

    # تحليل الجملة باستخدام spaCy
    doc = nlp(sentence)

    # استخراج المعلومات النحوية
    sentence_analysis = []

    for token in doc:
        token_info = {
            "الكلمة": token.text,
            "التصنيف النحوي": token.pos_,
            "الوظيفة النحوية": token.dep_,
            "التفاصيل الإضافية": token.tag_
        }
        sentence_analysis.append(token_info)

    return sentence_analysis

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        sentence_analysis = analyze_sentence(sentence)
        for token_info in sentence_analysis:
            st.write("---")
            st.write("الكلمة:", token_info["الكلمة"])
            st.write("التصنيف النحوي:", token_info["التصنيف النحوي"])
            st.write("الوظيفة النحوية:", token_info["الوظيفة النحوية"])
            st.write("التفاصيل الإضافية:", token_info["التفاصيل الإضافية"])

if __name__ == "__main__":
    main()
