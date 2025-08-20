import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/random_forest.pkl")

st.title("🌾 Crop Yield Prediction System")

# User input fields
rainfall = st.number_input("Rainfall (mm)", min_value=0, max_value=2000, value=800)
temperature = st.number_input("Temperature (°C)", min_value=0, max_value=50, value=28)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=70)
fertilizer = st.number_input("Fertilizer (kg/acre)", min_value=0, max_value=500, value=120)
soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"])

# Encode soil type manually (same as training)
soil_encoded = {
    "Soil_Type_Loamy": 1 if soil_type == "Loamy" else 0,
    "Soil_Type_Sandy": 1 if soil_type == "Sandy" else 0,
}

# Prepare input for model
input_data = {
    "Rainfall": rainfall,
    "Temperature": temperature,
    "Humidity": humidity,
    "Fertilizer": fertilizer,
    "Soil_Type_Loamy": soil_encoded["Soil_Type_Loamy"],
    "Soil_Type_Sandy": soil_encoded["Soil_Type_Sandy"]
}

if st.button("Predict Yield"):
    prediction = model.predict(pd.DataFrame([input_data]))
    st.success(f"✅ Predicted Crop Yield: {prediction[0]:.2f} kg/hectare")
