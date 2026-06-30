from src.core.intelligence_engine import analyze_founder
from src.core.recommendation_engine import generate_recommendations


def build_ai_context(founder):

    intelligence = analyze_founder(founder)

    recommendations = generate_recommendations(founder)

    return {

        "intelligence": intelligence,

        "recommendations": recommendations

    }