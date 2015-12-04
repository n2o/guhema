from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import SawBlade, Clamping


def index(request, page=1, category="Allgemein"):
    return render(request, 'products/index.html')


def sawblades(request):
    pass


def sawblade(request, clamping, slug):
    blade = get_object_or_404(SawBlade, slug=slug)
    clamping = get_object_or_404(Clamping, slug=clamping)
    indicators = blade.indicators.order_by('width')
    return render(request, 'products/sawblade_detail.html', {'blade': blade,
                                                             'clamping': clamping,
                                                             'indicators': indicators})