import streamlit as st
from pyarabic.araby import morphological_analysis

def analyze_verb_subject(sentence):
    # استخراج الفعل والفاعل باستخدام PyArabic
    analysis = morphological_analysis(sentence)
    
    verb = None
    subject = None

    for word in analysis:
        if 'فعل' in word['pos']:
            verb = word['word']
        elif 'اسم' in word['pos']:
            subject = word['word']

    return verb, subject

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الفعل والفاعل العربي")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject = analyze_verb_subject(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)

if __name__ == "__main__":
    main()
