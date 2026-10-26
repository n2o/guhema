from datetime import timedelta

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50, blank=False)
    intro = models.TextField(_('Kurzbeschreibung'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Kategorie')
        verbose_name_plural = _('Kategorien')


# News older than this is not shown anywhere; with nothing newer the news section disappears
NEWS_MAX_AGE = timedelta(days=365)


class EntryQuerySet(models.QuerySet):
    def current(self):
        return self.filter(public=True, created__gte=timezone.now() - NEWS_MAX_AGE)


class Entry(models.Model):
    title = models.CharField(_('Titel'), max_length=50, blank=False)
    author = models.ForeignKey(User, null=True, blank=True, verbose_name=_("Autor"), on_delete=models.SET_NULL)
    content = models.TextField(_('Inhalt'), blank=False)
    image = models.ImageField(_('Bild'), null=True, blank=True)
    attachment = models.FileField(_('Anhang'), null=True, blank=True)
    slug = AutoSlugField(null=True, populate_from='title')
    archive = models.BooleanField(_('Archiviert?'), default=False)
    public = models.BooleanField(_('Öffentlich?'), default=True)
    created = models.DateTimeField(_('Erstellt am'), default=timezone.now)
    category = models.ForeignKey(Category, null=True, verbose_name=_("Kategorie"), on_delete=models.SET_NULL)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', args=[self.slug])

    class Meta:
        verbose_name = _('Eintrag')
        verbose_name_plural = _('Einträge')
        ordering = ('created',)
