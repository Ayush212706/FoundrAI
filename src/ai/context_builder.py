from src.services.memory_service import load_memory


def build_context(user, founder_data, question):

    memory = load_memory(user.username)

    context = f"""
==============================
FOUNDER PROFILE
==============================

Name: {user.username}

Startup: {user.startup_name}

Industry: {user.industry}

==============================
CURRENT ASSESSMENT
==============================

Founder Score: {founder_data.get("score")}

Budget: ₹{founder_data.get("budget")}

Team Size: {founder_data.get("team_size")}

Stage: {founder_data.get("startup_stage")}

Programming: {founder_data.get("programming")}/10

Marketing: {founder_data.get("marketing")}/10

Finance: {founder_data.get("finance")}/10

Leadership: {founder_data.get("leadership")}/10

Communication: {founder_data.get("communication")}/10

Problem Solving: {founder_data.get("problem_solving")}/10

==============================
MEMORY
==============================

Goals:

{memory["goals"]}

Timeline:

{memory["timeline"]}

Decisions:

{memory["decisions"]}

Notes:

{memory["notes"]}

==============================
FOUNDER QUESTION
==============================

{question}
"""

    return context