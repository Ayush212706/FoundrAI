import json
from pathlib import Path
from datetime import datetime

MEMORY_DIR = Path("memory")
MEMORY_DIR.mkdir(exist_ok=True)


def _memory_path(username):
    return MEMORY_DIR / f"{username}.json"


def load_memory(username):

    path = _memory_path(username)

    if not path.exists():

        return {
            "profile": {},
            "assessments": [],
            "goals": [],
            "timeline": [],
            "decisions": [],
            "notes": [],
            "chat_history": []
        }

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(username, memory):

    with open(_memory_path(username), "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)


def save_assessment(username, founder):

    memory = load_memory(username)

    assessment = {

        "date": str(datetime.now()),

        "score": founder["score"],

        "budget": founder["budget"],

        "team_size": founder["team_size"],

        "startup_stage": founder["startup_stage"],

        "programming": founder["programming"],

        "marketing": founder["marketing"],

        "finance": founder["finance"],

        "leadership": founder["leadership"],

        "communication": founder["communication"],

        "problem_solving": founder["problem_solving"]

    }

    memory["assessments"].append(assessment)

    save_memory(username, memory)


def save_chat(username, question, answer):

    memory = load_memory(username)

    memory["chat_history"].append({

        "question": question,

        "answer": answer,

        "time": str(datetime.now())

    })

    save_memory(username, memory)


def add_goal(username, goal):

    memory = load_memory(username)

    memory["goals"].append(goal)

    save_memory(username, memory)


def add_timeline(username, event):

    memory = load_memory(username)

    memory["timeline"].append({

        "event": event,

        "time": str(datetime.now())

    })

    save_memory(username, memory)


def add_decision(username, decision):

    memory = load_memory(username)

    memory["decisions"].append(decision)

    save_memory(username, memory)


def add_note(username, note):

    memory = load_memory(username)

    memory["notes"].append(note)

    save_memory(username, memory)