import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/training/founder_dataset.csv")

# Encode categorical columns
education_encoder = LabelEncoder()
stage_encoder = LabelEncoder()

df["education"] = education_encoder.fit_transform(df["education"])
df["startup_stage"] = stage_encoder.fit_transform(df["startup_stage"])

# Features
X = df[
    [
        "age",
        "education",
        "budget",
        "team_size",
        "programming",
        "marketing",
        "finance",
        "leadership",
        "risk_tolerance",
        "communication",
        "problem_solving",
        "startup_stage"
    ]
]

# Target
y = df["score"]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save everything
joblib.dump(model, "models/trained_models/founder_model.pkl")
joblib.dump(education_encoder, "models/trained_models/education_encoder.pkl")
joblib.dump(stage_encoder, "models/trained_models/stage_encoder.pkl")

print("✅ New AI model trained successfully!")