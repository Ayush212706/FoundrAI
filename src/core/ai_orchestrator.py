from src.core.intelligence_engine import analyze_founder
from src.core.recommendation_engine import generate_recommendations
from src.core.progress_engine import calculate_progress
from src.core.decision_engine import analyze_decision
from src.core.task_engine import generate_tasks
from src.core.timeline_engine import generate_timeline


def build_ai_context(founder, memory=None):
    """
    Main AI orchestration function.

    This function gathers information from every intelligence
    component and prepares one unified context for the AI model.
    """

    if memory is None:
        memory = {}

    # ----------------------------------------------------
    # Intelligence
    # ----------------------------------------------------

    intelligence = analyze_founder(founder)

    # ----------------------------------------------------
    # Recommendations
    # ----------------------------------------------------

    recommendations = generate_recommendations(founder)

    # ----------------------------------------------------
    # Founder Progress
    # ----------------------------------------------------

    progress = calculate_progress(founder)

    # ----------------------------------------------------
    # Decision Analysis
    # ----------------------------------------------------

    try:
        decision_analysis = analyze_decision(founder)
    except Exception:
        decision_analysis = {}

    # ----------------------------------------------------
    # Task Engine
    # ----------------------------------------------------

    try:
        tasks = generate_tasks(memory)
    except Exception:
        tasks = {
            "tasks": [],
            "today_tasks": [],
            "upcoming_tasks": [],
            "high_priority_tasks": [],
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "overdue_tasks": 0,
            "completion_rate": 0
        }

    # ----------------------------------------------------
    # Timeline
    # ----------------------------------------------------

    try:
        timeline = generate_timeline(memory)
    except Exception:
        timeline = []

    # ----------------------------------------------------
    # Startup Snapshot
    # ----------------------------------------------------

    startup = memory.get("startup", {})

    startup_snapshot = {
        "name": startup.get("name", ""),
        "industry": startup.get("industry", ""),
        "stage": founder.get(
            "startup_stage",
            startup.get("stage", "")
        )
    }

    # ----------------------------------------------------
    # Memory Summary
    # ----------------------------------------------------

    memory_summary = {
        "goals": len(memory.get("goals", [])),
        "tasks": len(memory.get("tasks", [])),
        "decisions": len(memory.get("decisions", [])),
        "notes": len(memory.get("notes", [])),
        "reports": len(memory.get("reports", [])),
        "assessments": len(memory.get("assessments", [])),
        "chat_history": len(memory.get("chat_history", []))
    }

    # ----------------------------------------------------
    # Final AI Context
    # ----------------------------------------------------

    return {

        "founder": founder,

        "startup": startup_snapshot,

        "intelligence": intelligence,

        "recommendations": recommendations,

        "progress": progress,

        "decision_analysis": decision_analysis,

        "tasks": tasks,

        "timeline": timeline,

        "memory_summary": memory_summary,

        "memory": memory

    }