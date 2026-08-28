import tensorflow as tf
import tf_keras

print("TensorFlow:", tf.__version__)
print("Testing model...")

model = tf_keras.models.load_model(
    "model/rice_leaf_disease_cnn.keras",
    compile=False
)

print("MODEL LOADED SUCCESSFULLY!")
print(model.summary())