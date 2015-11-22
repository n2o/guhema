# -*- coding: utf-8 -*-
from django.db import models


class Tooth(models.Model):
    C = models.CharField("C", max_length=255, blank=True)
    E = models.CharField("E", max_length=255, blank=True)
    G = models.CharField("G", max_length=255, blank=True)
    H = models.CharField("H", max_length=255, blank=True)
    I = models.CharField("I", max_length=255, blank=True)
    J = models.CharField("J", max_length=255, blank=True)
    L = models.CharField("L", max_length=255, blank=True)
    M = models.CharField("M", max_length=255, blank=True)
    N = models.CharField("N", max_length=255, blank=True)
    O = models.CharField("O", max_length=255, blank=True)
    U = models.CharField("U", max_length=255, blank=True)
    V = models.CharField("V", max_length=255, blank=True)
    W = models.CharField("W", max_length=255, blank=True)
    UE = models.CharField("Ü", max_length=255, blank=True)


class Indicator(models.Model):
    indicator = models.CharField("Kennziffer", max_length=255, blank=False)
    size = models.CharField("Abmessung in mm", max_length=255, blank=True)
    value = models.IntegerField("Wert", blank=False)
    diameter = models.FloatField("Durchmesser", blank=False)
    teeth = models.ManyToManyField(Tooth)

    def __str__(self):
        return self.indicator


class SawBlade(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    description = models.CharField("Beschreibung", max_length=255, blank=False)
    quality = models.CharField("Qualität", max_length=255, blank=False)
    indicators = models.ManyToManyField(Indicator)

    def __str__(self):
        return self.name