# 🌾 AgroVision-AI – Rice Leaf Disease Prediction

## 📌 Project Overview

**AgroVision-AI** is an AI-based web application that uses a **Convolutional Neural Network (CNN)** to identify diseases in rice leaves from uploaded images.

The system allows users to upload a rice leaf image and predicts the corresponding disease class.

## 🎯 Objectives

* Detect rice leaf diseases using deep learning.
* Classify uploaded leaf images into disease categories.
* Provide a simple and user-friendly web interface.
* Help support early identification of rice plant diseases.

## 🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras / tf-keras**
* **CNN (Convolutional Neural Network)**
* **OpenCV**
* **NumPy**
* **Pillow**
* **Flask**
* **HTML**
* **CSS**
* **JavaScript**

## 📂 Project Structure

```text
AgroVision-AI/
│
├── model/
│   └── rice_leaf_disease_cnn.keras
│
├── static/
│
├── templates/
│
├── app.py
├── test_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🤖 Model

The project uses a **CNN image classification model** trained to recognize rice leaf disease categories.

The trained model is saved as:

```text
model/rice_leaf_disease_cnn.keras
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd AgroVision-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## 🧪 Model Testing

To test whether the trained model loads correctly, run:

```bash
python test_model.py
```

A successful result should display:

```text
MODEL LOADED SUCCESSFULLY!
```

## 📊 Project Highlights

* CNN-based image classification
* Rice leaf disease prediction
* Flask web application
* Image upload functionality
* Trained `.keras` model
* Simple and user-friendly interface

## 👩‍💻 Author

**Sahana Benni**

MCA Graduate | Python & Data Science Enthusiast
