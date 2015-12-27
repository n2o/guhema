from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import SawBlade, ProductGroup


def index(request):
    productgroup = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': productgroup})


def list(request, slug):
    blades = productgroup = None
    layout = "sawblade_overview.html"
    if slug == "maschinensageblatter":
        productgroup = ProductGroup.objects.get(slug=slug)
        blades = SawBlade.objects.all()
        layout = 'sawblade_overview.html'
    elif slug == "metallstichsageblatter":
        pass
    return render(request, 'products/'+layout, {'blades': blades,
                                                'group': productgroup})


def details(request, slug, type):
    blade = SawBlade.objects.get(type=type)
    indicators = blade.indicators.order_by('width')
    return render(request, 'products/sawblade_detail.html', {'blade': blade,
                                                             'clamping': blade.clamping,
                                                             'indicators': indicators})
