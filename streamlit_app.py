import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

def extract_entities(sentence):
    # تقسيم الجملة إلى كلمات منفردة
    words = word_tokenize(sentence)

    # تحديد الأنواع اللغوية (POS tagging)
    tagged_words = pos_tag(words)

    # التعرف على الكيانات المسماة (Named Entity Recognition)
    entities = ne_chunk(tagged_words)

    # استخراج الفعل والفاعل والمفعول به
    verb = None
    subject = None
    object_ = None

    for entity in entities:
        if hasattr(entity, 'label') and entity.label() == 'ORGANIZATION':
            object_ = ' '.join(word for word, pos in entity.leaves())
        elif hasattr(entity, 'label') and entity.label() == 'PERSON':
            subject = ' '.join(word for word, pos in entity.leaves())
        elif hasattr(entity, 'label') and entity.label() == 'VERB':
            verb = ' '.join(word for word, pos in entity.leaves())

    return verb, subject, object_

def main():
    st.title("Extraction of Verb, Subject, and Object in Arabic Sentence")
    sentence = st.text_input("Enter an Arabic sentence:")

    if sentence:
        verb, subject, object_ = extract_entities(sentence)
        st.write("Verb:", verb)
        st.write("Subject:", subject)
        st.write("Object:", object_)

if __name__ == "__main__":
    main()
