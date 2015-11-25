from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import SawBlade


def index(request, page=1, category="Allgemein"):
    return render(request, 'products/index.html')


def sawblade(request):
    blades_query = get_list_or_404(SawBlade)
    blades = list()

    for blade in blades_query:
        indicators = list()
        indicator_list = list(blade.indicators.all().order_by('width'))
        for indicator in indicator_list:
            indicators.append(str(indicator).replace(' ', '').split(','))
        blade.indicator_array = indicators
        blades.append(blade)

    return render(request, 'products/sawblade_detail.html', {'blades': blades})