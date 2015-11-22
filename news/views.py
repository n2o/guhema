from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Entry


def detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'news/detail.html', {'entry': entry})


def overview(request, page=1, category="Allgemein"):
    posts = get_list_or_404(Entry.objects.order_by('-created'))
    return render(request, 'news/overview.html',
                  {'posts':     posts,
                   'category':  category[0]})