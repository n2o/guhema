from django.shortcuts import get_object_or_404, render
from django.http import Http404

from news.models import Entry


def index(request):
    try:
        posts = Entry.objects.all()[:3]
    except Entry.DoesNotExist:
        raise Http404("Keine Beiträge vorhanden.")
    return render(request, 'index.html', {'posts': posts})


def products(request):
    return render(request, '../products/templates/products/index.html')