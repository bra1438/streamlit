import streamlit as st
import pyarabic.araby as araby

def analyze_sentence(sentence):
    verb = None
    subject = None

    # تفكيك الجملة إلى كلمات
    words = araby.tokenize(sentence)

    # البحث عن الفعل والفاعل
    for i in range(len(words)):
        if araby.is_arabicrange(words[i]):
            # التأكد من أن الكلمة الحالية هي فعل
            if araby.strip_tashkeel(words[i]) in ['فعل', 'مضارع', 'أمر', 'ماضي']:
                verb = words[i]
                # التأكد من أن الكلمة التالية هي فاعل
                if i+1 < len(words) and araby.is_arabicrange(words[i+1]):
                    subject = words[i+1]
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
