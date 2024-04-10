import os
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Get the path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
model_path = os.path.join(current_directory, 'bcd_model.h5')
model = load_model(model_path)

# Define allowed extensions for file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def main():
    st.title('Breast Cancer Detection')
    
    # File upload
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        if allowed_file(uploaded_file.name):
            # Preprocess the image
            img = load_img(uploaded_file, target_size=(150, 150))
            img = img_to_array(img)
            img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
            img /= 255.

            # Make prediction
            prediction = model.predict(img)

            # Interpret the prediction
            if prediction < 0.5:
                result = 'Normal'
                color = 'green'
            elif prediction > 0.5:
                result = 'Tumor'
                color = 'red'
            else:
                result = 'Unpredictable'
                color = 'orange'

            # Display result with highlight
            st.write(f'Prediction: <span style="color:{color}">{result}</span>', unsafe_allow_html=True)
        else:
            st.error("Invalid file format. Please upload an image file.")

if __name__ == '__main__':
    main()
