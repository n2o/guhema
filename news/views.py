from django.shortcuts import get_object_or_404, render

from .models import Entry


def detail(request, slug):
    entries = Entry.objects.all() if request.user.is_staff else Entry.objects.filter(public=True)
    entry = get_object_or_404(entries, slug=slug)
    return render(request, 'news/detail.html', {'entry': entry})


def overview(request):
    posts = Entry.objects.filter(public=True).order_by('-created')
    return render(request, 'news/overview.html', {'posts': posts})
