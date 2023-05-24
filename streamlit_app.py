import streamlit as st
import nltk
from nltk.corpus import arabic

nltk.download("arabic")

def analyze_sentence(sentence):
    # قائمة بأدوات التعريف في اللغة العربية
    definite_articles = ["ال", "لل"]

    # تحويل الجملة إلى قائمة من الكلمات
    words = sentence.split()

    # استخراج الفعل
    verb = None
    for word in words:
        if word in arabic.verbs.words():
            verb = word
            break

    # استخراج الفاعل والمفعول به
    subject = None
    object = None
    for i in range(len(words)):
        if words[i] == verb:
            if i > 0 and words[i-1] not in definite_articles:
                subject = words[i-1]
            if i < len(words)-1 and words[i+1] not in definite_articles:
                object = words[i+1]
            break

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
