from django.shortcuts import get_list_or_404, render

from .models import (BandSawBlade, BandSawBladeIndicator, CircularSawBlade,
                     CircularSawBladeIndicator, HackSawBlade, HoleSaw,
                     HoleSawDiameter, JigSawBlade, ProductGroup, SableSawBlade,
                     SawBlade)


def index(request):
    groups = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': groups})


def list(request, slug):
    blades = None
    other = None
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
        blades = HoleSaw.objects.all()
        other = HoleSawDiameter.objects.filter(advice=False)
    elif slug == 'metallsagebander':
        layout = 'bandsawblade_overview.html'
        blades = BandSawBlade.objects.all()
        other = BandSawBladeIndicator.objects.all()
    elif slug == 'pendelhubstichsageblatter':
        layout = 'jigsawblade_overview.html'
        blades = JigSawBlade.objects.all()
    elif slug == 'metallkreissageblatter':
        layout = 'circularsawblade_overview.html'
        blades = CircularSawBlade.objects.all()
        other = CircularSawBladeIndicator.objects.all().order_by('diameter')
    return render(request, 'products/'+layout, {'blades': blades,
                                                'group': group,
                                                'other': other})


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



def detailsById(request, slug, id):
    """
    Given a slug and a ID it returns a unique blade
    :param slug: slug of productgroup
    :param id: blade id
    :return: blade
    """
    layout = 'bandsawblade_details.html'
    blade = BandSawBlade.objects.get(id=id)
    indicators = blade.bandsaw_indicators.all()

    return render(request, 'products/'+layout, {'blade': blade,
                                                'indicators': indicators})


def productDetails(request, slug):
    if slug == 'maschinensageblatter':
        layout = 'sawblade_general.html'
    elif slug == 'metallstichsageblatter':
        layout = ''
    elif slug == 'sabel-und-spezialsabelsageblatter':
        layout = ''
    elif slug == 'metallhandsageblatter':
        layout = ''
    elif slug == 'lochsagen':
        layout = ''
        other = HoleSawDiameter.objects.filter(advice=False)
    elif slug == 'metallsagebander':
        layout = ''
        other = BandSawBladeIndicator.objects.all()
    elif slug == 'pendelhubstichsageblatter':
        layout = ''
    elif slug == 'metallkreissageblatter':
        layout = ''
    return render(request, 'products/details/'+layout)


def holesawAdvice(request):
    layout = 'holesaw_advice.html'
    diameters = HoleSawDiameter.objects.filter(advice=True)
    group = ProductGroup.objects.get(slug='lochsagen')
    return render(request, 'products/'+layout, {'diameters': diameters,
                                                'group': group})
