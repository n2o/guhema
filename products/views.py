from django.shortcuts import render, get_list_or_404

from .models import SawBlade, ProductGroup, SableSawBlade, HackSawBlade, HoleSaw


def index(request):
    groups = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': groups})


def list(request, slug):
    blades = None
    layout = 'sawblade_overview.html'
    group = ProductGroup.objects.get(slug=slug)
    if slug == 'maschinensageblatter':
        layout = 'sawblade_overview.html'
        blades = SawBlade.objects.filter(group=group)
    elif slug == 'metallstichsageblatter':
        layout = 'compass_overview.html'
        blades = SawBlade.objects.filter(group=group)
    elif slug == 'sabel-und-spezialsabelsageblatter':
        layout = 'sablesawblade_overview.html'
        blades = SableSawBlade.objects.filter(group=group)
    elif slug == 'metallhandsageblatter':
        layout = 'hacksawblade_overview.html'
        blades = HackSawBlade.objects.filter(group=group)
    elif slug == 'lochsagen':
        layout = 'holesaw_overview.html'
        blades = HoleSaw.objects.filter()
    return render(request, 'products/'+layout, {'blades': blades,
                                                'group': group})


def details(request, slug, type):
    layout = 'sawblade_details.html'
    blade = SawBlade.objects.get(type=type)
    indicators = blade.indicators.order_by('width')
    if slug == 'maschinensageblatter':
        layout = 'sawblade_details.html'
    elif slug == 'metallstichsageblatter' or slug == 'metallhandsageblatter':
        layout = 'compass_details.html'
    return render(request, 'products/'+layout, {'blade': blade,
                                                'clamping': blade.clamping,
                                                'indicators': indicators})
