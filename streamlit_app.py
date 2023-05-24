import streamlit as st
import pyarabic.araby as araby

def analyze_sentence(sentence):
    # تحليل الجملة لاستخراج الفعل والفاعل
    words = araby.tokenize(sentence)
    verb = None
    subject = None

    for i in range(len(words)):
        if araby.is_arabicrange(words[i]):
            if araby.vocalized_verb(words[i]):
                verb = words[i]
                if i > 0 and araby.is_arabicrange(words[i-1]):
                    subject = words[i-1]
                elif i > 1 and araby.is_arabicrange(words[i-2]):
                    subject = words[i-2]
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
