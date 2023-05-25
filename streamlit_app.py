import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import arabic_reshaper
from bidi.algorithm import get_display
from pyarabic.araby import strip_tashkeel
from pyarabic import araby

def pos_tag_arabic(sentence):
    # تفريق الجملة إلى كلمات منفردة
    words = word_tokenize(sentence)

    # إجراء POS tagging باستخدام NLTK
    tagged_words = nltk.pos_tag(words)

    # إعادة تشكيل الكلمات العربية
    reshaped_words = [get_display(arabic_reshaper.reshape(word)) for word, _ in tagged_words]

    # إزالة التشكيل من الكلمات
    stripped_words = [strip_tashkeel(word) for word in reshaped_words]

    # ترجيع الكلمات والتاغات
    tags = [tag for _, tag in tagged_words]
    return stripped_words, tags

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل POS للجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        words, tags = pos_tag_arabic(sentence)
        for word, tag in zip(words, tags):
            st.write("الكلمة:", word)
            st.write("التاغ:", tag)
            st.write("---")

if __name__ == "__main__":
    main()
