import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from PIL import Image

# Load model and labels
model = tf.keras.models.load_model('traffic_signs_model.h5')
labels = pd.read_csv('labels.csv')

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Traffic Signs Classification")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Resize image and preprocess
    image = image.resize((30, 30))
    image = np.array(image)
    image = image/255.0
    image = image.reshape(1, 30, 30, 3)

    # Make prediction
    prediction = model.predict([image])
    prediction = np.argmax(prediction)

    # Display label
    st.write("")
    st.write("Classifying...")
    label = labels.loc[prediction, 'SignName']
    st.success(f"The traffic sign is {label}.")
