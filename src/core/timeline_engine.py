from datetime import datetime


def _get_date(item, default=None):
    """Safely get a date from a dictionary."""

    if default is None:
        default = datetime.now().strftime("%Y-%m-%d")

    if isinstance(item, dict):
        return item.get("date", default)

    return default


def generate_timeline(memory):
    """
    Generates a unified Founder Timeline from memory.
    """

    timeline = []

    # ----------------------------
    # Assessments
    # ----------------------------

    for assessment in memory.get("assessments", []):

        timeline.append({
            "date": _get_date(assessment),
            "type": "Assessment",
            "icon": "bi-clipboard-check",
            "title": "Founder Assessment Completed",
            "description": f"Founder Score: {assessment.get('score', 'N/A')}"
        })

    # ----------------------------
    # Goals
    # ----------------------------

    for goal in memory.get("goals", []):

        if isinstance(goal, str):

            timeline.append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "type": "Goal",
                "icon": "bi-bullseye",
                "title": "New Goal",
                "description": goal
            })

        else:

            timeline.append({
                "date": _get_date(goal),
                "type": "Goal",
                "icon": "bi-bullseye",
                "title": goal.get("title", "Startup Goal"),
                "description": goal.get("description", "")
            })

    # ----------------------------
    # Decisions
    # ----------------------------

    for decision in memory.get("decisions", []):

        if isinstance(decision, str):

            timeline.append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "type": "Decision",
                "icon": "bi-lightbulb",
                "title": "Founder Decision",
                "description": decision
            })

        else:

            timeline.append({
                "date": _get_date(decision),
                "type": "Decision",
                "icon": "bi-lightbulb",
                "title": decision.get("title", "Decision"),
                "description": decision.get("description", "")
            })

    # ----------------------------
    # Tasks
    # ----------------------------

    for task in memory.get("tasks", []):

        if isinstance(task, str):

            timeline.append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "type": "Task",
                "icon": "bi-check2-square",
                "title": "Task Added",
                "description": task
            })

        else:

            timeline.append({
                "date": _get_date(task),
                "type": "Task",
                "icon": "bi-check2-square",
                "title": task.get("title", "Task"),
                "description": task.get("description", "")
            })

    # ----------------------------
    # Reports
    # ----------------------------

    for report in memory.get("reports", []):

        timeline.append({
            "date": _get_date(report),
            "type": "Report",
            "icon": "bi-file-earmark-pdf",
            "title": "Report Generated",
            "description": report.get("title", "Founder Report")
        })

    # ----------------------------
    # AI Recommendations
    # ----------------------------

    for recommendation in memory.get("recommendations", []):

        timeline.append({
            "date": _get_date(recommendation),
            "type": "Recommendation",
            "icon": "bi-stars",
            "title": "AI Recommendation",
            "description": recommendation.get(
                "text",
                recommendation if isinstance(recommendation, str) else ""
            )
        })

    # ----------------------------
    # Notes
    # ----------------------------

    for note in memory.get("notes", []):

        timeline.append({
            "date": _get_date(note),
            "type": "Note",
            "icon": "bi-journal-text",
            "title": "Founder Note",
            "description": note.get(
                "text",
                note if isinstance(note, str) else ""
            )
        })

    # ----------------------------
    # Sort newest first
    # ----------------------------

    timeline.sort(
        key=lambda item: item["date"],
        reverse=True
    )

    return timeline