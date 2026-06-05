import streamlit as st
import pandas as pd
import joblib

# Load saved pipeline/model
pipeline = joblib.load("flight_price_pipeline.pkl")

# App Title
st.title("✈️ Flight Ticket Price Prediction")

st.write("Enter flight details below and click Predict.")

# User Inputs
airline = st.selectbox(
    "Airline",
    ["IndiGo", "Air India", "SpiceJet", "Jet Airways"]
)

source = st.selectbox(
    "Source",
    ["Delhi", "Mumbai", "Kolkata", "Chennai"]
)

destination = st.selectbox(
    "Destination",
    ["Cochin", "Delhi", "Hyderabad", "Bangalore"]
)

duration = st.number_input(
    "Duration (Minutes)",
    min_value=30,
    value=120
)

stops = st.selectbox(
    "Total Stops",
    [0, 1, 2, 3]
)

journey_day = st.slider(
    "Journey Day",
    1, 31, 15
)

journey_month = st.slider(
    "Journey Month",
    1, 12, 6
)

# Predict Button
if st.button("Predict Flight Price"):

    input_data = pd.DataFrame({
        "Airline": [airline],
        "Source": [source],
        "Destination": [destination],
        "Total_Stops": [stops],
        "Duration_Mins": [duration],
        "Journey_Day": [journey_day],
        "Journey_Month": [journey_month]
    })

    prediction = pipeline.predict(input_data)

    st.success(
        f"Predicted Flight Ticket Price: ₹{prediction[0]:,.2f}"
    )