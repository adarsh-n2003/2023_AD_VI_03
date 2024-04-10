### **Breast Cancer Prediction using CNN**

This repository contains code for a breast cancer prediction project, utilizing convolutional neural networks (CNNs) to classify breast tissue images as either normal or showing signs of a tumor.

### **Dataset**

The dataset used in this project is obtained from Kaggle and consists of breast histopathology images. The dataset contains images of breast tissue samples at 400x magnification, with each image labeled as either normal or containing a tumor.

After downloading the dataset from the Kaggle link, please ensure to organize the data into two directories: "normal" and "tumor". This organization is necessary for the model training process.

You can access the dataset on Kaggle via the following link: [BreakHis 400x Dataset](https://www.kaggle.com/datasets/forderation/breakhis-400x)

### **Project Overview**

The project involves the following steps:

1. **Model Training:** Developing a CNN model using TensorFlow/Keras to learn features from breast tissue images and classify them into normal or tumor categories.
2. **User Interface Development:** Creating a user-friendly interface using Streamlit to allow users to upload breast tissue images for prediction.
3. **Model Deployment:** Deploying the trained CNN model within the Streamlit application to provide real-time breast cancer prediction.

### **Files**

- **`ml_model.ipynb`**: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.
- **`breast_cancer_prediction.py`**: Python script implementing the user interface and model deployment using Streamlit.
- **`bcd_model.h5`**: Trained CNN model file.

### **Usage**

To use the code in this repository:

1. Download the dataset from the provided Kaggle link.
2. Organize the dataset into two directories: "normal" and "tumor".
3. Train the CNN model using the code provided in the **`ml_model.ipynb`** notebook.
4. After training the model, save it as **`bcd_model.h5`**.
5. Run the **`breast_cancer_prediction.py`** script to execute the Streamlit application.
6. Upload breast tissue images for prediction and view the classification results.

### **Requirements**

The project code requires the following Python libraries:

- streamlit
- tensorflow
- numpy
- PIL

You can install these dependencies using pip:

```bash
bashCopy code
pip install streamlit tensorflow numpy pillow
```

### **Contributors**

- [Adarsh Nashine](https://github.com/adarsh-n2003)
- [Anuj Tirole](https://github.com/anujtirole)
- [Prabal Singh](https://github.com/Prabalsing)
- [Surendra Singh Koranga](https://github.com/Surendrasingh6289)

### **Acknowledgments**

- The dataset used in this project is sourced from Kaggle.
- Special thanks to the contributors and maintainers of the dataset for making it publicly available for research purposes.

### **License**

This project is licensed under the MIT License. Feel free to use the code for educational and commercial purposes.
