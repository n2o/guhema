from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Entry


def detail(request, slug):
    entries = Entry.objects.all() if request.user.is_staff else Entry.objects.current()
    entry = get_object_or_404(entries, slug=slug)
    return render(request, 'news/detail.html', {'entry': entry})


def overview(request):
    posts = get_list_or_404(Entry.objects.current().order_by('-created'))
    return render(request, 'news/overview.html', {'posts': posts})
