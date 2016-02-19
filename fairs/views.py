from datetime import datetime

from django.shortcuts import render

from .models import Fair


def index(request):
    upcoming = Fair.objects.filter(archive=False,
                                   public=True,
                                   end__gte=datetime.now())
    past = Fair.objects.filter(public=True,
                               end__lte=datetime.now())
    return render(request, 'fairs/index.html', {'upcoming': upcoming,
                                                'past': past})
