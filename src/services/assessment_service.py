from src.ai.ai_service import generate_founder_advice
from src.ml.predict_model import predict_founder_score
from src.models.database import db
from src.models.founder import Founder
from src.services.report_service import generate_report
from src.core.intelligence_engine import analyze_founder


def process_assessment(form_data):

    founder_data = {

        "name": form_data.get("name"),

        "age": int(form_data.get("age")),

        "education": form_data.get("education"),

        "occupation": form_data.get("occupation"),

        "budget": int(form_data.get("budget")),

        "team_size": int(form_data.get("team_size")),

        "programming": int(form_data.get("programming")),

        "marketing": int(form_data.get("marketing")),

        "finance": int(form_data.get("finance")),

        "leadership": int(form_data.get("leadership")),

        "risk_tolerance": int(form_data.get("risk_tolerance")),

        "communication": int(form_data.get("communication")),

        "problem_solving": int(form_data.get("problem_solving")),

        "startup_stage": form_data.get("startup_stage")

    }

    # ML Prediction
    founder_data["score"] = predict_founder_score(founder_data)

    # Decision Engine
    founder_data["analysis"] = analyze_founder(founder_data)

    # AI Advice
    founder_data["ai_advice"] = generate_founder_advice(founder_data)

    founder = Founder(
        name=founder_data["name"],
        age=founder_data["age"],
        education=founder_data["education"],
        occupation=founder_data["occupation"],
        score=int(founder_data["score"])
    )

    db.session.add(founder)
    db.session.commit()

    founder_data["report_path"] = generate_report(founder_data)

    return founder_data