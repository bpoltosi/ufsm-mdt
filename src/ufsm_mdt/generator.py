from pathlib import Path
from .profiles import load_profile
from .model import Document

TEMPLATE = Path(__file__).resolve().parents[2] / "template" / "upstream"

def _tex(v):
    value = str(v if v is not None else "")
    escapes = {
        "\\": r"\textbackslash{}",
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(escapes.get(char, char) for char in value)

def _cmd(name, *values):
    return "\\" + name + "".join("{" + _tex(v) + "}" for v in values)

def _references_bib(references):
    if isinstance(references, str) and references.strip():
        return references.strip()
    if not isinstance(references, list):
        return ""
    entries = []
    for i, ref in enumerate(references):
        if not isinstance(ref, dict):
            continue
        author = str(ref.get("author", "")).strip()
        title = str(ref.get("title", "")).strip()
        year = str(ref.get("year", "")).strip()
        if not (author and title and year):
            continue
        key = "ref" + str(ref.get("id", i)).replace("-", "")
        publisher = str(ref.get("publisher", "")).strip()
        entry = f"@misc{{{key},\n  author = {{{author}}},\n  title = {{{title}}},\n  year = {{{year}}}"
        if publisher:
            entry += f",\n  publisher = {{{publisher}}}"
        entry += "\n}"
        entries.append(entry)
    return "\n\n".join(entries)

def render_main(document):
    profile = load_profile(document.type)
    metadata = document.metadata
    lines = [
        r"\documentclass[oneside,openright,12pt]{ufsm_2021}",
        r"\usepackage{lipsum}",
        _cmd("centroensino", metadata.get("centro_ensino", "Centro de Ensino")),
        _cmd("centroensinosigla", metadata.get("centro_ensino_sigla", "UFSM")),
        _cmd("nivelensino", metadata.get("nivel_ensino", "Graduação")),
        _cmd("curso", metadata.get("curso", "Curso")),
        _cmd("ppg", metadata.get("ppg", "PPG")),
        _cmd("statuscurso", metadata.get("status_curso", "Curso")),
        _cmd("cidade", metadata.get("cidade", "Santa Maria")),
        _cmd("estado", metadata.get("estado", "RS")),
        _cmd("author", metadata.get("author", "Autor")),
        _cmd("sexo", metadata.get("sexo", "M")),
        _cmd("grauensino", metadata.get("grau_ensino", "Graduação")),
        _cmd("grauobtido", metadata.get("grau_obtido", "Graduado")),
        _cmd("email", metadata.get("email", "autor@example.org")),
        _cmd("titulo", metadata.get("title", profile["name"])),
        _cmd("englishtitle", metadata.get("english_title", profile["name"])),
        _cmd("areaconcentracao", metadata.get("area_concentracao", "Área de concentração")),
        _cmd("data", metadata.get("day", "01"), metadata.get("month", "01"), metadata.get("year", "2026")),
    ]
    if metadata.get("subtitle"):
        lines += [_cmd("subtitulo", metadata["subtitle"]), _cmd("subenglishtitle", metadata.get("english_subtitle", metadata["subtitle"]))]
    if profile["template_command"] == "generico":
        lines += [
            _cmd("tipogenerico", metadata.get("generic_type_pt", profile["name"])),
            _cmd("tipogenericoen", metadata.get("generic_type_en", profile["name"])),
            _cmd("concordagenerico", metadata.get("generic_concordance", "o")),
            _cmd("graugenerico", metadata.get("grau_obtido", "Graduado")),
        ]
    lines += [
        "\\" + profile["template_command"],
        _cmd("videoconferenciabancap", metadata.get("videoconferencia_banca_presencial", "")),
        _cmd("videoconferenciabancas", metadata.get("videoconferencia_banca_suplementar", "")),
        _cmd("orientador", metadata.get("orientador_nome", "Orientador"), metadata.get("orientador_titulo", "Dr."), metadata.get("orientador_instituicao", "UFSM"), metadata.get("orientador_sexo", "M"), metadata.get("orientador_presidente", "P")),
        r"\semcatalografica",
        r"\resumo{Resumo de exemplo gerado automaticamente para validar a estrutura do perfil.}",
        r"\palavrachave{Exemplo. Perfil. UFSM.}",
        r"\abstract{Example abstract generated automatically to validate the profile structure.}",
        r"\keywords{Example. Profile. UFSM.}",
        r"\begin{document}",
        r"\pretextual",
    ]
    sections = document.sections or [{"title": "Introdução", "content": "Conteúdo inicial do trabalho."}, {"title": "Conclusão", "content": "Conclusão do trabalho."}]
    for section in sections:
        lines += [f"\\chapter{{{_tex(section.get('title', 'Seção'))}}}", str(section.get("content", ""))]
    lines += [r"\startbibliography", r"\bibliography{referencias}", r"\end{document}", ""]
    return "\n".join(lines)

def generate(document, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    for name in ("ufsm_2021.cls", "tocstyle.sty"):
        (output / name).write_text((TEMPLATE / name).read_text(encoding="utf-8"), encoding="utf-8")
    (output / "main.tex").write_text(render_main(document), encoding="utf-8")
    bib = _references_bib(document.references) or "@misc{example, title={Exemplo}, author={UFSM}, year={2026}}"
    (output / "referencias.bib").write_text(bib + "\n", encoding="utf-8")
    return output
