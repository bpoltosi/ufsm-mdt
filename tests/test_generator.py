import json
from pathlib import Path
from ufsm_mdt.generator import generate
from ufsm_mdt.model import Document

def test_generator_emits_independent_project(tmp_path):
    source=Path("tests/fixtures/dissertation/document.json")
    doc=Document.from_dict(json.loads(source.read_text(encoding="utf-8")))
    out=generate(doc,tmp_path/"project")
    assert (out/"main.tex").is_file()
    assert (out/"ufsm_2021.cls").is_file()
    assert (out/"tocstyle.sty").is_file()
    assert (out/"referencias.bib").is_file()
    assert "\\dissertacao" in (out/"main.tex").read_text(encoding="utf-8")
