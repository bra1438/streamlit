import streamlit as st
import nltk

# تحميل مكونات NLTK اللازمة
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)  # تقسيم الجملة إلى كلمات
    tagged_tokens = nltk.pos_tag(tokens)  # تحديد أنواع الكلمات (Parts-of-Speech)

    verb = ''
    subject = ''
    object = ''

    for token in tagged_tokens:
        if token[1].startswith('V'):  # التحقق مما إذا كانت الكلمة فعلاً
            verb = token[0]
        elif token[1] == 'NNP':  # التحقق مما إذا كانت الكلمة اسماً مفرداً محدداً (الفاعل)
            subject = token[0]
        elif token[1].startswith('N'):  # التحقق مما إذا كانت الكلمة اسماً عاماً (المفعول به)
            object = token[0]

    return verb, subject, object

# تكوين واجهة المستخدم باستخدام Streamlit
st.title("تحليل الجمل")
sentence = st.text_input("أدخل الجملة:")
if sentence:
    verb, subject, object = analyze_sentence(sentence)
    st.write("الفعل:", verb)
    st.write("الفاعل:", subject)
    st.write("المفعول به:", object)
