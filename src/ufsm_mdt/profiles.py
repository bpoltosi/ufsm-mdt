from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
PROFILE_DIR=ROOT/"profiles"
def list_profiles(): return sorted(p.stem for p in PROFILE_DIR.glob("*.json"))
def load_profile(profile_id):
    path=PROFILE_DIR/f"{profile_id}.json"
    if not path.is_file(): raise ValueError(f"Tipo de trabalho não suportado: {profile_id}")
    return json.loads(path.read_text(encoding="utf-8"))
