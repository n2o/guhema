from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Entry, Category


@login_required
def detail(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'news/detail.html', {'entry': entry})


@login_required
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
    return render(request, 'blog/list.html',
                  {'posts':     posts,
                   'paginator': posts,
                   'length':    range(len(posts)),
                   'category':  category[0]})