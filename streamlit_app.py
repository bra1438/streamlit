import streamlit as st
import nltk
from nltk.tag import tashaphyne

def pos_tag_arabic(text):
    # تحميل قاموس الكلمات العربية
    nltk.download("tashaphyne")
    
    # تقسيم النص إلى كلمات منفردة
    words = nltk.word_tokenize(text)
    
    # إجراء POS tagging للنص العربي
    pos_tags = tashaphyne.pos_tag(words)
    
    return pos_tags

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحديد أجزاء الكلام في النص العربي")
    text = st.text_area("أدخل النص:")
    
    if text:
        pos_tags = pos_tag_arabic(text)
        
        st.write("نتائج تحديد أجزاء الكلام:")
        for word, pos_tag in pos_tags:
            st.write(f"{word}: {pos_tag}")

if __name__ == "__main__":
    main()
