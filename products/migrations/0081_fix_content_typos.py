"""Fix typos in product, Lochsägen and legal-page content, found in a proofreading pass (2026-10-26)."""
from django.db import migrations
from django.db.models import Value
from django.db.models.functions import Replace

# (app, model, field, wrong, right) — applied to every row that still contains the wrong text.
# Product descriptions are fixed in the German column and the untranslated base column.
TEXT_FIXES = [
    ('products', 'ProductGroup', 'description', 'Lebensdauer von Sägeblatt und Maschine wird auch', 'Lebensdauer von Sägeblatt und Maschine werden auch'),
    ('products', 'ProductGroup', 'description', 'Den adäquaten Nutzen', 'Der adäquate Nutzen'),
    ('products', 'ProductGroup', 'description', 'Lebensdauer von Sägeband und Maschine wird auch', 'Lebensdauer von Sägeband und Maschine werden auch'),
    ('products', 'ProductGroup', 'description', 'Kunst- stoffe', 'Kunststoffe'),
    ('products', 'ProductGroup', 'description', 'dampf\xad angelassen', 'dampfangelassen'),
    ('products', 'ProductGroup', 'description', 'GUHEMA – Säbel- und Spezialsäbelsägeblätter', 'GUHEMA-Säbel- und Spezialsäbelsägeblätter'),
    ('products', 'SawBlade', 'description', 'leicht zerpanbare Werkstoffe', 'leicht zerspanbare Werkstoffe'),
    ('products', 'SawBlade', 'description', 'Pulverbeschichtetes, Reckteckrohr', 'Pulverbeschichtetes Rechteckrohr'),
    ('products', 'SawBlade', 'description', 'gefertigt aus\n* Bi-Metall, erzielt', 'gefertigt aus Bi-Metall, erzielt'),
    ('products', 'SawBlade', 'description', 'beidseitigem, sauberen Schnittkantenverlauf', 'beidseitigem, sauberem Schnittkantenverlauf'),
    ('products', 'SawBlade', 'description', 'und beschichteten Platten', 'und beschichtete Platten'),
    ('products', 'SawBlade', 'description', 'Zahn- und Rückengehärtetes Sägeband', 'Zahn- und rückengehärtetes Sägeband'),
    ('products', 'SawBlade', 'description', '* rechteckige Hartmetallverzahnung', '* Rechteckige Hartmetallverzahnung'),
    ('products', 'SawBlade', 'description', '2-Komponenten Kunststoffgriff', '2-Komponenten-Kunststoffgriff'),
    ('products', 'SawBlade', 'description', 'GUHEMA Bi-Metall Handsägeblatt', 'GUHEMA Bi-Metall-Handsägeblatt'),
    ('products', 'SawBlade', 'description', '"Memoryeffekt"', '„Memoryeffekt“'),
    ('products', 'JigSawBlade', 'cutting_metal', '1,5 -3', '1,5 - 3'),
    ('flatpages', 'FlatPage', 'content', 'welche personenbezogene Daten', 'welche personenbezogenen Daten'),
    ('flatpages', 'FlatPage', 'content', 'Eine darüberhinausgehende Speicherung', 'Eine darüber hinausgehende Speicherung'),
    ('flatpages', 'FlatPage', 'content', 'in der Eingabemaske eingegeben Daten', 'in der Eingabemaske eingegebenen Daten'),
    ('flatpages', 'FlatPage', 'content', 'Session Cookies ist erforderlich', 'Session-Cookies ist erforderlich'),
    ('flatpages', 'FlatPage', 'content', 'auf Ihrem Endgerät dienen in der Regel', 'auf Ihrem Endgerät und dienen in der Regel'),
    ('flatpages', 'FlatPage', 'content', 'nicht auf Ihrem Endgerät ablegt werden können', 'nicht auf Ihrem Endgerät abgelegt werden können'),
    ('flatpages', 'FlatPage', 'content', 'im Sinne der. DSGVO', 'im Sinne der DSGVO'),
    ('flatpages', 'FlatPage', 'content', 'die im weiteren beschrieben Rechte', 'die im Weiteren beschriebenen Rechte'),
    ('flatpages', 'FlatPage', 'content', 'Sie haben das Recht die Einschränkung', 'Sie haben das Recht, die Einschränkung'),
    ('flatpages', 'FlatPage', 'content', 'das Recht, dass die sie betreffenden', 'das Recht, dass die Sie betreffenden'),
    ('flatpages', 'FlatPage', 'content', 'Sie widerrufen ihre Einwilligung', 'Sie widerrufen Ihre Einwilligung'),
    ('flatpages', 'FlatPage', 'content', 'das Recht diese Daten', 'das Recht, diese Daten'),
    ('flatpages', 'FlatPage', 'content', 'GmbH & Co.KG', 'GmbH & Co. KG'),
]
TRANSLATED = {("products", "ProductGroup", "description"), ("products", "SawBlade", "description")}


def fix_content(apps, schema_editor):
    for app, model, field, wrong, right in TEXT_FIXES:
        manager = apps.get_model(app, model).objects
        fields = [field, f"{field}_de"] if (app, model, field) in TRANSLATED else [field]
        # content was entered both with Unix and Windows line breaks
        for f in fields:
            for w, r in {(wrong, right), (wrong.replace("\n", "\r\n"), right.replace("\n", "\r\n"))}:
                manager.filter(**{f"{f}__contains": w}).update(**{f: Replace(f, Value(w), Value(r))})

    # Ø 57 was entered twice in the hole saw recommendation table; the one between 65 and 68 is 67
    HoleSawDiameter = apps.get_model("products", "HoleSawDiameter")
    HoleSawDiameter.objects.filter(diameter=57, advice=True, niro=65, iron=85, steel=130).update(diameter=67)

    # Decimal comma like all other dimensions
    Indicator = apps.get_model("products", "Indicator")
    Indicator.objects.filter(diameter__contains=".").update(diameter=Replace("diameter", Value("."), Value(",")))


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0080_sync_model_state"),
        ("flatpages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(fix_content, migrations.RunPython.noop),
    ]
