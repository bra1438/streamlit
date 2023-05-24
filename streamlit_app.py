import streamlit as st
from pyarabic.araby import Tokenizer, is_arabicrange

def extract_verb_subject(sentence):
    tokenizer = Tokenizer()

    # تقسيم الجملة إلى كلمات منفردة
    words = tokenizer.tokenize(sentence)

    verb = None
    subject = None

    # استخراج الفعل والفاعل
    for i in range(len(words)):
        if is_arabicrange(words[i]):
            if i+1 < len(words) and words[i+1] == 'من':
                subject = words[i]
            else:
                verb = words[i]
    
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
