from dataclasses import dataclass, field

@dataclass
class Document:
    type: str
    metadata: dict = field(default_factory=dict)
    sections: list = field(default_factory=list)
    references: list | str = field(default_factory=list)
    assets: list = field(default_factory=list)

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("Documento deve ser um objeto JSON")
        return cls(
            data.get("type", ""),
            data.get("metadata", {}) if isinstance(data.get("metadata", {}), dict) else {},
            data.get("sections", []) if isinstance(data.get("sections", []), list) else [],
            data.get("references", []),
            data.get("assets", []) if isinstance(data.get("assets", []), list) else [],
        )

    def to_dict(self):
        return {"type": self.type, "metadata": self.metadata, "sections": self.sections, "references": self.references, "assets": self.assets}
