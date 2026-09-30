import argparse,json
from pathlib import Path
from .generator import generate
from .model import Document
from .profiles import list_profiles
from .validator import validate
def main():
    p=argparse.ArgumentParser(prog="ufsm-mdt"); s=p.add_subparsers(dest="command",required=True); s.add_parser("types")
    g=s.add_parser("generate"); g.add_argument("input",type=Path); g.add_argument("output",type=Path)
    v=s.add_parser("validate"); v.add_argument("input",type=Path); a=p.parse_args()
    if a.command=="types": print("\n".join(list_profiles())); return 0
    d=json.loads(a.input.read_text(encoding="utf-8"))
    if a.command=="validate":
        f=validate(d); [print(f"{x.severity}: {x.rule_id}: {x.message}") for x in f]; return int(any(x.severity=="ERROR" for x in f))
    generate(Document.from_dict(d),a.output); return 0
if __name__=="__main__": raise SystemExit(main())
