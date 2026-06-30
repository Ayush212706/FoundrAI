import json
from pathlib import Path
from datetime import datetime

MEMORY_DIR = Path("memory")
MEMORY_DIR.mkdir(exist_ok=True)


def _memory_path(username):
    return MEMORY_DIR / f"{username}.json"


def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _default_memory():
    return {
        "profile": {},
        "startup": {},
        "assessments": [],
        "goals": [],
        "tasks": [],
        "timeline": [],
        "decisions": [],
        "notes": [],
        "reports": [],
        "recommendations": [],
        "chat_history": []
    }


def load_memory(username):
    path = _memory_path(username)

    if not path.exists():
        return _default_memory()

    with open(path, "r", encoding="utf-8") as f:
        memory = json.load(f)

    defaults = _default_memory()

    for key, value in defaults.items():
        memory.setdefault(key, value)

    return memory


def save_memory(username, memory):
    with open(_memory_path(username), "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)


# ------------------------------------------------------------------
# Founder Profile
# ------------------------------------------------------------------

def save_profile(username, profile):
    memory = load_memory(username)
    memory["profile"] = profile
    save_memory(username, memory)


# ------------------------------------------------------------------
# Startup Profile
# ------------------------------------------------------------------

def save_startup(username, startup):
    memory = load_memory(username)
    memory["startup"] = startup
    save_memory(username, memory)


# ------------------------------------------------------------------
# Assessment
# ------------------------------------------------------------------

def save_assessment(username, founder):
    memory = load_memory(username)

    assessment = {
        "date": _timestamp(),
        "score": founder.get("score"),
        "budget": founder.get("budget"),
        "team_size": founder.get("team_size"),
        "startup_stage": founder.get("startup_stage"),
        "programming": founder.get("programming"),
        "marketing": founder.get("marketing"),
        "finance": founder.get("finance"),
        "leadership": founder.get("leadership"),
        "communication": founder.get("communication"),
        "problem_solving": founder.get("problem_solving"),
        "risk_tolerance": founder.get("risk_tolerance")
    }

    memory["assessments"].append(assessment)
    save_memory(username, memory)


# ------------------------------------------------------------------
# Chat History
# ------------------------------------------------------------------

def save_chat(username, question, answer):
    memory = load_memory(username)

    memory["chat_history"].append({
        "question": question,
        "answer": answer,
        "time": _timestamp()
    })

    save_memory(username, memory)


# ------------------------------------------------------------------
# Goals
# ------------------------------------------------------------------

def add_goal(username, goal):
    memory = load_memory(username)

    if isinstance(goal, str):
        goal = {
            "title": goal,
            "date": _timestamp()
        }

    memory["goals"].append(goal)
    save_memory(username, memory)


# ------------------------------------------------------------------
# Tasks
# ------------------------------------------------------------------

def add_task(username, task):
    memory = load_memory(username)

    if isinstance(task, str):
        task = {
            "title": task,
            "status": "Pending",
            "date": _timestamp()
        }

    memory["tasks"].append(task)
    save_memory(username, memory)


# ------------------------------------------------------------------
# Timeline
# ------------------------------------------------------------------

def add_timeline(username, event):
    memory = load_memory(username)

    memory["timeline"].append({
        "event": event,
        "time": _timestamp()
    })

    save_memory(username, memory)


# ------------------------------------------------------------------
# Decisions
# ------------------------------------------------------------------

def add_decision(username, decision):
    memory = load_memory(username)

    if isinstance(decision, str):
        decision = {
            "title": decision,
            "date": _timestamp()
        }

    memory["decisions"].append(decision)
    save_memory(username, memory)


# ------------------------------------------------------------------
# Notes
# ------------------------------------------------------------------

def add_note(username, note):
    memory = load_memory(username)

    if isinstance(note, str):
        note = {
            "text": note,
            "date": _timestamp()
        }

    memory["notes"].append(note)
    save_memory(username, memory)


# ------------------------------------------------------------------
# Reports
# ------------------------------------------------------------------

def add_report(username, report_name):
    memory = load_memory(username)

    memory["reports"].append({
        "title": report_name,
        "date": _timestamp()
    })

    save_memory(username, memory)


# ------------------------------------------------------------------
# AI Recommendations
# ------------------------------------------------------------------

def add_recommendation(username, recommendation):
    memory = load_memory(username)

    memory["recommendations"].append({
        "text": recommendation,
        "date": _timestamp()
    })

    save_memory(username, memory)