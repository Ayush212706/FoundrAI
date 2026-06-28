from src.core.founder_score import calculate_founder_score


def process_assessment(form_data):

    founder_data = {

        "name": form_data.get("name"),

        "age": form_data.get("age"),

        "education": form_data.get("education"),

        "occupation": form_data.get("occupation")

    }

    founder_data["score"] = calculate_founder_score(founder_data)

    print("\n========== Founder Assessment ==========")

    for key, value in founder_data.items():

        print(f"{key.title():12}: {value}")

    print("========================================\n")

    return founder_data