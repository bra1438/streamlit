import streamlit as st
import pyarabic.araby as araby

def ta3reeb(word):
    ta3reeb_word = araby.tokenize(word)[0]
    return ta3reeb_word

# إعداد واجهة المستخدم باستخدام Streamlit
st.title("تعريب جملة عربية")
sentence = st.text_input("أدخل الجملة:")

if st.button("تعريب"):
    words = sentence.split()
    ta3reeb_sentence = []
    for word in words:
        ta3reeb_word = ta3reeb(word)
        ta3reeb_sentence.append(ta3reeb_word)
    ta3reeb_text = " ".join(ta3reeb_sentence)
    st.write("الجملة المعربة:", ta3reeb_text)
