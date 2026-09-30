from pathlib import Path
from .profiles import load_profile
from .model import Document
TEMPLATE=Path(__file__).resolve().parents[2]/"template"/"upstream"
def _tex(v):
    return str(v if v is not None else "").replace("\\",r"\\textbackslash{}").replace("&",r"\\&").replace("%",r"\\%").replace("#",r"\\#").replace("_",r"\\_")
def _cmd(name,*values): return "\\"+name+"".join("{"+_tex(v)+"}" for v in values)
def render_main(document):
    p=load_profile(document.type); m=document.metadata
    lines=[r"\documentclass[oneside,openright,12pt]{ufsm_2021}",r"\usepackage{lipsum}",_cmd("centroensino",m.get("centro_ensino","Centro de Ensino")),_cmd("centroensinosigla",m.get("centro_ensino_sigla","UFSM")),_cmd("nivelensino",m.get("nivel_ensino","Graduação")),_cmd("curso",m.get("curso","Curso")),_cmd("ppg",m.get("ppg","PPG")),_cmd("statuscurso",m.get("status_curso","Curso")),_cmd("cidade",m.get("cidade","Santa Maria")),_cmd("estado",m.get("estado","RS")),_cmd("author",m.get("author","Autor")),_cmd("sexo",m.get("sexo","M")),_cmd("grauensino",m.get("grau_ensino","Graduação")),_cmd("grauobtido",m.get("grau_obtido","Graduado")),_cmd("email",m.get("email","autor@example.org")),_cmd("titulo",m.get("title",p["name"])),_cmd("englishtitle",m.get("english_title",p["name"])),_cmd("areaconcentracao",m.get("area_concentracao","Área de concentração")),_cmd("data",m.get("day","01"),m.get("month","01"),m.get("year","2026"))]
    if m.get("subtitle"): lines += [_cmd("subtitulo",m["subtitle"]),_cmd("subenglishtitle",m.get("english_subtitle",m["subtitle"]))]
    if p["template_command"]=="generico": lines += [_cmd("tipogenerico",m.get("generic_type_pt",p["name"])),_cmd("tipogenericoen",m.get("generic_type_en",p["name"])),_cmd("concordagenerico",m.get("generic_concordance","o")),_cmd("graugenerico",m.get("grau_obtido","Graduado"))]
    lines += ["\\"+p["template_command"],_cmd("orientador",m.get("orientador_nome","Orientador"),m.get("orientador_titulo","Dr."),m.get("orientador_instituicao","UFSM"),m.get("orientador_sexo","M"),m.get("orientador_presidente","P")),r"\semcatalografica",r"\resumo{Resumo de exemplo gerado automaticamente para validar a estrutura do perfil.}",r"\palavrachave{Exemplo. Perfil. UFSM.}",r"\abstract{Example abstract generated automatically to validate the profile structure.}",r"\keywords{Example. Profile. UFSM.}",r"\begin{document}",r"\pretextual"]
    sections=document.sections or [{"title":"Introdução","content":"Conteúdo inicial do trabalho."},{"title":"Conclusão","content":"Conclusão do trabalho."}]
    for s in sections: lines += [f"\\chapter{{{_tex(s.get('title','Seção'))}}}",s.get("content","")]
    lines += [r"\startbibliography",r"\bibliography{referencias}",r"\end{document}",""]
    return "\n".join(lines)
def generate(document,output):
    output=Path(output); output.mkdir(parents=True,exist_ok=True)
    for name in ("ufsm_2021.cls","tocstyle.sty"): (output/name).write_text((TEMPLATE/name).read_text(encoding="utf-8"),encoding="utf-8")
    (output/"main.tex").write_text(render_main(document),encoding="utf-8")
    (output/"referencias.bib").write_text((document.references or "@misc{example, title={Exemplo}, author={UFSM}, year={2026}}")+"\n",encoding="utf-8")
    return output
