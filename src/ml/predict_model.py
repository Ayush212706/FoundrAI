import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/trained_models/founder_model.pkl")

education_encoder = joblib.load(
    "models/trained_models/education_encoder.pkl"
)

stage_encoder = joblib.load(
    "models/trained_models/stage_encoder.pkl"
)


def predict_founder_score(data):

    education = education_encoder.transform(
        [data["education"]]
    )[0]

    stage = stage_encoder.transform(
        [data["startup_stage"]]
    )[0]

    input_df = pd.DataFrame([{

        "age": data["age"],
        "education": education,
        "budget": data["budget"],
        "team_size": data["team_size"],
        "programming": data["programming"],
        "marketing": data["marketing"],
        "finance": data["finance"],
        "leadership": data["leadership"],
        "risk_tolerance": data["risk_tolerance"],
        "communication": data["communication"],
        "problem_solving": data["problem_solving"],
        "startup_stage": stage

    }])

    prediction = model.predict(input_df)

    return round(float(prediction[0]), 2)