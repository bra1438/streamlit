import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Load model and labels
model = ... # load your trained model
labels = pd.read_csv('labels.csv')

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Traffic Sign Classifier")

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
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1)

    # Display label
    st.write("")
    st.write("Classifying...")
    label = labels.loc[prediction[0], 'SignName']
    st.success(f"The traffic sign is {label}.")

# Display sample images for testing
st.write("")
st.write("")
st.write("Sample Images for Testing")

sample_imgs = ['stop.jpg', 'speed_limit.jpg', 'yield.jpg']
for img_path in sample_imgs:
    img = Image.open(img_path)
    st.image(img, caption=img_path, use_column_width=True)
    
    img = img.resize((30, 30))
    img = np.array(img)
    img = img/255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    prediction = np.argmax(prediction, axis=1)

    label = labels.loc[prediction[0], 'SignName']
    st.write(f"Prediction for {img_path}: {label}.")
