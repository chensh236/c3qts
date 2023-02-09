"""
Global setting of the trading platform.
"""
import json
from typing import Dict, Tuple, Any
from .util import _get_trader_dir, get_file_path, TRADER_DIR, TEMP_DIR

TRADER_DIR, TEMP_DIR = _get_trader_dir(".tmp")

def save_json(filename: str, data: dict) -> None:
    """
    Save data into json file in temp path.
    """
    filepath = get_file_path(filename)
    with open(filepath, mode="w+", encoding="UTF-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

def load_json(filename: str) -> dict:
    """
    Load data from json file in temp path.
    """
    filepath = get_file_path(filename)

    if filepath.exists():
        with open(filepath, mode="r", encoding="UTF-8") as f:
            data = json.load(f)
        return data
    else:
        save_json(filename, {})
        return {}



SETTINGS: Dict[str, Any] = {
    "database.database": "future_seq_data",
    "database.name": "localdb",
    "database.basedir":"/14T/dev_database"
}


# Load global setting from json file.
SETTING_FILENAME: str = "st_settings.json"
SETTINGS.update(load_json(SETTING_FILENAME))

def get_settings(prefix: str = "") -> Dict[str, Any]:
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}
