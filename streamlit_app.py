import streamlit as st
from pyarabic.araby import is_arabicrange
from pyarabic.araby import strip_tashkeel
from pyarabic.araby import is_tashkeel
from pyarabic.araby import simplify_tashkeel
from pyarabic.araby import is_arabicletter
from pyarabic.araby import is_arabicsymbol

def arabic_syntax():
    st.title("تحليل واعراب الجمل العربية")

    sentence = st.text_input("أدخل الجملة العربية:")

    if sentence:
        # تقوم بتنظيف الجملة من الأشكال الزائدة
        clean_sentence = strip_tashkeel(sentence)

        # قم بعمل الاعراب على الجملة المنظفة هنا
        # يمكنك استخدام أي مكتبة أو أداة لتنفيذ عملية الاعراب

        # عرض النتائج
        st.subheader("الجملة الأصلية:")
        st.write(sentence)

        st.subheader("الجملة المنظفة:")
        st.write(clean_sentence)

        st.subheader("النتائج:")
        # عرض نتائج عملية الاعراب هنا

arabic_syntax()
