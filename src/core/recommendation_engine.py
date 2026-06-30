def generate_recommendations(founder):

    recommendations = []

    learning = []

    hiring = []

    budget = {}

    # Marketing

    if founder["marketing"] <= 4:

        recommendations.append(
            "Your marketing skills are below average. Focus on customer acquisition before scaling."
        )

        hiring.append(
            "Hire a Marketing Intern or Freelancer."
        )

        learning.extend([
            "Google Digital Garage - Fundamentals of Digital Marketing",
            "HubSpot Academy - Content Marketing",
            "Meta Blueprint"
        ])

    # Programming

    if founder["programming"] <= 4:

        recommendations.append(
            "Improve technical capability or partner with a technical co-founder."
        )

        hiring.append(
            "Technical Co-founder"
        )

    # Finance

    if founder["finance"] <= 4:

        recommendations.append(
            "Improve startup finance knowledge before raising funding."
        )

        learning.extend([
            "Y Combinator Startup School",
            "Startup Finance by Coursera"
        ])

    # Leadership

    if founder["leadership"] <= 4:

        recommendations.append(
            "Develop leadership skills before expanding your team."
        )

    # Budget

    if founder["budget"] < 300000:

        budget = {
            "Product": "50%",
            "Marketing": "20%",
            "Cloud": "10%",
            "Emergency": "20%"
        }

    else:

        budget = {
            "Product": "40%",
            "Marketing": "30%",
            "Operations": "10%",
            "Cloud": "10%",
            "Emergency": "10%"
        }

    return {

        "recommendations": recommendations,

        "learning": learning,

        "hiring": hiring,

        "budget": budget

    }