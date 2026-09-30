from dataclasses import dataclass, field
@dataclass
class Document:
    type:str
    metadata:dict=field(default_factory=dict)
    sections:list=field(default_factory=list)
    references:str=""
    assets:list=field(default_factory=list)
    @classmethod
    def from_dict(cls,data): return cls(data["type"],data.get("metadata",{}),data.get("sections",[]),data.get("references",""),data.get("assets",[]))
    def to_dict(self): return {"type":self.type,"metadata":self.metadata,"sections":self.sections,"references":self.references,"assets":self.assets}
