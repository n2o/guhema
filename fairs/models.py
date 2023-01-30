from datetime import datetime

from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Fair(models.Model):
    name = models.CharField(_('Name der Messe'), max_length=255, blank=False)
    website = models.URLField(_('Veranstaltungswebsite'), blank=True)
    location = models.TextField(_('Veranstaltungsort'), blank=True)
    hall = models.CharField(_('Halle'), max_length=255, blank=True)
    stand = models.CharField(_('Stand'), max_length=255, blank=True)
    start = models.DateField(_('Beginn'), blank=False)
    end = models.DateField(_('Ende'), blank=False)
    description = models.TextField(_('Beschreibung'), blank=True)
    image = models.ImageField(_('Bild'), null=True, blank=True)
    attachment = models.FileField(_('Anhang'), null=True, blank=True)
    slug = AutoSlugField(null=True, populate_from='name')
    archive = models.BooleanField(_('Archiviert?'), default=False)
    public = models.BooleanField(_('Öffentlich?'), default=True)
    created = models.DateTimeField(_('Erstellt am'), default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Messe')
        verbose_name_plural = _('Messen')
        ordering = ('created',)
