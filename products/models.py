# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from django.db import models


class Indicator(models.Model):
    value = models.CharField("Kennziffer", max_length=1024, blank=False)
    width = models.IntegerField("Breite", blank=True, default=0)
    strength = models.FloatField("Stärke", blank=True, default=0)
    length = models.IntegerField("Länge", blank=True, default=0)
    diameter = models.CharField("Durchmesser", max_length=255, blank=True, default="")
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
        verbose_name = 'Kennziffer'
        verbose_name_plural = 'Kennziffer'
        ordering = ('value',)


class Clamping(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField("Bild", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aufnahme'
        verbose_name_plural = 'Aufnahmen'


class ProductGroup(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    description = models.TextField("Beschreibung", max_length=1024, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField("Produktabbildung", null=True, blank=True)
    public = models.BooleanField("Öffentlich?", default=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produktgruppe'
        verbose_name_plural = 'Produktgruppen'


class SawBlade(models.Model):
    quality = models.CharField("Stahlsorte", max_length=255, blank=False)
    name = models.CharField("Bezeichnung", max_length=255, blank=True)
    description = models.TextField("Beschreibung", max_length=1024, blank=True)
    group = models.ForeignKey(ProductGroup, verbose_name="Produktgruppe", null=True, blank=True)
    clamping = models.ForeignKey(Clamping, verbose_name="Aufnahme", null=True, blank=True)
    type = models.CharField("Typ", max_length=255, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField("Produktabbildung", null=True, blank=True)
    indicators = models.ManyToManyField(Indicator, verbose_name="Kennziffern", blank=True)

    def __str__(self):
        return self.quality

    class Meta:
        verbose_name = 'Sägeblatt'
        verbose_name_plural = 'Sägeblätter'


class SableSawBlade(SawBlade):
    toothing = models.CharField("Verzahnung", max_length=255, blank=True)
    cutting_metal = models.CharField("Schnittbereich Metall", max_length=255, blank=True, default=None, null=True)
    cutting_wood = models.CharField("Schnittbereich Holz", max_length=255, blank=True, default=None, null=True)
    cutting_minerals = models.CharField("Schnittbereich Mineralisch", max_length=255, blank=True, default=None, null=True)

    class Meta:
        verbose_name = 'Säbelsägeblatt'
        verbose_name_plural = 'Säbelsägeblätter'


class HackSawBlade(SableSawBlade):
    accessory = models.BooleanField("Zubehörartikel?", default=False, blank=False)

    class Meta:
        verbose_name = 'Metallhandsägeblatt'
        verbose_name_plural = 'Metallhandsägeblätter'


class HoleSawDiameter(models.Model):
    diameter = models.IntegerField("Durchmesser in mm", blank=False)

    def __str__(self):
        return self.diameter

    class Meta:
        verbose_name = 'Durchmesser'
        verbose_name_plural = 'Durchmesser'


class HoleSaw(models.Model):
    ordernr = models.CharField("Bestellnr.", max_length=1024, blank=False)
    image = models.ImageField("Abbildung", blank=True)
    description = models.TextField("Beschreibung", max_length=1024, blank=True)
    category = models.CharField("Kategorie", max_length=1024, blank=True)
    mounting = models.CharField("Aufnahmeschaft", max_length=1024, blank=True)
    saw_length = models.CharField("Lochsägenlänge", max_length=1024, blank=True)
    pilot_drill_length = models.CharField("Zentrierbohrerlänge", max_length=1024, blank=True)
    quality = models.CharField("Stahlsorte", max_length=255, blank=True)
    toothing = models.CharField("Verzahnung", max_length=255, blank=True)
    diameter = models.ManyToManyField(HoleSawDiameter, verbose_name="Durchmesser in mm", blank=True)

    class Meta:
        verbose_name = 'Lochsäge'
        verbose_name_plural = 'Lochsägen'