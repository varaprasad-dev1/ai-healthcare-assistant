import os
import json
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "skin_model.h5")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")

model = load_model(MODEL_PATH)

with open(LABELS_PATH, "r") as f:
    labels = json.load(f)


def predict_image(image_path):

    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    confidence = round(float(prediction[0][index]) * 100, 2)

    disease = labels[str(index)]

    return disease, confidence