import streamlit as st
from pyarabic.araby import strip_tashkeel
from WordNetArabic.WordNet import ArabicWordNet

def analyze_sentence(sentence):
    # تنظيف الجملة من التشكيل
    sentence = strip_tashkeel(sentence)

    # تحميل قاموس المعاني العربي
    wordnet = ArabicWordNet()

    # استخراج المعلومات النحوية
    verb = None
    subject = None
    object = None

    # تحليل الجملة إلى كلمات
    words = sentence.split()

    # العثور على الفعل
    for word in words:
        if wordnet.is_verb(word):
            verb = word
            break

    # العثور على الفاعل والمفعول به
    for word in words:
        if wordnet.is_noun(word):
            if verb and wordnet.is_subject(verb, word):
                subject = word
            elif verb and wordnet.is_object(verb, word):
                object = word

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
