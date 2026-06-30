from src.services.memory_service import load_memory


def _format_list(items, key=None, limit=5):
    """
    Converts lists of strings/dictionaries into readable text
    for the LLM prompt.
    """

    if not items:
        return "None"

    lines = []

    for item in items[-limit:]:

        if isinstance(item, str):
            lines.append(f"- {item}")

        elif isinstance(item, dict):

            if key and item.get(key):
                lines.append(f"- {item[key]}")

            elif item.get("title"):
                lines.append(f"- {item['title']}")

            elif item.get("text"):
                lines.append(f"- {item['text']}")

            elif item.get("event"):
                lines.append(f"- {item['event']}")

            else:
                lines.append(f"- {str(item)}")

    return "\n".join(lines)


def build_context(user, founder_data, question):

    memory = load_memory(user.username)

    startup = memory.get("startup", {})
    profile = memory.get("profile", {})

    context = f"""
=========================================================
FOUNDER PROFILE
=========================================================

Founder Name:
{user.username}

Startup Name:
{startup.get("name", getattr(user, "startup_name", "Not Available"))}

Industry:
{startup.get("industry", getattr(user, "industry", "Not Available"))}

Founder Experience:
{profile.get("experience", "Unknown")}

=========================================================
CURRENT ASSESSMENT
=========================================================

Founder Score:
{founder_data.get("score", "N/A")}

Startup Stage:
{founder_data.get("startup_stage", "N/A")}

Budget:
₹{founder_data.get("budget", "N/A")}

Team Size:
{founder_data.get("team_size", "N/A")}

Programming:
{founder_data.get("programming", "N/A")}/10

Marketing:
{founder_data.get("marketing", "N/A")}/10

Finance:
{founder_data.get("finance", "N/A")}/10

Leadership:
{founder_data.get("leadership", "N/A")}/10

Communication:
{founder_data.get("communication", "N/A")}/10

Problem Solving:
{founder_data.get("problem_solving", "N/A")}/10

Risk Tolerance:
{founder_data.get("risk_tolerance", "N/A")}/10

=========================================================
FOUNDER GOALS
=========================================================

{_format_list(memory.get("goals", []))}

=========================================================
ACTIVE TASKS
=========================================================

{_format_list(memory.get("tasks", []))}

=========================================================
RECENT DECISIONS
=========================================================

{_format_list(memory.get("decisions", []))}

=========================================================
RECENT NOTES
=========================================================

{_format_list(memory.get("notes", []))}

=========================================================
RECENT REPORTS
=========================================================

{_format_list(memory.get("reports", []))}

=========================================================
AI RECOMMENDATIONS
=========================================================

{_format_list(memory.get("recommendations", []), key="text")}

=========================================================
RECENT CHAT HISTORY
=========================================================

{_format_list(memory.get("chat_history", []), key="question")}

=========================================================
USER QUESTION
=========================================================

{question}

=========================================================
AI INSTRUCTIONS
=========================================================

You are FoundrAI, an AI Founder Operating System.

Do NOT give generic startup advice.

Use the founder's assessment, startup profile,
goals, tasks, previous decisions, notes,
reports, recommendations, and recent conversations
to provide personalized guidance.

If the founder has weak skills,
recommend practical actions.

If there are unfinished goals or tasks,
prioritize those before suggesting new work.

Always explain your reasoning before giving recommendations.
"""

    return context