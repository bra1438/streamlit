import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Load data and labels
data = []
labels = []
for i in range(43):
    path = 'Data/train/{0}/'.format(i)
    Class=os.listdir(path)
    for a in Class:
        try:
            # Load and resize image
            image = Image.open(path + a)
            image = image.resize((30,30))
            image = np.array(image)
            
            # Append image and label to list
            data.append(image)
            labels.append(i)
        
        except Exception as e:
            print(e)

# Convert data and labels to array
data = np.array(data)
labels = np.array(labels)

# Binarize labels
lb = LabelBinarizer()
labels = lb.fit_transform(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train Support Vector Classifier
clf = SVC(kernel='linear', probability=True)
clf.fit(X_train.reshape(X_train.shape[0], 30*30*3), np.argmax(y_train, axis=1))

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
    image = image.reshape(1, 30*30*3)

    # Make prediction
    prediction = clf.predict(image)
    label = lb.inverse_transform(prediction)

    # Display label
    st.write("")
    st.write("Classifying...")
    st.success(f"The traffic sign is {label[0]}.")

# Display sample images for testing
st.write("")
st.write("")
st.write("Sample Images for Testing")

images_dir = 'Data/test'
images_list = os.listdir(images_dir)
for img_path in images_list:
    img = Image.open(os.path.join(images_dir, img_path))
    st.image(img, caption=img_path, use_column_width=True)
    
    img = img.resize((30*30*3))
    img = np.array(img)
    
    prediction = clf.predict(img.reshape(1, 30*30*3))
    label = lb.inverse_transform(prediction)
    st.write(f"Prediction for {img_path}: {label[0]}.")
