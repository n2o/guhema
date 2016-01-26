from datetime import datetime

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)
    intro = models.TextField('Kurzbeschreibung', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'


class Entry(models.Model):
    title = models.CharField('Titel', max_length=50, blank=False)
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Autor")
    content = models.TextField('Inhalt', blank=False)
    image = models.ImageField('Bild', null=True, blank=True)
    attachment = models.FileField('Anhang', null=True, blank=True)
    slug = AutoSlugField(null=True, populate_from='title')
    archive = models.BooleanField('Archiviert?', default=False)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)
    category = models.ForeignKey('Category', null=True, verbose_name="Kategorie")

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'news:entry', (self.slug,)

    class Meta:
        verbose_name = 'Eintrag'
        verbose_name_plural = 'Einträge'
        ordering = ('created',)
