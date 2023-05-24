import streamlit as st
import pyarabic.araby as araby

def ta3reeb(word):
    ta3reeb_word = araby.tokenize(word)[0]
    return ta3reeb_word

# تكوين واجهة المستخدم باستخدام Streamlit
st.title("تعريب الكلمة")

word = st.text_input("أدخل الكلمة:")
if st.button("تعريب"):
    if word:
        ta3reeb_word = ta3reeb(word)
        st.success(f"الكلمة المعربة: {ta3reeb_word}")
    else:
        st.warning("الرجاء إدخال كلمة.")

