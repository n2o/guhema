from django.shortcuts import render
from django.utils import timezone

from .models import Fair


def index(request):
    today = timezone.localdate()
    upcoming = Fair.objects.filter(archive=False, public=True, end__gte=today).order_by('start')
    past = Fair.objects.filter(public=True, end__lt=today).order_by('-start')
    return render(request, 'fairs/index.html', {'upcoming': upcoming,
                                                'past': past})
