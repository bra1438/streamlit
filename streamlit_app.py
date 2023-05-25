import streamlit as st
import pyarabic.araby as araby
import buckwalter

def analyze_sentence(sentence):
    # تحليل الجملة إلى كلمات منفردة
    words = araby.tokenize(sentence)

    # إعادة ترميز الكلمات إلى ترميز بوكوالتر
    buckwalter_words = [buckwalter.transliterate(word) for word in words]

    # استخراج الفعل والفاعل
    verb = None
    subject = None

    for i, word in enumerate(buckwalter_words):
        # التحقق مما إذا كانت الكلمة فعلًا
        if 'V' in word:
            verb = words[i]
        # التحقق مما إذا كانت الكلمة فاعلًا
        elif 'N' in word:
            subject = words[i]

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
