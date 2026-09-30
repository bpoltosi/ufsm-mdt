#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROFILE_DIR=ROOT/"profiles"
OUTPUT=ROOT/"site"/"data"/"profiles.json"
def main():
    profiles=[]
    for path in sorted(PROFILE_DIR.glob("*.json")):
        data=json.loads(path.read_text(encoding="utf-8"))
        profiles.append({"id":data["id"],"name":data["name"],"source":data.get("source",""),"template_command":data.get("template_command",""),"required_metadata_count":len(data.get("required_metadata",[])),"notes":data.get("notes","")})
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps({"version":1,"profiles":profiles},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()