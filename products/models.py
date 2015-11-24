# -*- coding: utf-8 -*-
from django.db import models


class Indicator(models.Model):
    value = models.CharField("Kennziffer", max_length=1024, blank=False)
    hss = models.BooleanField("HSS?", blank=True, default=False)
    width = models.FloatField("Breite", blank=True, default=0)
    strength = models.FloatField("Stärke", blank=True, default=0)
    length = models.FloatField("Länge", blank=True, default=0)
    diameter = models.FloatField("Durchmesser", blank=True, default=0.0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Kennziffer'
        verbose_name_plural = 'Kennziffer'
        ordering = ('value',)


class SawBlade(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    description = models.CharField("Beschreibung", max_length=255, blank=False)
    quality = models.CharField("Qualität", max_length=255, blank=False)
    indicators = models.ManyToManyField(Indicator, verbose_name="Kennziffern")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maschinensägeblatt'
        verbose_name_plural = 'Maschinensägeblätter'