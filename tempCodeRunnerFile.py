# delivery_predict.py
import joblib
import json
import numpy as np
import pandas as pd

# Load model and feature names once
model = joblib.load("ridge_pipeline.joblib")

with open("feature_names.json", "r") as f:
    feature_names = json.load(f)

def predict_delivery_time(inputs: dict) -> float:
    # Convert inputs to DataFrame with correct column order
    X_input = pd.DataFrame([inputs], columns=feature_names)
    prediction = model.predict(X_input)[0]
    return prediction
