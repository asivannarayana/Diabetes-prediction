from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
# 1. Load the "Brain" and "Translator"
model = joblib.load('models/diabetes_model.pkl')
scaler = joblib.load('models/scaler.pkl')
app = FastAPI(title="Diabetes Prediction API")
# 2. Define the input data format
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running!"}
@app.post("/predict")
def predict(data: PatientData):
    # Convert input to array
    patient_dict = data.dict()
    features = np.array([list(patient_dict.values())])
    # Scale and Predict
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    probability = model.predict_proba(features_scaled)
    return {
        "prediction": int(prediction[0]),
        "probability": float(np.max(probability))
    }
