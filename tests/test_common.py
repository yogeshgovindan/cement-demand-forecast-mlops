from pathlib import Path

from src.utils.common import (
    create_directories,
    save_json,
    load_json
)


test_folder = Path("artifacts/test")


create_directories(
    [test_folder]
)


data = {
    "model": "RandomForest",
    "accuracy": 0.95
}


save_json(
    test_folder / "test.json",
    data
)


result = load_json(
    test_folder / "test.json"
)


print(result)
