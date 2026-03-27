import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".gitool.json"

DEFAULT_CONFIG = {
    "base_path": str(Path.home() / "Projects")
}

def get_config() -> dict:
    if not CONFIG_PATH.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    with open(CONFIG_PATH) as f:
        return json.load(f)

def save_config(config: dict):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)