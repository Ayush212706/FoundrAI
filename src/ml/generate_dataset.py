import random
import pandas as pd

education_levels = [
    "School",
    "Diploma",
    "Bachelor's Degree",
    "Master's Degree",
    "PhD"
]

startup_stages = [
    "Idea",
    "Prototype",
    "MVP",
    "Early Revenue",
    "Scaling"
]

rows = []

for _ in range(1000):

    age = random.randint(18, 50)

    education = random.choice(education_levels)

    budget = random.randint(10000, 5000000)

    team_size = random.randint(1, 20)

    programming = random.randint(1, 10)
    marketing = random.randint(1, 10)
    finance = random.randint(1, 10)
    leadership = random.randint(1, 10)
    risk_tolerance = random.randint(1, 10)
    communication = random.randint(1, 10)
    problem_solving = random.randint(1, 10)

    startup_stage = random.choice(startup_stages)

    score = (
        30
        + programming * 2
        + marketing * 2
        + finance
        + leadership * 2
        + communication
        + problem_solving * 2
        + risk_tolerance
        + min(team_size, 5)
    )

    score = max(40, min(score, 100))

    rows.append([
        age,
        education,
        budget,
        team_size,
        programming,
        marketing,
        finance,
        leadership,
        risk_tolerance,
        communication,
        problem_solving,
        startup_stage,
        score
    ])

columns = [
    "age",
    "education",
    "budget",
    "team_size",
    "programming",
    "marketing",
    "finance",
    "leadership",
    "risk_tolerance",
    "communication",
    "problem_solving",
    "startup_stage",
    "score"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "data/training/founder_dataset.csv",
    index=False
)

print("Dataset generated successfully!")