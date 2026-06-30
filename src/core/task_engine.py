from datetime import datetime


def generate_timeline(memory):

    timeline = []

    for assessment in memory.get("assessments", []):

        timeline.append({

            "date": assessment["date"],

            "title": "Founder Assessment",

            "description": f'Founder Score: {assessment["score"]}'

        })

    for goal in memory.get("goals", []):

        timeline.append({

            "date": datetime.now().strftime("%Y-%m-%d"),

            "title": "Goal Added",

            "description": goal

        })

    for decision in memory.get("decisions", []):

        timeline.append({

            "date": datetime.now().strftime("%Y-%m-%d"),

            "title": "Decision",

            "description": decision

        })

    for note in memory.get("notes", []):

        timeline.append({

            "date": datetime.now().strftime("%Y-%m-%d"),

            "title": "Founder Note",

            "description": note

        })

    timeline = sorted(

        timeline,

        key=lambda x: x["date"],

        reverse=True

    )

    return timeline