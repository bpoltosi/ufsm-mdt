from dataclasses import dataclass
from .profiles import load_profile, list_profiles

@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    message: str

def _shape_findings(data):
    out=[]
    if not isinstance(data, dict):
        return [Finding("MDT-SCHEMA-001","ERROR","O documento importado deve ser um objeto JSON.")]
    if not isinstance(data.get("type"), str) or data.get("type") not in set(list_profiles()):
        out.append(Finding("MDT-SCHEMA-002","ERROR","Tipo de trabalho ausente ou não suportado."))
    if not isinstance(data.get("metadata", {}), dict):
        out.append(Finding("MDT-SCHEMA-003","ERROR","metadata deve ser um objeto JSON."))
    sections=data.get("sections", [])
    if not isinstance(sections, list):
        out.append(Finding("MDT-SCHEMA-004","ERROR","sections deve ser uma lista."))
    else:
        for i,item in enumerate(sections):
            if not isinstance(item, dict) or not isinstance(item.get("title"), str) or not isinstance(item.get("content", ""), str):
                out.append(Finding("MDT-SCHEMA-005","ERROR",f"Seção {i+1} inválida: informe title e content como texto."))
                break
    refs=data.get("references", [])
    if not isinstance(refs, (list, str)):
        out.append(Finding("MDT-SCHEMA-006","ERROR","references deve ser uma lista de referências ou BibTeX legado em texto."))
    elif isinstance(refs, list):
        for i,ref in enumerate(refs):
            if not isinstance(ref, dict):
                out.append(Finding("MDT-SCHEMA-007","ERROR",f"Referência {i+1} inválida: cada referência deve ser um objeto.")); break
            for field in ("id","author","year","title","type"):
                if field in ref and not isinstance(ref[field], str):
                    out.append(Finding("MDT-SCHEMA-008","ERROR",f"Referência {i+1}: campo {field} deve ser texto.")); break
    if not isinstance(data.get("assets", []), list):
        out.append(Finding("MDT-SCHEMA-009","ERROR","assets deve ser uma lista."))
    return out

def validate(data):
    out=_shape_findings(data)
    if any(x.severity=="ERROR" for x in out):
        return out
    profile=load_profile(data["type"]); meta=data.get("metadata", {})
    for field in profile.get("required_metadata", []):
        if not meta.get(field):
            out.append(Finding(f"MDT-CONFIG-{field.upper()}","ERROR",f"Campo obrigatório ausente: {field}"))
    if not data.get("sections"):
        out.append(Finding("MDT-STRUCT-001","WARNING","Nenhuma seção textual foi informada; o gerador usará uma estrutura mínima."))
    if not data.get("references"):
        out.append(Finding("MDT-REF-001","INFO","Nenhuma referência foi fornecida; a saída poderá conter uma bibliografia mínima técnica."))
    return out
