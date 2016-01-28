from django.shortcuts import get_list_or_404, render

from .models import (BandSawBlade, BandSawBladeIndicator, CircularSawBlade,
                     CircularSawBladeIndicator, HackSawBlade, HoleSaw,
                     HoleSawDiameter, JigSawBlade, ProductGroup, SableSawBlade,
                     SawBlade)


def index(request):
    groups = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': groups})


def list(request, slug):
    other = None
    group = ProductGroup.objects.get(slug=slug)
    blades = SawBlade.objects.filter(group=group)
    if slug == 'lochsagen':
        blades = HoleSaw.objects.all()
        other = HoleSawDiameter.objects.filter(advice=False)
    elif slug == 'metallsagebander':
        blades = BandSawBlade.objects.all()
        other = BandSawBladeIndicator.objects.all()
    elif slug == 'metallkreissageblatter':
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
    layout = ''
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


def productAdvices(request, slug):
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
    return render(request, 'products/maschinensageblatter/sawblade_advices.html')


def holesawAdvice(request):
    layout = 'holesaw_advice.html'
    diameters = HoleSawDiameter.objects.filter(advice=True)
    group = ProductGroup.objects.get(slug='lochsagen')
    return render(request, 'products/'+layout, {'diameters': diameters,
                                                'group': group})
