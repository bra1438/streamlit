import streamlit as st
from pyarabic.araby import tokenize

def analyze_sentence(sentence):
    # تقسيم الجملة إلى كلمات باستخدام pyarabic
    words = tokenize(sentence)

    # البحث عن الفعل والفاعل والمفعول به
    verb = None
    subject = None
    object = None

    for i in range(len(words)):
        word = words[i]
        if word.startswith("فعل"):
            verb = word[3:]
            # البحث عن الفاعل والمفعول به إذا كانا موجودين
            if i > 0 and words[i-1].startswith("فاعل"):
                subject = words[i-1][4:]
            if i < len(words)-1 and words[i+1].startswith("مفعول"):
                object = words[i+1][5:]

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
