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


class SawBlade(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    description = models.CharField("Beschreibung", max_length=255, blank=True)
    clamping = models.ForeignKey(Clamping, verbose_name="Aufnahme", null=True, blank=True)
    type = models.CharField("Typ", max_length=255, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    image = models.ImageField("Produktabbildung", null=True, blank=True)
    indicators = models.ManyToManyField(Indicator, verbose_name="Kennziffern", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sägeblatt'
        verbose_name_plural = 'Sägeblätter'