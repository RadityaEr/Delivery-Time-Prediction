import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "ridge_pipeline.joblib"))

def predict_delivery_time(inputs: dict) -> float:
    # Ensure correct data types
    inputs = {
        "Traffic_Level": str(inputs["Traffic_Level"]),
        "Time_of_Day": str(inputs["Time_of_Day"]),
        "Weather": str(inputs["Weather"]),
        "Vehicle_Type": str(inputs["Vehicle_Type"]),
        "Distance_km": float(inputs["Distance_km"]),
        "Preparation_Time_min": float(inputs["Preparation_Time_min"]),
        "Courier_Experience_yrs": float(inputs["Courier_Experience_yrs"])
    }

    X_input = pd.DataFrame([inputs])
    prediction = model.predict(X_input)[0]
    return prediction
