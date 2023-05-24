import streamlit as st
from pyarabic import araby

def analyze_sentence(sentence):
    # تجهيز الجملة وتحليلها
    normalized_sentence = araby.strip_tashkeel(sentence)
    words = araby.tokenize(normalized_sentence)

    # استخراج الفعل والفاعل
    verb = None
    subject = None

    for i in range(len(words)):
        word = words[i]
        if araby.is_verb(word):
            verb = word
            if i > 0 and araby.is_noun(words[i - 1]):
                subject = words[i - 1]
            break

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
