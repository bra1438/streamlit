import streamlit as st
from pyarabic.araby import strip_tashkeel, is_arabicrange

def analyze_sentence(sentence):
    words = sentence.split()
    verb = None
    subject = None
    object = None

    for word in words:
        # التأكد من أن الكلمة تحتوي على حروف عربية فقط
        if is_arabicrange(word):
            # إزالة التشكيل من الكلمة
            word_stripped = strip_tashkeel(word)
            
            # فحص إذا كانت الكلمة فعلاً
            if word_stripped in verb_list:
                verb = word
            # فحص إذا كانت الكلمة فاعلاً
            elif word_stripped in subject_list:
                subject = word
            # فحص إذا كانت الكلمة مفعولاً به
            elif word_stripped in object_list:
                object = word

    return verb, subject, object

# تحميل قوائم الأفعال والفواعل والمفاعيل
verb_list = ["فعل1", "فعل2", "فعل3"]
subject_list = ["فاعل1", "فاعل2", "فاعل3"]
object_list = ["مفعول1", "مفعول2", "مفعول3"]

# تكوين واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل الجملة العربية")
    sentence = st.text_input("أدخل الجملة:")

    if sentence:
        verb, subject, object = analyze_sentence(sentence)
        st.write("الفعل:", verb)
        st.write("الفاعل:", subject)
        st.write("المفعول به:", object)

if __name__ == "__main__":
    main()
