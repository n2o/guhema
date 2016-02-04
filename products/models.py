# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Indicator(models.Model):
    """
    Definiere Kennziffern, welche für die Sägeblätter notwendig sind.
    """
    value = models.CharField(_("Kennziffer"), max_length=1024, blank=False)
    width = models.IntegerField(_("Breite (in mm)"), blank=True, default=0)
    strength = models.FloatField(_("Stärke (in mm)"), blank=True, default=0)
    length = models.IntegerField(_("Länge (in mm)"), blank=True, default=0)
    diameter = models.CharField(_("Durchmesser (in mm)"), max_length=255, blank=True, default="")
    C = models.BooleanField("C", blank=True, default=False)
    E = models.BooleanField("E", blank=True, default=False)
    G = models.BooleanField("G", blank=True, default=False)
    H = models.BooleanField("H", blank=True, default=False)
    I = models.BooleanField("I", blank=True, default=False)
    J = models.BooleanField("J", blank=True, default=False)
    L = models.BooleanField("L", blank=True, default=False)
    M = models.BooleanField("M", blank=True, default=False)
    N = models.BooleanField("N", blank=True, default=False)
    O = models.BooleanField("O", blank=True, default=False)
    T = models.BooleanField("T", blank=True, default=False)
    U = models.BooleanField("U", blank=True, default=False)
    V = models.BooleanField("V", blank=True, default=False)
    W = models.BooleanField("W", blank=True, default=False)
    UE = models.BooleanField("Ü", blank=True, default=False)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = _('Kennziffer')
        verbose_name_plural = _('Kennziffern')
        ordering = ('value',)
        app_label = 'products'


class Clamping(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=False)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField(_("Bild"), null=True, blank=True, upload_to='blades/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Aufnahme')
        verbose_name_plural = _('Aufnahmen')
        app_label = 'products'


