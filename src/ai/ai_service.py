from src.ai.context_builder import build_context
from src.ai.prompt_builder import build_prompt
from src.ai.gemini_client import ask_ai

from src.core.ai_orchestrator import build_ai_context

from src.services.memory_service import (
    load_memory,
    save_chat,
    add_recommendation
)


def generate_founder_advice(founder_data, user=None):
    """
    Main AI entry point.

    Collects founder information, memory,
    builds AI context, creates the final prompt,
    queries Ollama and stores the conversation.
    """

    # -------------------------------------------------
    # Guest Mode
    # -------------------------------------------------

    if user is None:

        ai_context = build_ai_context(founder_data, {})

        context = f"""
Founder Name:
{founder_data.get("name", "Guest")}

Startup Stage:
{founder_data.get("startup_stage", "Idea")}

Founder Score:
{founder_data.get("score", "N/A")}

Budget:
₹{founder_data.get("budget", "N/A")}

Team Size:
{founder_data.get("team_size", "N/A")}

Programming:
{founder_data.get("programming", 0)}/10

Marketing:
{founder_data.get("marketing", 0)}/10

Finance:
{founder_data.get("finance", 0)}/10

Leadership:
{founder_data.get("leadership", 0)}/10

Communication:
{founder_data.get("communication", 0)}/10

Problem Solving:
{founder_data.get("problem_solving", 0)}/10

Risk Tolerance:
{founder_data.get("risk_tolerance", 0)}/10

====================================================

SUCCESS PROBABILITY

{ai_context["intelligence"].get("success_probability", "N/A")}%

====================================================

RECOMMENDED STARTUP

{ai_context["intelligence"].get("startup_type", "General Startup")}

====================================================

FUNDING STRATEGY

{ai_context["intelligence"].get("funding", "Bootstrap")}

====================================================

STRENGTHS

{", ".join(ai_context["intelligence"].get("strengths", []))}

====================================================

WEAKNESSES

{", ".join(ai_context["intelligence"].get("weaknesses", []))}

====================================================

AI RECOMMENDATIONS

{", ".join(ai_context["recommendations"].get("recommendations", []))}
"""

        prompt = build_prompt(context)

        return ask_ai(prompt)

    # -------------------------------------------------
    # Logged-in Founder
    # -------------------------------------------------

    memory = load_memory(user.username)

    ai_context = build_ai_context(
        founder_data,
        memory
    )

    context = build_context(
        user,
        founder_data,
        ""
    )

    prompt = build_prompt(context)

    answer = ask_ai(prompt)

    # Save conversation
    save_chat(
        user.username,
        "Founder Assessment",
        answer
    )

    # Save recommendation
    add_recommendation(
        user.username,
        answer
    )

    return answer