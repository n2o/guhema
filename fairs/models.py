from datetime import datetime

from autoslug import AutoSlugField
from django.db import models


class Fair(models.Model):
    name = models.CharField('Name der Messe', max_length=255, blank=False)
    website = models.URLField('Veranstaltungswebsite', blank=True)
    location = models.TextField('Veranstaltungsort', blank=True)
    hall = models.CharField('Halle', max_length=255, blank=True)
    stand = models.CharField('Stand', max_length=255, blank=True)
    start = models.DateField('Beginn', blank=False)
    end = models.DateField('Ende', blank=False)
    description = models.TextField('Beschreibung', blank=True)
    image = models.ImageField('Bild', null=True, blank=True)
    attachment = models.FileField('Anhang', null=True, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    archive = models.BooleanField('Archiviert?', default=False)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Messe'
        verbose_name_plural = 'Messen'
        ordering = ('created',)
