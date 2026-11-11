"""Collect every translatable text of the site into one worklist per language, and apply reviewed results.

  python3 tools/translations.py export <lang> <out.json>   # [{"id", "de", "current"}]
  python3 tools/translations.py apply <lang> <in.json>     # {"id": "new text"}

ids: "ui:<msgid>" for src/i18n/<lang>.json, "<file>:<row id>:<field>" for translated fields in src/data/*.json.
UI msgids are the t(lang, "...") keys used in src/ (unused dictionary entries are dropped on apply).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src/data"
DICT = ROOT / "src/i18n"
IMG = re.compile(r"\.(png|jpe?g|gif|webp|pdf)$", re.I)
LITERAL = re.compile(r"""(["'`])((?:\\.|(?!\1).)*?)\1""")
T_CALL = re.compile(r"""\bt\(\s*lang\s*,\s*(["'`])((?:\\.|(?!\1).)*)\1""", re.S)


def unquote(literal):
    return literal.replace("\\'", "'").replace('\\"', '"')


def used_msgids():
    """Literal t(lang, "...") keys, plus any string literal that is a known msgid (keys passed via variables)."""
    known = set(json.loads((DICT / "en.json").read_text())) | set(json.loads((DICT / "ru.json").read_text()))
    keys = set()
    for f in [*(ROOT / "src").rglob("*.astro"), *(ROOT / "src").rglob("*.ts")]:
        text = f.read_text()
        keys |= {unquote(m.group(2)) for m in T_CALL.finditer(text)}
        keys |= {unquote(m.group(2)) for m in LITERAL.finditer(text)} & known
    return keys


def data_fields():
    for f in sorted(DATA.glob("*.json")):
        for row in json.loads(f.read_text()):
            for field, value in row.items():
                if isinstance(value, dict) and set(value) == {"de", "en", "ru"} and value["de"] and not IMG.search(value["de"]):
                    yield f"{f.stem}:{row['id']}:{field}", value


def export(lang, out):
    d = json.loads((DICT / f"{lang}.json").read_text())
    items = [{"id": f"ui:{k}", "de": k.split("|")[-1], "current": d.get(k)} for k in sorted(used_msgids())]
    seen = {}
    for id_, value in data_fields():  # same German text → translate once
        if value["de"] in seen:
            continue
        seen[value["de"]] = id_
        items.append({"id": id_, "de": value["de"], "current": value[lang]})
    Path(out).write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n")
    print(len(items), "items")


def apply(lang, inp):
    new = json.loads(Path(inp).read_text())
    path = DICT / f"{lang}.json"
    d = json.loads(path.read_text())
    keys = used_msgids()
    d = {k: new.get(f"ui:{k}", d.get(k)) for k in sorted(keys) if new.get(f"ui:{k}", d.get(k))}
    path.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    by_de = {}
    for id_, value in data_fields():
        by_de.setdefault(value["de"], new.get(id_))
    for f in sorted(DATA.glob("*.json")):
        rows = json.loads(f.read_text())
        for row in rows:
            for value in row.values():
                if isinstance(value, dict) and set(value) == {"de", "en", "ru"} and by_de.get(value["de"]):
                    value[lang] = by_de[value["de"]]
        f.write_text(json.dumps(rows, ensure_ascii=False, indent=1, default=str) + "\n")
    print("applied", lang)


if __name__ == "__main__":
    {"export": export, "apply": apply}[sys.argv[1]](sys.argv[2], sys.argv[3])
