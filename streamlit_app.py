import streamlit as st
from pyarabic.araby import vocalized_word
from pyarabic.araby import tokenize
from pyarabic.araby import strip_tashkeel
from pyarabic.madina_corpus import MadinaCorpus

def find_verb_and_subject(sentence):
    tokens = tokenize(sentence)
    madina_corpus = MadinaCorpus()
    
    verb = ""
    subject = ""
    
    for token in tokens:
        if is_arabicrange(token):
            token = strip_tashkeel(token)
            token = vocalized_word(token)
            
            if not verb and madina_corpus.is_verb(token):
                verb = token
            elif not subject and madina_corpus.is_noun(token):
                subject = token
    
    return verb, subject

def main():
    st.title("تطبيق تحديد الفعل والفاعل")

    sentence = st.text_input("أدخل الجملة العربية:")
    if st.button("تحديد"):
        verb, subject = find_verb_and_subject(sentence)
        st.write("الفعل:")
        st.write(verb)
        st.write("الفاعل:")
        st.write(subject)

if __name__ == "__main__":
    main()
