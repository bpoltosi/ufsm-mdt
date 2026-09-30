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


def test_generator_escapes_latex_metadata(tmp_path):
    doc = Document(
        type="article",
        metadata={
            "author": "Autor & Co.",
            "title": "Título_100% {teste}",
            "english_title": "A \\ B ~ C ^ D",
        },
    )
    out = generate(doc, tmp_path / "escaped")
    tex = (out / "main.tex").read_text(encoding="utf-8")
    assert r"Autor \& Co." in tex
    assert r"Título\_100\% \{teste\}" in tex
    assert r"A \textbackslash{} B \textasciitilde{} C \textasciicircum{} D" in tex


def test_generator_accepts_browser_reference_objects(tmp_path):
    doc = Document(type="thesis", metadata={"author":"A","title":"T"}, sections=[{"title":"Introdução","content":"Texto"}], references=[{"id":"r1","author":"AUTOR","year":"2024","title":"Título","type":"Livro","publisher":"Editora"}])
    out = generate(doc, tmp_path/"browser-contract")
    bib = (out/"referencias.bib").read_text(encoding="utf-8")
    assert "@misc{r1" in bib
    assert "publisher = {Editora}" in bib
