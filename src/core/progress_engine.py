from datetime import datetime


def calculate_progress(founder):

    scores = {
        "technical": founder["programming"],
        "marketing": founder["marketing"],
        "finance": founder["finance"],
        "leadership": founder["leadership"],
        "communication": founder["communication"],
        "problem_solving": founder["problem_solving"],
        "risk": founder["risk_tolerance"]
    }

    overall = sum(scores.values()) / len(scores)

    if overall >= 8:
        level = "Excellent"

    elif overall >= 6:
        level = "Good"

    elif overall >= 4:
        level = "Average"

    else:
        level = "Needs Improvement"

    startup_health = {

        "Product": "Healthy" if founder["programming"] >= 7 else "Needs Work",

        "Marketing": "Healthy" if founder["marketing"] >= 7 else "Needs Work",

        "Finance": "Healthy" if founder["finance"] >= 7 else "Needs Work",

        "Leadership": "Healthy" if founder["leadership"] >= 7 else "Needs Work"

    }

    if founder["startup_stage"] == "Idea":

        next_milestone = "Validate your idea with at least 20 potential users."

    elif founder["startup_stage"] == "MVP":

        next_milestone = "Acquire your first 100 active users."

    elif founder["startup_stage"] == "Growth":

        next_milestone = "Optimize revenue and prepare for scaling."

    else:

        next_milestone = "Continue improving your startup."

    weak_skills = []

    for skill, score in scores.items():

        if score < 5:
            weak_skills.append(skill.title())

    strong_skills = []

    for skill, score in scores.items():

        if score >= 8:
            strong_skills.append(skill.title())

    return {

        "overall_progress": round(overall * 10, 2),

        "founder_level": level,

        "startup_health": startup_health,

        "next_milestone": next_milestone,

        "weak_skills": weak_skills,

        "strong_skills": strong_skills,

        "generated_at": datetime.now().strftime("%d %B %Y %H:%M")

    }