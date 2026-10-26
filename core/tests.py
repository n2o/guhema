from datetime import date, timedelta

from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from fairs.models import Fair
from news.models import Entry
from products.models import ProductGroup, SawBlade

GROUP_SLUGS = [
    'maschinensageblatter', 'metallstichsageblatter', 'sabel-und-spezialsabelsageblatter',
    'metallhandsageblatter', 'lochsagen', 'metallsagebander', 'pendelhubstichsageblatter',
    'metallkreissageblatter',
]


class SmokeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for slug in GROUP_SLUGS:
            ProductGroup.objects.create(name=slug, slug=slug, public=True)
        group = ProductGroup.objects.get(slug='metallstichsageblatter')
        SawBlade.objects.create(quality='HSS', type='ISD', name='ISD', group=group)
        Entry.objects.create(title='Neuigkeit', content='**Hallo**')
        Entry.objects.create(title='Versteckt', content='geheim', public=False)
        today = date.today()
        Fair.objects.create(name='Messe', description='*Beschreibung*', start=today, end=today + timedelta(days=2))
        page = FlatPage.objects.create(url='/impressum/', title='Impressum', content='Impressum')
        page.sites.add(Site.objects.get_current())

    def assertStatus(self, url, status=200):
        response = self.client.get(url, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, status, url)
        return response

    def test_pages(self):
        for url in ['/', '/unternehmen/', '/news/', '/messen/', '/kataloge/', '/produkte/', '/impressum/',
                    '/produkte/metallstichsageblatter/ISD/', '/produkte/lochsagen/empfehlungen']:
            self.assertStatus(url)
        for slug in GROUP_SLUGS:
            self.assertStatus(reverse('products:list', args=[slug]))

    def test_unknown_pages_are_404(self):
        for url in ['/produkte/unbekannt/', '/produkte/metallstichsageblatter/XXX/',
                    '/produkte/metallsagebander/99999/', '/produkte/lochsagen/details/',
                    '/produkte/unbekannt/empfehlungen', '/news/versteckt/']:
            self.assertStatus(url, 404)

    def test_hidden_news_not_listed(self):
        response = self.assertStatus('/news/')
        self.assertContains(response, 'Neuigkeit')
        self.assertNotContains(response, 'Versteckt')

    def test_admin_pages(self):
        self.client.force_login(User.objects.create(username='admin', is_staff=True, is_superuser=True))
        self.assertStatus('/admin/')
        for name in ['news_entry', 'fairs_fair', 'products_sawblade', 'products_bandsawblade',
                     'products_holesaw', 'products_circularsawblade', 'flatpages_flatpage']:
            self.assertStatus(reverse(f'admin:{name}_changelist'))
            self.assertStatus(reverse(f'admin:{name}_add'))
