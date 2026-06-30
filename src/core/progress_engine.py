from datetime import datetime


def _safe_value(founder, key, default=0):
    """Safely retrieve numeric values from founder data."""
    try:
        return int(founder.get(key, default))
    except (ValueError, TypeError):
        return default


def calculate_progress(founder):
    """
    Calculates overall founder progress, startup readiness,
    strengths, weaknesses, and personalized recommendations.
    """

    scores = {
        "Technical": _safe_value(founder, "programming"),
        "Marketing": _safe_value(founder, "marketing"),
        "Finance": _safe_value(founder, "finance"),
        "Leadership": _safe_value(founder, "leadership"),
        "Communication": _safe_value(founder, "communication"),
        "Problem Solving": _safe_value(founder, "problem_solving"),
        "Risk Tolerance": _safe_value(founder, "risk_tolerance"),
    }

    overall_score = round(sum(scores.values()) / len(scores), 2)
    overall_progress = round(overall_score * 10, 2)

    # --------------------------------------------------
    # Founder Level
    # --------------------------------------------------

    if overall_score >= 9:
        founder_level = "Elite Founder"

    elif overall_score >= 8:
        founder_level = "Excellent"

    elif overall_score >= 6.5:
        founder_level = "Good"

    elif overall_score >= 5:
        founder_level = "Average"

    else:
        founder_level = "Needs Improvement"

    # --------------------------------------------------
    # Startup Health
    # --------------------------------------------------

    startup_health = {}

    for skill, value in scores.items():

        if value >= 8:
            status = "Healthy"

        elif value >= 5:
            status = "Moderate"

        else:
            status = "Needs Work"

        startup_health[skill] = status

    # --------------------------------------------------
    # Startup Stage Guidance
    # --------------------------------------------------

    stage = founder.get("startup_stage", "Idea")

    milestones = {
        "Idea": "Validate your idea with at least 20 potential users.",
        "MVP": "Acquire your first 100 active users.",
        "Growth": "Optimize revenue and prepare for scaling.",
        "Scaling": "Build repeatable systems and expand the team."
    }

    next_milestone = milestones.get(
        stage,
        "Continue improving your startup."
    )

    # --------------------------------------------------
    # Strong & Weak Skills
    # --------------------------------------------------

    strong_skills = [
        skill
        for skill, score in scores.items()
        if score >= 8
    ]

    moderate_skills = [
        skill
        for skill, score in scores.items()
        if 5 <= score < 8
    ]

    weak_skills = [
        skill
        for skill, score in scores.items()
        if score < 5
    ]

    # --------------------------------------------------
    # Readiness Metrics
    # --------------------------------------------------

    technical_readiness = round(
        (scores["Technical"] + scores["Problem Solving"]) / 2 * 10,
        2
    )

    business_readiness = round(
        (scores["Marketing"] + scores["Finance"]) / 2 * 10,
        2
    )

    leadership_readiness = round(
        (scores["Leadership"] + scores["Communication"]) / 2 * 10,
        2
    )

    execution_readiness = round(
        (
            technical_readiness +
            business_readiness +
            leadership_readiness
        ) / 3,
        2
    )

    # --------------------------------------------------
    # AI Recommendations
    # --------------------------------------------------

    recommendations = []

    if scores["Technical"] < 6:
        recommendations.append(
            "Improve technical skills by building real-world projects."
        )

    if scores["Marketing"] < 6:
        recommendations.append(
            "Focus on customer acquisition and digital marketing."
        )

    if scores["Finance"] < 6:
        recommendations.append(
            "Learn startup budgeting, pricing, and financial planning."
        )

    if scores["Leadership"] < 6:
        recommendations.append(
            "Develop leadership through collaboration and decision making."
        )

    if scores["Communication"] < 6:
        recommendations.append(
            "Practice pitching and communicating ideas clearly."
        )

    if scores["Risk Tolerance"] < 5:
        recommendations.append(
            "Work on making data-driven decisions with calculated risks."
        )

    if not recommendations:
        recommendations.append(
            "Maintain momentum and continue executing consistently."
        )

    # --------------------------------------------------
    # Suggested Next Actions
    # --------------------------------------------------

    next_actions = []

    if stage == "Idea":
        next_actions.extend([
            "Interview potential users.",
            "Validate the core problem.",
            "Create a simple MVP roadmap."
        ])

    elif stage == "MVP":
        next_actions.extend([
            "Launch to early adopters.",
            "Collect product feedback.",
            "Measure retention."
        ])

    elif stage == "Growth":
        next_actions.extend([
            "Increase customer acquisition.",
            "Improve revenue channels.",
            "Prepare hiring strategy."
        ])

    elif stage == "Scaling":
        next_actions.extend([
            "Build internal systems.",
            "Delegate responsibilities.",
            "Optimize operations."
        ])

    # --------------------------------------------------
    # Progress Summary
    # --------------------------------------------------

    progress_summary = (
        f"You are currently operating at {overall_progress:.1f}% "
        f"overall founder readiness with a '{founder_level}' profile."
    )

    # --------------------------------------------------
    # Return Result
    # --------------------------------------------------

    return {

        "overall_progress": overall_progress,

        "overall_score": overall_score,

        "founder_level": founder_level,

        "startup_stage": stage,

        "startup_health": startup_health,

        "technical_readiness": technical_readiness,

        "business_readiness": business_readiness,

        "leadership_readiness": leadership_readiness,

        "execution_readiness": execution_readiness,

        "next_milestone": next_milestone,

        "strong_skills": strong_skills,

        "moderate_skills": moderate_skills,

        "weak_skills": weak_skills,

        "recommendations": recommendations,

        "next_actions": next_actions,

        "summary": progress_summary,

        "generated_at": datetime.now().strftime("%d %B %Y %H:%M")

    }