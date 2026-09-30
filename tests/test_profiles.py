import json
from pathlib import Path
from ufsm_mdt.profiles import list_profiles, load_profile

EXPECTED={"research-project","tcc","internship-report","dissertation","thesis","article","technical-report","monograph","didactic-material","pedagogical-resource","professional-project"}

def test_all_documented_types_have_profiles():
    assert set(list_profiles()) == EXPECTED
    for profile_id in EXPECTED:
        p=load_profile(profile_id)
        assert p["id"]==profile_id
        assert p["template_command"]

def test_all_fixtures_match_profiles():
    root=Path("tests/fixtures")
    for path in root.glob("*/document.json"):
        data=json.loads(path.read_text(encoding="utf-8"))
        assert data["type"] in EXPECTED
