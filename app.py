import streamlit as st
import numpy as np
import pickle

# Load the saved Logistic Regression model
model = pickle.load(open('logistic_regression.pkl', 'rb'))

# Title
st.title("🫀 Heart Disease Prediction")
st.write("""
**This web app predicts whether a person has heart disease or not 
based on their health parameters.**
""")

# --- User Inputs ---
st.header("Enter Patient Details: ")

age = st.number_input("**Enter your Age:**", min_value=1, max_value=120, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

cp = st.selectbox("Your Chest Pain Type:",
                  ["0: Typical Angina", "1: Atypical Angina", "2: Non-anginal Pain", "3: Asymptomatic"])
cp = int(cp.split(":")[0])

trestbps = st.number_input("Enter your Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Your Resting ECG Results",
                       ["0: Normal", "1: ST-T wave abnormality", "2: Left ventricular hypertrophy"])
restecg = int(restecg.split(":")[0])

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

slope = st.selectbox("Slope of Peak Exercise ST Segment", ["0: Upsloping", "1: Flat", "2: Downsloping"])
slope = int(slope.split(":")[0])

ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)

thal = st.selectbox("Thalassemia Type", ["1: Normal", "2: Fixed Defect", "3: Reversible Defect"])
thal = int(thal.split(":")[0])

# --- Prediction ---
if st.button("Predict"):
    # Convert inputs to numpy array
    input_data = np.array([[age, gender, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.header("⚠️ Patient is at **risk of Heart Disease**.")
    else:
        st.header("✅ Patient is **Healthy**.")

# Footer
st.write("---")
st.caption("**Disclaimer:** The predictions made by this tool are for educational purposes only and should not replace professional medical consultation.")