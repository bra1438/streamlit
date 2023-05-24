import streamlit as st
import pyarabic.araby as araby

def ta3reeb(sentence):
    words = araby.tokenize(sentence)
    ta3reeb_sentence = ' '.join([araby.ta3reeb(word) for word in words])
    return ta3reeb_sentence

# تكوين واجهة Streamlit
st.title("تعريب جملة عربية")
sentence = st.text_input("أدخل الجملة:")

if sentence:
    ta3reeb_sentence = ta3reeb(sentence)
    st.write("الجملة المعربة:", ta3reeb_sentence)
