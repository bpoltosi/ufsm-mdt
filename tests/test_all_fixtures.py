import json
from pathlib import Path

import pytest

from ufsm_mdt.generator import generate
from ufsm_mdt.model import Document
from ufsm_mdt.profiles import load_profile

FIXTURES = sorted(Path("tests/fixtures").glob("*/document.json"))


@pytest.mark.parametrize("source", FIXTURES, ids=lambda p: p.parent.name)
def test_every_fixture_generates_complete_project(tmp_path, source):
    data = json.loads(source.read_text(encoding="utf-8"))
    document = Document.from_dict(data)
    profile = load_profile(document.type)
    out = generate(document, tmp_path / document.type)

    assert (out / "main.tex").is_file()
    assert (out / "ufsm_2021.cls").is_file()
    assert (out / "tocstyle.sty").is_file()
    assert (out / "referencias.bib").is_file()

    tex = (out / "main.tex").read_text(encoding="utf-8")
    assert f"\\{profile['template_command']}" in tex
    assert "\\begin{document}" in tex
    assert "\\end{document}" in tex
