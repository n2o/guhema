from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import SawBlade, Clamping


def index(request, page=1, category="Allgemein"):
    return render(request, 'products/index.html')


# Maschinensägeblätter
def sawblades(request):
    blades = get_list_or_404(SawBlade.objects.order_by('type'))
    return render(request, 'products/sawblade_overview.html', {'blades': blades})


def sawblade(request, clamping, slug):
    clamping = get_object_or_404(Clamping, slug=clamping)
    blade = get_object_or_404(SawBlade, slug=slug, clamping=clamping)
    indicators = blade.indicators.order_by('width')
    return render(request, 'products/sawblade_detail.html', {'blade': blade,
                                                             'clamping': clamping,
                                                             'indicators': indicators})


# Metallstichsägeblätter
def compasses(request):
    blades = get_list_or_404(SawBlade.objects.order_by('type'))
    return render(request, 'products/compass_overview.html', {'blades': blades})


def compass(request, clamping, slug):
    clamping = get_object_or_404(Clamping, slug=clamping)
    blade = get_object_or_404(SawBlade, slug=slug, clamping=clamping)
    indicators = blade.indicators.order_by('width')
    return render(request, 'products/compass_detail.html', {'blade': blade,
                                                             'clamping': clamping,
                                                             'indicators': indicators})