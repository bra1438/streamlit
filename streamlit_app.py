import speech_recognition as sr
import streamlit as st

def speech_recognition():
    # Create a recognizer object
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        
        # Prompt the user to say something
        st.write("Say something!")
        
        # Listen for speech input
        audio = r.listen(source)
        
    # Use Google's speech recognition API to transcribe the speech
    try:
        text = r.recognize_google(audio)
        st.write("You said: ", text)
        
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand what you said.")
        
    except sr.RequestError as e:
        st.write("Sorry, something went wrong with the speech recognition service.")
        
# Create a Streamlit application
def app():
    st.title("Speech Recognition")

    # Call the speech_recognition function on button click
    if st.button("Speak"):
        speech_recognition()

# Run the Streamlit application
if __name__ == "__main__":
    app()
