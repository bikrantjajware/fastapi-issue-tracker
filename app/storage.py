from pathlib import Path
import json

DATA_DIR = Path("data")
ISSUES_FILE_PATH = DATA_DIR / 'issues.json'

def load():
    if ISSUES_FILE_PATH.exists():
        with ISSUES_FILE_PATH.open('r') as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []

def save(issues):
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    with ISSUES_FILE_PATH.open('w') as f:
        json.dump(issues, f, indent=4)

