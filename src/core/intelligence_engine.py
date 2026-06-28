def analyze_founder(founder):

    analysis = {}

    score = founder["score"]

    # ------------------------
    # Success Probability
    # ------------------------

    if score >= 90:
        analysis["success_probability"] = 90

    elif score >= 80:
        analysis["success_probability"] = 80

    elif score >= 70:
        analysis["success_probability"] = 70

    else:
        analysis["success_probability"] = 60

    # ------------------------
    # Strengths
    # ------------------------

    strengths = []

    weaknesses = []

    skills = {
        "Programming": founder["programming"],
        "Marketing": founder["marketing"],
        "Finance": founder["finance"],
        "Leadership": founder["leadership"],
        "Communication": founder["communication"],
        "Problem Solving": founder["problem_solving"]
    }

    for skill, value in skills.items():

        if value >= 8:
            strengths.append(skill)

        elif value <= 4:
            weaknesses.append(skill)

    analysis["strengths"] = strengths

    analysis["weaknesses"] = weaknesses

    # ------------------------
    # Startup Type
    # ------------------------

    if founder["programming"] >= 8:

        analysis["startup_type"] = "AI SaaS"

    elif founder["marketing"] >= 8:

        analysis["startup_type"] = "D2C Brand"

    else:

        analysis["startup_type"] = "Tech Startup"

    # ------------------------
    # Funding Strategy
    # ------------------------

    if founder["budget"] < 500000:

        analysis["funding"] = "Bootstrap"

    else:

        analysis["funding"] = "Angel Investment"

    # ------------------------
    # Team Recommendation
    # ------------------------

    team = ["Founder"]

    if founder["marketing"] < 6:
        team.append("Marketing")

    if founder["programming"] < 6:
        team.append("Developer")

    if founder["finance"] < 6:
        team.append("Finance Advisor")

    analysis["recommended_team"] = team

    # ------------------------
    # Budget Allocation
    # ------------------------

    analysis["budget_plan"] = {

        "Product Development": 40,

        "Marketing": 25,

        "Cloud": 15,

        "Legal": 10,

        "Emergency": 10

    }

    # ------------------------
    # Roadmap
    # ------------------------

    analysis["roadmap"] = [

        "Validate the startup idea",

        "Interview at least 20 target users",

        "Build the MVP",

        "Launch a beta version",

        "Collect user feedback",

        "Improve the product"

    ]

    return analysis