from dataclasses import dataclass
from .profiles import load_profile
@dataclass(frozen=True)
class Finding: rule_id:str; severity:str; message:str
def validate(data):
    out=[]; profile=load_profile(data.get("type","")); meta=data.get("metadata",{})
    for field in profile.get("required_metadata",[]):
        if not meta.get(field): out.append(Finding(f"MDT-CONFIG-{field.upper()}","ERROR",f"Campo obrigatório ausente: {field}"))
    if not data.get("sections"): out.append(Finding("MDT-STRUCT-001","WARNING","Nenhuma seção textual foi informada; o gerador usará uma estrutura mínima."))
    if not data.get("references"): out.append(Finding("MDT-REF-001","INFO","Nenhuma referência foi fornecida; um registro mínimo será criado."))
    return out
