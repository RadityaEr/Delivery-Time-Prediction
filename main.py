import streamlit as st
from delivery_predict import predict_delivery_time

def map_hour_to_time_of_day(hour):
    hour = int(hour)
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

st.set_page_config(page_title="Delivery Time Prediction", layout="centered", page_icon="🚚")
st.title("🚚 Predict Delivery Time")

with st.form("prediction_form"):
    st.subheader("Enter Delivery Details")

    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    time_of_day_hour = st.slider("Time of Day (24h)", 0, 23, 12)
    weather = st.selectbox("Weather Condition", ["Clear", "Foggy", "Rainy", "Snowy", "Windy"])
    vehicle = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])
    distance = st.number_input("Distance (km)", min_value=0.1, step=0.1)
    prep_time = st.number_input("Preparation Time (minutes)", min_value=0, step=1)
    experience = st.slider("Courier Experience (years)", 0, 20, 1)

    submitted = st.form_submit_button("Predict Delivery Time")

if submitted:
    input_dict = {
        "Traffic_Level": str(traffic),
        "Time_of_Day": map_hour_to_time_of_day(time_of_day_hour),  # ✅ FIXED HERE
        "Weather": str(weather),
        "Vehicle_Type": str(vehicle),
        "Distance_km": float(distance),
        "Preparation_Time_min": float(prep_time),
        "Courier_Experience_yrs": float(experience)
    }

    try:
        prediction = predict_delivery_time(input_dict)
        st.success(f"⏱️ Estimated Delivery Time: {prediction:.2f} minutes")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
