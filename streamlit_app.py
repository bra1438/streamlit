import streamlit as st
import stanza

def pos_tag_arabic(text):
    # Load the Arabic pre-trained POS tagger
    nlp = stanza.Pipeline(lang='ar', processors='pos')

    # Process the text and perform POS tagging
    doc = nlp(text)

    pos_tags = []
    for sentence in doc.sentences:
        for word in sentence.words:
            pos_tags.append((word.text, word.upos))

    return pos_tags

# Configure the Streamlit app
def main():
    st.title("Arabic Part-of-Speech Tagging")
    text = st.text_area("Enter Arabic text:")

    if text:
        pos_tags = pos_tag_arabic(text)
        for word, pos_tag in pos_tags:
            st.write("Word:", word)
            st.write("POS Tag:", pos_tag)
            st.write("---")

if __name__ == "__main__":
    main()
