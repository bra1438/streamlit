import streamlit as st
import pyarabic.araby as araby

def ta3reeb(sentence):
    words = sentence.split()
    ta3reeb_sentence = []
    for word in words:
        ta3reeb_word = araby.tokenize(word)[0]
        ta3reeb_sentence.append(ta3reeb_word)
    return ' '.join(ta3reeb_sentence)

# تهيئة واجهة Streamlit
st.title("تعريب جملة عربية")
sentence = st.text_input("أدخل الجملة:")
if sentence:
    ta3reeb_sentence = ta3reeb(sentence)
    st.write("الجملة المعربة:", ta3reeb_sentence)
