"""One-off export of the Django database to JSON for the Astro site.

Run: uv run python manage.py shell < tools/export_json.py   (DB path via settings)
Translated fields become {"de", "en", "ru"}; image fields become media paths;
FKs become ids, M2M become id lists. Delete together with Django after cutover.
"""
import json
from pathlib import Path

from django.contrib.flatpages.models import FlatPage
from django.db import models
from modeltranslation.translator import NotRegistered, translator

from products.models import (BandSawBladeIndicator, CircularSawBladeIndicator, Clamping, HoleSaw,
                             HoleSawDiameter, Indicator, ProductGroup, SawBlade)

LANGS = ("de", "en", "ru")
OUT = Path("src/data")
SUBCLASS_PATH = [  # most specific first
    ("hacksawblade", ("sablesawblade", "hacksawblade")),
    ("sablesawblade", ("sablesawblade",)),
    ("bandsawblade", ("bandsawblade",)),
    ("jigsawblade", ("jigsawblade",)),
    ("circularsawblade", ("circularsawblade",)),
]


def translated(model):
    try:
        return set(translator.get_options_for_model(model).all_fields)
    except NotRegistered:
        return set()


def plain(value):
    if isinstance(value, models.fields.files.FieldFile):
        return (value.name or "").removeprefix("./") or None
    return value


def dump(obj):
    model = type(obj)
    trans = translated(model)
    skip = {f"{name}_{lang}" for name in trans for lang in LANGS}
    out = {}
    for field in model._meta.concrete_fields:
        if field.name in skip or field.one_to_one:
            continue
        if field.name in trans:
            out[field.name] = {lang: plain(getattr(obj, f"{field.name}_{lang}")) or None for lang in LANGS}
        elif field.is_relation:
            out[field.name] = getattr(obj, field.attname)
        else:
            out[field.name] = plain(getattr(obj, field.name))
    for field in model._meta.many_to_many:
        out[field.name] = list(getattr(obj, field.name).values_list("id", flat=True))  # Django default order
    return out


def most_specific(blade):
    for kind, chain in SUBCLASS_PATH:
        obj = blade
        try:
            for attr in chain:
                obj = getattr(obj, attr)
        except models.ObjectDoesNotExist:
            continue
        return kind, obj
    return "sawblade", blade


def write(name, rows):
    (OUT / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1, default=str) + "\n")


OUT.mkdir(parents=True, exist_ok=True)
blades = []
for blade in SawBlade.objects.order_by("id"):
    kind, obj = most_specific(blade)
    blades.append({"kind": kind, **dump(obj)})
write("sawblades", blades)
for name, model in [("productgroups", ProductGroup), ("clampings", Clamping), ("indicators", Indicator),
                    ("holesaws", HoleSaw), ("holesawdiameters", HoleSawDiameter),
                    ("bandsawindicators", BandSawBladeIndicator),
                    ("circularindicators", CircularSawBladeIndicator)]:
    write(name, [dump(o) for o in model.objects.order_by("id")])

pages = Path("src/content/pages")
pages.mkdir(parents=True, exist_ok=True)
for page in FlatPage.objects.all():
    slug = page.url.strip("/")
    (pages / f"{slug}.md").write_text(f"---\ntitle: {json.dumps(page.title, ensure_ascii=False)}\n---\n\n{page.content.strip()}\n")
print("exported", len(blades), "blades")
