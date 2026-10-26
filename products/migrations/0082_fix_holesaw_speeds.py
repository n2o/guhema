"""Hole saw recommended speeds that differ from the GUHEMA catalogue (de/en/ru agree)."""
from django.db import migrations

# diameter: {field: (wrong, right)}
SPEED_FIXES = {
    24: {"non_ferrous_metals": (395, 495)},
    46: {"steel": (170, 190), "non_ferrous_metals": (230, 250), "alu": (255, 285)},
    54: {"non_ferrous_metals": (200, 210), "alu": (225, 240)},
}


def fix_speeds(apps, schema_editor):
    HoleSawDiameter = apps.get_model("products", "HoleSawDiameter")
    for diameter, fields in SPEED_FIXES.items():
        for field, (wrong, right) in fields.items():
            HoleSawDiameter.objects.filter(advice=True, diameter=diameter, **{field: wrong}).update(**{field: right})


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0081_fix_content_typos"),
    ]

    operations = [
        migrations.RunPython(fix_speeds, migrations.RunPython.noop),
    ]
