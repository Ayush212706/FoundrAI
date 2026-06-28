import json
from pathlib import Path

MEMORY_DIR = Path("memory")

MEMORY_DIR.mkdir(exist_ok=True)


def get_memory_file(username):
    return MEMORY_DIR / f"{username}.json"


def load_memory(username):

    file = get_memory_file(username)

    if not file.exists():
        return {
            "profile": {},
            "goals": [],
            "timeline": [],
            "notes": [],
            "decisions": [],
            "startup": {}
        }

    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(username, memory):

    file = get_memory_file(username)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)


def add_goal(username, goal):

    memory = load_memory(username)

    memory["goals"].append(goal)

    save_memory(username, memory)


def add_decision(username, decision):

    memory = load_memory(username)

    memory["decisions"].append(decision)

    save_memory(username, memory)


def add_note(username, note):

    memory = load_memory(username)

    memory["notes"].append(note)

    save_memory(username, memory)


def add_timeline(username, event):

    memory = load_memory(username)

    memory["timeline"].append(event)

    save_memory(username, memory)