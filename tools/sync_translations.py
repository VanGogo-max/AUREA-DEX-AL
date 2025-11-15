#!/usr/bin/env python3
# tools/sync_translations.py
import json
from pathlib import Path

# папка с преводите в frontend
T_DIR = Path('frontend/translations')
BASE = T_DIR / 'en.json'
LANGS = ["en","bg","ru","es","pt","de","fr","it","nl","pl","tr","ar","zh","ja","ko","hi","vi","sv","no","he"]

def load(p):
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}

def main():
    if not T_DIR.exists():
        print("Не намерих frontend/translations — провери пътя.")
        return
    base = load(BASE)
    if not base:
        print("Не намерих en.json или е празен.")
        return
    for lang in LANGS:
        p = T_DIR / f"{lang}.json"
        cur = load(p)
        changed = False
        for k,v in base.items():
            if k not in cur:
                cur[k] = "__MISSING__ " + v
                changed = True
        # remove keys not in base? we keep extras
        if changed:
            p.write_text(json.dumps(cur, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"Updated {lang}.json — added {len([1 for k in base if k not in cur])} keys")
        else:
            print(f"{lang}.json - OK")
    print("Синхронизация готова. Прегледай и преведи '__MISSING__' стойностите, ако желаеш.")

if __name__ == "__main__":
    main()
