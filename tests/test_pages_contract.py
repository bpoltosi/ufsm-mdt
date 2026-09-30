from pathlib import Path


def test_pages_uses_audit_semantics():
    html = Path("docs/canvasite.html").read_text(encoding="utf-8")
    assert "Novo rascunho" in html
    assert "Conferência MDT" in html
    assert "Itens conferidos" in html
    assert "PDF — em desenvolvimento" in html
    assert "DOCX — em desenvolvimento" in html


def test_pages_inline_script_is_present():
    html = Path("docs/canvasite.html").read_text(encoding="utf-8")
    assert "const STORAGE_KEY='mdt-ufsm-draft-v3'" in html
    assert "prefers-color-scheme" in html
    assert "MDT-SCHEMA" not in html
