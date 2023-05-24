import streamlit as st
from pyarabic.araby import strip_tashkeel
import stanza

def analyze_sentence(sentence):
    # تحميل نموذج تحليل الجمل العربية من مكتبة stanza
    stanza.download("ar")
    nlp = stanza.Pipeline(lang='ar', processors='tokenize, pos')

    # تحليل الجملة
    doc = nlp(sentence)

    # استخراج المعلومات النحوية
    verb = None
    subject = None
    object = None

    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos == 'VERB':
                verb = strip_tashkeel(word.text)
            elif word.deprel == 'nsubj':
                subject = strip_tashkeel(word.text)
            elif word.deprel == 'obj':
                object = strip_tashkeel(word.text)

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
