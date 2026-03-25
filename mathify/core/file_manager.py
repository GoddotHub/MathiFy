import os
from core.config import SAVE_HISTORY_FILE

def save_history(history: list[str]):
    with open(SAVE_HISTORY_FILE, "w") as f:
        f.write("\n".join(history))

def load_history() -> list[str]:
    if not os.path.exists(SAVE_HISTORY_FILE):
        return []
    with open(SAVE_HISTORY_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]