import pytest
from ufsm_mdt.validator import validate

def test_validator_accepts_complete_fixture():
    data={"type":"thesis","metadata":{"author":"A","title":"T","english_title":"T","centro_ensino":"C","centro_ensino_sigla":"C","nivel_ensino":"P","curso":"C","status_curso":"Programa","cidade":"Santa Maria","estado":"RS","grau_ensino":"Doutorado","grau_obtido":"Doutor","email":"a@example.org","day":"01","month":"01","year":"2026"},"sections":[{"title":"Introdução","content":"Texto"}]}
    assert not [x for x in validate(data) if x.severity=="ERROR"]

def test_validator_reports_missing_metadata():
    findings=validate({"type":"thesis","metadata":{}})
    assert any(x.severity=="ERROR" for x in findings)