class ProductGroup(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=False)
    description = models.TextField(_("Beschreibung"), max_length=1024, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField(_("Produktabbildung"), null=True, blank=True, upload_to='blades/')
    public = models.BooleanField(_("Öffentlich?"), default=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Produktgruppe')
        verbose_name_plural = _('Produktgruppen')
        app_label = 'products'


class SawBlade(models.Model):
    quality = models.CharField(_("Stahlsorte"), max_length=255, blank=False)
    type = models.CharField(_("Typ"), max_length=255, blank=True)
    name = models.CharField(_("Bezeichnung"), max_length=255, blank=True)
    description = models.TextField(_("Beschreibung"), max_length=1024, blank=True)
    group = models.ForeignKey(ProductGroup, verbose_name=_("Produktgruppe"), null=True, blank=True)
    clamping = models.ForeignKey(Clamping, verbose_name=_("Aufnahme"), null=True, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField(_("Produktabbildung"), null=True, blank=True, upload_to='blades/')
    indicators = models.ManyToManyField(Indicator, verbose_name=_("Kennziffern"), blank=True)

    def __str__(self):
        return self.quality

    class Meta:
        verbose_name = _('Sägeblatt')
        verbose_name_plural = _('Sägeblätter')
        app_label = 'products'


class SableSawBlade(SawBlade):
    toothing = models.CharField(_("Verzahnung"), max_length=255, blank=True)
    cutting_metal = models.CharField(_("Schnittbereich Metall"), max_length=255, blank=True, default=None, null=True)
    cutting_wood = models.CharField(_("Schnittbereich Holz"), max_length=255, blank=True, default=None, null=True)
    cutting_minerals = models.CharField(_("Schnittbereich Mineralisch"), max_length=255, blank=True, default=None, null=True)

    class Meta:
        verbose_name = _('Säbelsägeblatt')
        verbose_name_plural = _('Säbelsägeblätter')
        app_label = 'products'


class HackSawBlade(SableSawBlade):
    accessory = models.BooleanField(_("Zubehörartikel?"), default=False, blank=False)
    subcategory = models.CharField(_("Unterkategorie"), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Metallhandsägeblatt')
        verbose_name_plural = _('Metallhandsägeblätter')
        app_label = 'products'


class HoleSaw(models.Model):
    ordernr = models.CharField(_("Bestellnr."), max_length=1024, blank=False)
    image = models.ImageField(_("Abbildung"), blank=True, upload_to='blades/')
    description = models.TextField(_("Beschreibung"), max_length=1024, blank=True)
    category = models.CharField(_("Kategorie"), max_length=1024, blank=True)
    mounting = models.CharField(_("Aufnahmeschaft"), max_length=1024, blank=True)
    saw_length = models.CharField(_("Lochsägenlänge (in mm)"), max_length=1024, blank=True)
    pilot_drill_length = models.CharField(_("Zentrierbohrerlänge (in mm)"), max_length=1024, blank=True)
    quality = models.CharField(_("Stahlsorte"), max_length=255, blank=True)
    toothing = models.CharField(_("Verzahnung"), max_length=255, blank=True)

    def __str__(self):
        return self.ordernr

    class Meta:
        verbose_name = _('Lochsäge')
        verbose_name_plural = _('Lochsägen')
        app_label = 'products'


class HoleSawDiameter(models.Model):
    diameter = models.IntegerField(_("Durchmesser (in mm)"), blank=False)
    blades = models.ManyToManyField(HoleSaw, verbose_name=_("Lochsäge"), blank=True)
    advice = models.BooleanField(_("Aus Empfehlungstabelle?"), default=True, blank=True)
    niro = models.IntegerField(_("NIRO"), null=True, blank=True)
    iron = models.IntegerField(_("Guss"), null=True, blank=True)
    steel = models.IntegerField(_("Stahl"), null=True, blank=True)
    non_ferrous_metals = models.IntegerField(_("Buntmetalle"), null=True, blank=True)
    alu = models.IntegerField(_("Alu"), null=True, blank=True)

    def __str__(self):
        return str(self.diameter)

    class Meta:
        verbose_name = _('Lochsägen-Durchmesser')
        verbose_name_plural = _('Lochsägen-Durchmesser')
        app_label = 'products'


class BandSawBladeIndicator(models.Model):
    value = models.CharField(_("Kennziffer"), max_length=255, blank=False)
    width = models.IntegerField(_("Breite (in mm)"), blank=True, default=0)
    strength = models.FloatField(_("Stärke (in mm)"), blank=True, default=0)
    A = models.CharField("A", max_length=255, blank=True)
    C = models.CharField("C", max_length=255, blank=True)
    E = models.CharField("E", max_length=255, blank=True)
    F = models.CharField("F", max_length=255, blank=True)
    G = models.CharField("G", max_length=255, blank=True)
    H = models.CharField("H", max_length=255, blank=True)
    I = models.CharField("I", max_length=255, blank=True)
    J = models.CharField("J", max_length=255, blank=True)
    L = models.CharField("L", max_length=255, blank=True)
    N = models.CharField("N", max_length=255, blank=True)
    O = models.CharField("O", max_length=255, blank=True)
    S = models.CharField("S", max_length=255, blank=True)
    T = models.CharField("T", max_length=255, blank=True)
    U = models.CharField("U", max_length=255, blank=True)
    V = models.CharField("V", max_length=255, blank=True)
    W = models.CharField("W", max_length=255, blank=True)
    X = models.CharField("X", max_length=255, blank=True)
    Y = models.CharField("Y", max_length=255, blank=True)
    Z = models.CharField("Z", max_length=255, blank=True)
    AE = models.CharField("Ä", max_length=255, blank=True)
    UE = models.CharField("Ü", max_length=255, blank=True)
    star_p = models.CharField("*P", max_length=255, blank=True)
    RP = models.CharField("RP", max_length=255, blank=True)
    SP = models.CharField("SP", max_length=255, blank=True)
    TP = models.CharField("TP", max_length=255, blank=True)
    UP = models.CharField("UP", max_length=255, blank=True)
    VP = models.CharField("VP", max_length=255, blank=True)
    WP = models.CharField("WP", max_length=255, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('Sägeband-Kennziffer')
        verbose_name_plural = _('Sägeband-Kennziffern')
        app_label = 'products'


class BandSawBlade(SawBlade):
    bandsaw_indicators = models.ManyToManyField(BandSawBladeIndicator, verbose_name=_("Kenziffern"), blank=True)
    type_description = models.CharField(_("Typ Beschreibung"), max_length=255, blank=True)
    type2 = models.CharField(_("2. Typ"), max_length=255, blank=True)
    type2_description = models.CharField(_("2. Typ Beschreibung"), max_length=255, blank=True)
    image2 = models.ImageField(_("2. Produktabbildung"), null=True, blank=True, upload_to='blades/')
    heading = models.CharField(_("Seitentitel"), max_length=255, blank=True)
    cols = models.CharField(_("Spalten"), max_length=1024, blank=True)

    class Meta:
        verbose_name = _('Sägeband')
        verbose_name_plural = _('Sägebänder')
        app_label = 'products'


class JigSawBlade(SawBlade):
    subcategory = models.CharField(_("Unterkategorie"), max_length=255, blank=True)
    tooth_separation = models.FloatField(_("Zahnteilung (ZpZ)"), blank=True)
    length = models.IntegerField(_("Sägeblattlänge (in mm)"), default=0, blank=True)
    cutting_metal = models.CharField(_("Schnittbereich Metall (in mm)"), max_length=255, blank=True)
    cutting_wood = models.CharField(_("Schnittbereich Holz (in mm)"), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Pendelhubstichsägeblatt')
        verbose_name_plural = _('Pendelhubstichsägeblätter')
        app_label = 'products'


class CircularSawBladeIndicator(models.Model):
    value = models.CharField(_("Kennziffer"), max_length=255, blank=False)
    diameter = models.IntegerField(_("Durchmesser (in mm)"), blank=True)
    strength = models.FloatField(_("Stärke (in mm)"), blank=True)
    bore = models.IntegerField(_("Bohrung (in mm)"), blank=True)
    BW_3 = models.IntegerField("BW 3 mm", default=0, blank=True)
    BW_4 = models.IntegerField("BW 4 mm", default=0, blank=True)
    HZ_5 = models.IntegerField("HZ 5 mm", default=0, blank=True)
    HZ_6 = models.IntegerField("HZ 6 mm", default=0, blank=True)
    BW_7 = models.IntegerField("BW 7 mm", default=0, blank=True)
    HZ_8 = models.IntegerField("HZ 8 mm", default=0, blank=True)
    HZ_9 = models.IntegerField("HZ 9 mm", default=0, blank=True)
    HZ_10 = models.IntegerField("HZ 10 mm", default=0, blank=True)
    HZ_12 = models.IntegerField("HZ 12 mm", default=0, blank=True)
    HZ_14 = models.IntegerField("HZ 14 mm", default=0, blank=True)
    NL = models.CharField("NL in mm", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = _('Metallkreissägeblatt-Kennziffer')
        verbose_name_plural = _('Metallkreissägeblatt-Kennziffern')
        app_label = 'products'


class CircularSawBlade(SawBlade):
    circular_indicators = models.ManyToManyField(CircularSawBladeIndicator, verbose_name=_("Kenziffern"), blank=True)

    class Meta:
        verbose_name = _('Metallkreissägeblatt')
        verbose_name_plural = _('Metallkreissägeblätter')
        app_label = 'products'
