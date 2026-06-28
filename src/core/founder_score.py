def calculate_founder_score(data):

    score = 50

    age = int(data.get("age", 0))

    if 18 <= age <= 35:
        score += 10

    education = data.get("education")

    if education == "Bachelor's Degree":
        score += 5

    elif education == "Master's Degree":
        score += 8

    elif education == "PhD":
        score += 10

    return score