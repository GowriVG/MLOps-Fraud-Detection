# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import dump

# Load the dataset
df = pd.read_csv("creditcard.csv")

# Separate features and labels
X = df.drop(columns=["Class"])
y = df["Class"]

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Train model
model = RandomForestClassifier(n_estimators=50, max_depth=8, n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

# Save the trained model and scaler
dump(model, "model.joblib")
dump(scaler, "scaler.joblib")

print("Fraud Detection Model trained and saved successfully!")
