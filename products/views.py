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
    group = ProductGroup.objects.get(slug=slug)
    if slug == 'maschinensageblatter':
        blades = SawBlade.objects.filter(group=group)
    elif slug == 'metallstichsageblatter':
        blades = SawBlade.objects.filter(group=group)
    elif slug == 'sabel-und-spezialsabelsageblatter':
        blades = SableSawBlade.objects.filter(group=group)
    elif slug == 'metallhandsageblatter':
        blades = HackSawBlade.objects.filter(group=group)
    elif slug == 'lochsagen':
        blades = HoleSaw.objects.all()
        other = HoleSawDiameter.objects.filter(advice=False)
    elif slug == 'metallsagebander':
        blades = BandSawBlade.objects.all()
        other = BandSawBladeIndicator.objects.all()
    elif slug == 'pendelhubstichsageblatter':
        blades = JigSawBlade.objects.all()
    elif slug == 'metallkreissageblatter':
        blades = CircularSawBlade.objects.all()
        other = CircularSawBladeIndicator.objects.all().order_by('diameter')
    return render(request, 'products/'+slug+'/overview.html',
                  {'blades': blades,
                   'group': group,
                   'other': other})


def details(request, slug, type):
    blade = SawBlade.objects.get(type=type)
    indicators = blade.indicators.order_by('width')
    return render(request, 'products/'+slug+'/details.html',
                  {'blade': blade,
                   'clamping': blade.clamping,
                   'indicators': indicators})


def details_by_id(request, slug, id):
    """
    Given a slug and a ID it returns a unique blade
    :param slug: slug of productgroup
    :param id: blade id
    :return: blade
    """
    blade = BandSawBlade.objects.get(id=id)
    indicators = blade.bandsaw_indicators.all()

    return render(request, 'products/'+slug+'/details.html',
                  {'blade': blade,
                   'indicators': indicators})


def product_details(request, slug):
    return render(request, 'products/'+slug+'/details.html')


def product_advices(request, slug):
    objects = None
    if slug == 'lochsagen':
        objects = HoleSawDiameter.objects.filter(advice=True)
    return render(request, 'products/'+slug+'/advices.html', {'objects': objects})


def holesawAdvice(request):
    layout = 'holesaw_advice.html'
    diameters = HoleSawDiameter.objects.filter(advice=True)
    group = ProductGroup.objects.get(slug='lochsagen')
    return render(request, 'products/'+layout, {'diameters': diameters,
                                                'group': group})


# ======================================================================================================================
#
# ======================================================================================================================
