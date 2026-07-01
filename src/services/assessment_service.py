from flask_login import current_user

from src.ai.ai_service import generate_founder_advice
from src.core.intelligence_engine import analyze_founder
from src.ml.predict_model import predict_founder_score

from src.models.database import db
from src.models.assessment import Assessment

from src.services.report_service import generate_report


def process_assessment(form_data):
    """
    Process assessment, save it,
    generate AI advice and PDF report.
    """

    founder_data = {

        "name": current_user.username,

        "age": int(form_data.get("age")),

        "education": form_data.get("education"),

        "occupation": form_data.get("occupation"),

        "budget": int(form_data.get("budget")),

        "team_size": int(form_data.get("team_size")),

        "programming": int(form_data.get("programming")),

        "marketing": int(form_data.get("marketing")),

        "finance": int(form_data.get("finance")),

        "leadership": int(form_data.get("leadership")),

        "communication": int(form_data.get("communication")),

        "problem_solving": int(form_data.get("problem_solving")),

        "risk_tolerance": int(form_data.get("risk_tolerance")),

        "startup_stage": form_data.get("startup_stage")

    }

    # ---------------------------------------
    # ML Prediction
    # ---------------------------------------

    founder_data["score"] = predict_founder_score(
        founder_data
    )

    # ---------------------------------------
    # AI Analysis
    # ---------------------------------------

    founder_data["analysis"] = analyze_founder(
        founder_data
    )

    founder_data["ai_advice"] = generate_founder_advice(
        founder_data,
        current_user
    )

    # ---------------------------------------
    # Save Assessment
    # ---------------------------------------

    assessment = Assessment(

        user_id=current_user.id,

        age=founder_data["age"],

        education=founder_data["education"],

        occupation=founder_data["occupation"],

        startup_stage=founder_data["startup_stage"],

        budget=founder_data["budget"],

        team_size=founder_data["team_size"],

        programming=founder_data["programming"],

        marketing=founder_data["marketing"],

        finance=founder_data["finance"],

        leadership=founder_data["leadership"],

        communication=founder_data["communication"],

        problem_solving=founder_data["problem_solving"],

        risk_tolerance=founder_data["risk_tolerance"],

        founder_score=founder_data["score"],

        ai_advice=founder_data["ai_advice"]

    )

    db.session.add(assessment)

    db.session.commit()

    # ---------------------------------------
    # Generate PDF
    # ---------------------------------------

    assessment.report_path = generate_report(founder_data)

    db.session.commit()

    founder_data["report_path"] = assessment.report_path

    founder_data["assessment_id"] = assessment.id

    return founder_data