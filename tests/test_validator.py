import pytest
from ufsm_mdt.validator import validate

def test_validator_accepts_complete_fixture():
    data={"type":"thesis","metadata":{"author":"A","title":"T","english_title":"T","centro_ensino":"C","centro_ensino_sigla":"C","nivel_ensino":"P","curso":"C","status_curso":"Programa","cidade":"Santa Maria","estado":"RS","grau_ensino":"Doutorado","grau_obtido":"Doutor","email":"a@example.org","day":"01","month":"01","year":"2026"},"sections":[{"title":"Introdução","content":"Texto"}]}
    assert not [x for x in validate(data) if x.severity=="ERROR"]

def test_validator_reports_missing_metadata():
    findings=validate({"type":"thesis","metadata":{}})
    assert any(x.severity=="ERROR" for x in findings)


def test_validator_reports_structure_and_reference_findings():
    data = {"type": "thesis", "metadata": {}}
    findings = validate(data)
    assert any(x.rule_id == "MDT-STRUCT-001" and x.severity == "WARNING" for x in findings)
    assert any(x.rule_id == "MDT-REF-001" and x.severity == "INFO" for x in findings)


def test_validator_uses_profile_metadata_contract():
    data = {
        "type": "thesis",
        "metadata": {"author": "A"},
        "sections": [{"title": "Introdução", "content": "Texto"}],
        "references": "ref",
    }
    findings = validate(data)
    ids = {x.rule_id for x in findings}
    assert "MDT-CONFIG-AUTHOR" not in ids
    assert any(x.rule_id == "MDT-CONFIG-TITLE" for x in findings)
    assert "MDT-STRUCT-001" not in ids
    assert "MDT-REF-001" not in ids
