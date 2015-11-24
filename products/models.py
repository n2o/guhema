# -*- coding: utf-8 -*-
from django.db import models


class Tooth(models.Model):
    name = models.CharField("Buchstabe", max_length=255, blank=False)
    value = models.CharField("Zahl", max_length=255, blank=False)
    diameter = models.FloatField("Durchmesser", blank=False, default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zahn'
        verbose_name_plural = 'Zähne'


class SawBlade(models.Model):
    name = models.CharField("Name", max_length=255, blank=False)
    description = models.CharField("Beschreibung", max_length=255, blank=False)
    quality = models.CharField("Qualität", max_length=255, blank=False)
    ind_2301 = models.ManyToManyField(Tooth, related_name="ind_2301", blank=True)
    ind_2301_hss = models.BooleanField("HSS?", blank=True)
    ind_2302 = models.ManyToManyField(Tooth, related_name="ind_2302", blank=True)
    ind_2302_hss = models.BooleanField("HSS?", blank=True)
    ind_2352 = models.ManyToManyField(Tooth, related_name="ind_2352", blank=True)
    ind_2352_hss = models.BooleanField("HSS?", blank=True)
    ind_2402 = models.ManyToManyField(Tooth, related_name="ind_2402", blank=True)
    ind_2402_hss = models.BooleanField("HSS?", blank=True)
    ind_3302 = models.ManyToManyField(Tooth, related_name="ind_3302", blank=True)
    ind_3302_hss = models.BooleanField("HSS?", blank=True)
    ind_3352 = models.ManyToManyField(Tooth, related_name="ind_3352", blank=True)
    ind_3352_hss = models.BooleanField("HSS?", blank=True)
    ind_3402 = models.ManyToManyField(Tooth, related_name="ind_3402", blank=True)
    ind_3402_hss = models.BooleanField("HSS?", blank=True)
    ind_3354 = models.ManyToManyField(Tooth, related_name="ind_3354", blank=True)
    ind_3354_hss = models.BooleanField("HSS?", blank=True)
    ind_3404 = models.ManyToManyField(Tooth, related_name="ind_3404", blank=True)
    ind_3404_hss = models.BooleanField("HSS?", blank=True)
    ind_3454 = models.ManyToManyField(Tooth, related_name="ind_3454", blank=True)
    ind_3454_hss = models.BooleanField("HSS?", blank=True)
    ind_4354 = models.ManyToManyField(Tooth, related_name="ind_4354", blank=True)
    ind_4354_hss = models.BooleanField("HSS?", blank=True)
    ind_4404 = models.ManyToManyField(Tooth, related_name="ind_4404", blank=True)
    ind_4404_hss = models.BooleanField("HSS?", blank=True)
    ind_4454 = models.ManyToManyField(Tooth, related_name="ind_4454", blank=True)
    ind_4454_hss = models.BooleanField("HSS?", blank=True)
    ind_4356 = models.ManyToManyField(Tooth, related_name="ind_4356", blank=True)
    ind_4356_hss = models.BooleanField("HSS?", blank=True)
    ind_4406 = models.ManyToManyField(Tooth, related_name="ind_4406", blank=True)
    ind_4406_hss = models.BooleanField("HSS?", blank=True)
    ind_4456 = models.ManyToManyField(Tooth, related_name="ind_4456", blank=True)
    ind_4456_hss = models.BooleanField("HSS?", blank=True)
    ind_4476 = models.ManyToManyField(Tooth, related_name="ind_4476", blank=True)
    ind_4476_hss = models.BooleanField("HSS?", blank=True)
    ind_4409 = models.ManyToManyField(Tooth, related_name="ind_4409", blank=True)
    ind_4409_hss = models.BooleanField("HSS?", blank=True)
    ind_4459 = models.ManyToManyField(Tooth, related_name="ind_4459", blank=True)
    ind_4459_hss = models.BooleanField("HSS?", blank=True)
    ind_4509 = models.ManyToManyField(Tooth, related_name="ind_4509", blank=True)
    ind_4509_hss = models.BooleanField("HSS?", blank=True)
    ind_4559 = models.ManyToManyField(Tooth, related_name="ind_4559", blank=True)
    ind_4559_hss = models.BooleanField("HSS?", blank=True)
    ind_4451 = models.ManyToManyField(Tooth, related_name="ind_4451", blank=True)
    ind_4451_hss = models.BooleanField("HSS?", blank=True)
    ind_4501 = models.ManyToManyField(Tooth, related_name="ind_4501", blank=True)
    ind_4501_hss = models.BooleanField("HSS?", blank=True)
    ind_4551 = models.ManyToManyField(Tooth, related_name="ind_4551", blank=True)
    ind_4551_hss = models.BooleanField("HSS?", blank=True)
    ind_5501 = models.ManyToManyField(Tooth, related_name="ind_5501", blank=True)
    ind_5501_hss = models.BooleanField("HSS?", blank=True)
    ind_5551 = models.ManyToManyField(Tooth, related_name="ind_5551", blank=True)
    ind_5551_hss = models.BooleanField("HSS?", blank=True)
    ind_5571 = models.ManyToManyField(Tooth, related_name="ind_5571", blank=True)
    ind_5571_hss = models.BooleanField("HSS?", blank=True)
    ind_5504 = models.ManyToManyField(Tooth, related_name="ind_5504", blank=True)
    ind_5504_hss = models.BooleanField("HSS?", blank=True)
    ind_5554 = models.ManyToManyField(Tooth, related_name="ind_5554", blank=True)
    ind_5554_hss = models.BooleanField("HSS?", blank=True)
    ind_5574 = models.ManyToManyField(Tooth, related_name="ind_5574", blank=True)
    ind_5574_hss = models.BooleanField("HSS?", blank=True)
    ind_5604 = models.ManyToManyField(Tooth, related_name="ind_5604", blank=True)
    ind_5604_hss = models.BooleanField("HSS?", blank=True)
    ind_5654 = models.ManyToManyField(Tooth, related_name="ind_5654", blank=True)
    ind_5654_hss = models.BooleanField("HSS?", blank=True)
    ind_5704 = models.ManyToManyField(Tooth, related_name="ind_5704", blank=True)
    ind_5704_hss = models.BooleanField("HSS?", blank=True)
    ind_5707 = models.ManyToManyField(Tooth, related_name="ind_5707", blank=True)
    ind_5707_hss = models.BooleanField("HSS?", blank=True)
    ind_5628 = models.ManyToManyField(Tooth, related_name="ind_5628", blank=True)
    ind_5628_hss = models.BooleanField("HSS?", blank=True)
    ind_6658 = models.ManyToManyField(Tooth, related_name="ind_6658", blank=True)
    ind_6658_hss = models.BooleanField("HSS?", blank=True)
    ind_6708 = models.ManyToManyField(Tooth, related_name="ind_6708", blank=True)
    ind_6708_hss = models.BooleanField("HSS?", blank=True)
    ind_6758 = models.ManyToManyField(Tooth, related_name="ind_6758", blank=True)
    ind_6758_hss = models.BooleanField("HSS?", blank=True)
    ind_6801 = models.ManyToManyField(Tooth, related_name="ind_6801", blank=True)
    ind_6801_hss = models.BooleanField("HSS?", blank=True)
    ind_6954 = models.ManyToManyField(Tooth, related_name="ind_6954", blank=True)
    ind_6954_hss = models.BooleanField("HSS?", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sägeblatt'
        verbose_name_plural = 'Sägeblätter'