def analyze_decision(founder):
    """
    Analyze founder data and generate decision insights.
    """

    score = founder.get("score", 0)
    stage = founder.get("startup_stage", "Idea")
    budget = founder.get("budget", 0)
    team_size = founder.get("team_size", 1)

    decision = {
        "overall": "",
        "priority": "",
        "next_step": "",
        "risk": ""
    }

    if score >= 80:
        decision["overall"] = "Excellent founder readiness."
    elif score >= 60:
        decision["overall"] = "Good founder potential."
    else:
        decision["overall"] = "Founder needs improvement."

    if stage == "Idea":
        decision["next_step"] = (
            "Validate your idea with potential customers."
        )
    elif stage == "MVP":
        decision["next_step"] = (
            "Launch MVP and collect user feedback."
        )
    elif stage == "Growth":
        decision["next_step"] = (
            "Focus on scaling and customer acquisition."
        )
    else:
        decision["next_step"] = (
            "Continue improving your startup."
        )

    if budget < 50000:
        decision["priority"] = "Bootstrap"
    elif budget < 500000:
        decision["priority"] = "Early Growth"
    else:
        decision["priority"] = "Scale"

    if team_size <= 2:
        decision["risk"] = "High execution risk due to small team."
    elif team_size <= 5:
        decision["risk"] = "Moderate execution risk."
    else:
        decision["risk"] = "Low execution risk."

    return decision