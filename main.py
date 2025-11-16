# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import time

# Initialize FastAPI
# Initialize FastAPIhgcjhcj
# app = FastAPI(title="Real-Time Fraud Detection API", version="2.0")
app = FastAPI(
    title="Real-Time Fraud Detection API",
    version="2.1"  
)

# Load model and scaler
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

# Define the input structure
class TransactionInput(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float
    Time: float

@app.get("/")
def root():
    return {"message": "Welcome to the 100ms Real-Time Fraud Detection API", "version": "2.1"}


@app.post("/predict")
def predict_fraud(data: TransactionInput):
    start_time = time.time()

    # Convert input to array
    features = np.array([[getattr(data, f) for f in data.__fields__.keys()]])
    
    # Scale input
    scaled_features = scaler.transform(features)

    # Predict
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]
    label = "Fraudulent" if prediction == 1 else "Legitimate"

    # Calculate latency
    end_time = time.time()
    latency_ms = round((end_time - start_time) * 1000, 3)

    return {
        "transaction_status": label,
        "fraud_probability": round(float(probability), 4),
        "response_time_ms": latency_ms
    }
