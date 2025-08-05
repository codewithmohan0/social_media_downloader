import json
import os

HISTORY_FILE = "history.json"

def save_history(entry):
    history = load_history()
    history.insert(0, {
        "title": entry["title"],
        "filename": entry["filename"],
        "platform": entry["platform"]
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[:50], f)  # Keep only latest 50

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
