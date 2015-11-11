from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Entry, Category


def detail(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'news/detail.html', {'entry': entry})


def overview(request, page=1, category="Allgemein"):
    try:
        category = Category.objects.filter(name=category)
        all_posts = Entry.objects.filter(
            Q(category=category[0].id),
            Q(public=True),
            Q(archive=False),
        ).order_by("-created")

        paginator = Paginator(all_posts, 6)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)
    except Entry.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'news/overview.html',
                  {'posts':     pack(posts),
                   'paginator': posts,
                   'length':    range(len(posts)),
                   'category':  category[0]})


def plugin(request):
    try:
        posts = Entry.objects.all()[:3]
        print(posts)
    except Entry.DoesNotExist:
        raise Http404("Keine Beiträge vorhanden.")
    return render(request, 'news/plugin.html', {'posts': posts})


################################ Aux functions

def pack(_list):
    nlist = list(_list)
    if len(nlist) % 2:      # Append none if len is odd
        nlist.append(None)
    return zip(nlist[::2], nlist[1::2])