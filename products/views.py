from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import SawBlade, ProductGroup


def index(request):
    groups = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': groups})


def list(request, slug):
    layout = 'sawblade_overview.html'
    group = ProductGroup.objects.get(slug=slug)
    blades = SawBlade.objects.filter(group=group)
    if slug == 'maschinensageblatter':
        layout = 'sawblade_overview.html'
    elif slug == 'metallstichsageblatter':
        layout = 'compass_overview.html'
    return render(request, 'products/'+layout, {'blades': blades,
                                                'group': group})


def details(request, slug, type):
    layout = 'sawblade_details.html'
    blade = SawBlade.objects.get(type=type)
    indicators = blade.indicators.order_by('width')
    #if slug == 'maschinensageblatter':
    #    layout = 'sawblade_details.html'
    #elif slug == 'metallstichsageblatter':
    #    layout = 'compass_details.html'
    return render(request, 'products/'+layout, {'blade': blade,
                                                'clamping': blade.clamping,
                                                'indicators': indicators})
