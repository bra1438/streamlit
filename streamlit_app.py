import streamlit as st
import pyarabic.araby as araby

def analyze_sentence(sentence):
    # تحليل الجملة إلى كلمات منفردة
    words = araby.tokenize(sentence)

    # استخراج إعراب الجملة
    analysis = araby.guess_pos(words)

    # استخراج الفعل والفاعل
    verb = None
    subject = None

    for word, pos in analysis:
        if pos == "verb":
            verb = word
        elif pos == "noun":
            subject = word

    return verb, subject

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject = analyze_sentence(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)

if __name__ == "__main__":
    main()
