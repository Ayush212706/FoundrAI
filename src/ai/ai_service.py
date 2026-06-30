from src.ai.context_builder import build_context
from src.ai.prompt_builder import build_prompt
from src.ai.ollama_client import ask_ai
from src.core.ai_orchestrator import build_ai_context


def generate_founder_advice(founder_data, user=None):

    # Build structured AI context
    ai_context = build_ai_context(founder_data)

    # Build founder context
    if user is None:
        context = f"""
Founder Name: {founder_data.get("name")}

Startup Stage: {founder_data.get("startup_stage")}

Founder Score: {founder_data.get("score")}

Budget: ₹{founder_data.get("budget")}

Team Size: {founder_data.get("team_size")}

Programming: {founder_data.get("programming")}/10

Marketing: {founder_data.get("marketing")}/10

Finance: {founder_data.get("finance")}/10

Leadership: {founder_data.get("leadership")}/10

Communication: {founder_data.get("communication")}/10

Problem Solving: {founder_data.get("problem_solving")}/10

Success Probability:
{ai_context["intelligence"]["success_probability"]}%

Strengths:
{", ".join(ai_context["intelligence"]["strengths"])}

Weaknesses:
{", ".join(ai_context["intelligence"]["weaknesses"])}

Recommended Startup:
{ai_context["intelligence"]["startup_type"]}

Funding Strategy:
{ai_context["intelligence"]["funding"]}

Hiring Advice:
{", ".join(ai_context["recommendations"]["hiring"])}

Learning Resources:
{", ".join(ai_context["recommendations"]["learning"])}

Recommendations:
{", ".join(ai_context["recommendations"]["recommendations"])}
"""
    else:
        context = build_context(user, founder_data, "")

    prompt = build_prompt(context)

    return ask_ai(prompt)