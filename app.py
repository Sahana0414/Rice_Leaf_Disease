from flask import Flask, render_template, request
import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)

# ==========================
# Configuration
# ==========================

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load CNN model
model = load_model("model/rice_leaf_disease_cnn.keras")

# Class labels
class_names = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Leaf Smut"
]

# ==========================
# Image Preprocessing
# ==========================

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (224, 224))

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)

    return img

# ==========================
# Routes
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/disease_library")
def disease_library():
    return render_template("disease_library.html")


@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    file = request.files["image"]

    if file.filename == "":
        return "Please select an image."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # ==========================
    # CNN Prediction
    # ==========================

    image = preprocess_image(filepath)

    prediction = model.predict(image)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction)) * 100

    disease = class_names[predicted_index]

    confidence = f"{confidence:.2f}%"

    # ==========================
    # Disease Information
    # ==========================

    if disease == "Brown Spot":

        description = "Brown Spot is a fungal disease caused by Bipolaris oryzae."

        symptoms = [
            "Brown circular spots on leaves",
            "Yellow halo around spots",
            "Leaves become dry"
        ]

        treatment = [
            "Apply recommended fungicide",
            "Improve field drainage",
            "Remove infected leaves"
        ]

    elif disease == "Leaf Smut":

        description = "Leaf Smut is a fungal disease caused by Entyloma oryzae."

        symptoms = [
            "Small black lesions",
            "Dark powdery spots",
            "Reduced plant growth"
        ]

        treatment = [
            "Remove infected leaves",
            "Use fungicide",
            "Maintain field hygiene"
        ]

    else:

        description = "Bacterial Leaf Blight is caused by Xanthomonas oryzae."

        symptoms = [
            "Yellow leaf edges",
            "Leaf wilting",
            "Dry leaf tips"
        ]

        treatment = [
            "Use resistant varieties",
            "Apply bactericide",
            "Avoid excessive nitrogen fertilizer"
        ]

    return render_template(
        "result.html",
        disease=disease,
        confidence=confidence,
        image=file.filename,
        description=description,
        symptoms=symptoms,
        treatment=treatment
    )


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)