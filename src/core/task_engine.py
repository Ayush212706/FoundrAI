from datetime import datetime


def _today():
    return datetime.now().strftime("%Y-%m-%d")


def _normalize_task(task):
    """
    Converts a string or dictionary into a standard task object.
    """

    if isinstance(task, str):
        return {
            "title": task,
            "description": "",
            "priority": "Medium",
            "status": "Pending",
            "due_date": "",
            "created_at": _today()
        }

    return {
        "title": task.get("title", "Untitled Task"),
        "description": task.get("description", ""),
        "priority": task.get("priority", "Medium"),
        "status": task.get("status", "Pending"),
        "due_date": task.get("due_date", ""),
        "created_at": task.get("created_at", _today())
    }


def generate_tasks(memory):
    """
    Generates a complete task dashboard using memory data.
    """

    tasks = []

    # Existing tasks
    for task in memory.get("tasks", []):
        tasks.append(_normalize_task(task))

    # Tasks from goals
    for goal in memory.get("goals", []):

        if isinstance(goal, str):
            goal_title = goal

        else:
            goal_title = goal.get("title", "Startup Goal")

        tasks.append({
            "title": f"Work on: {goal_title}",
            "description": "Progress towards this startup goal.",
            "priority": "High",
            "status": "Pending",
            "due_date": "",
            "created_at": _today()
        })

    # AI-generated tasks from weak skills
    latest_assessment = None

    assessments = memory.get("assessments", [])

    if assessments:
        latest_assessment = assessments[-1]

    if latest_assessment:

        weak_skills = latest_assessment.get("weak_skills", [])

        skill_map = {
            "Programming": "Build one practical coding project.",
            "Marketing": "Study customer acquisition strategies.",
            "Finance": "Create a startup budget and pricing model.",
            "Leadership": "Practice delegation and decision-making.",
            "Communication": "Improve pitching and presentation skills.",
            "Problem Solving": "Solve real startup case studies.",
            "Risk": "Analyze successful startup failures."
        }

        for skill in weak_skills:

            tasks.append({
                "title": f"Improve {skill}",
                "description": skill_map.get(
                    skill,
                    f"Improve your {skill} skill."
                ),
                "priority": "Medium",
                "status": "Pending",
                "due_date": "",
                "created_at": _today()
            })

    # Statistics
    total_tasks = len(tasks)

    completed_tasks = len(
        [
            t for t in tasks
            if t["status"].lower() == "completed"
        ]
    )

    pending_tasks = len(
        [
            t for t in tasks
            if t["status"].lower() != "completed"
        ]
    )

    overdue_tasks = len(
        [
            t for t in tasks
            if t["due_date"]
            and t["due_date"] < _today()
            and t["status"].lower() != "completed"
        ]
    )

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100,
            2
        )

    high_priority = [
        t
        for t in tasks
        if t["priority"].lower() == "high"
    ]

    today_tasks = [
        t
        for t in tasks
        if t["due_date"] == _today()
    ]

    upcoming_tasks = [
        t
        for t in tasks
        if t["due_date"] > _today()
    ]

    return {

        "tasks": tasks,

        "today_tasks": today_tasks,

        "upcoming_tasks": upcoming_tasks,

        "high_priority_tasks": high_priority,

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "pending_tasks": pending_tasks,

        "overdue_tasks": overdue_tasks,

        "completion_rate": completion_rate

    }