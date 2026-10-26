from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from .models import (BandSawBlade, BandSawBladeIndicator, CircularSawBlade,
                     CircularSawBladeIndicator, HackSawBlade, HoleSaw,
                     HoleSawDiameter, JigSawBlade, ProductGroup, SableSawBlade,
                     SawBlade)


def _render_or_404(request, slug, page, context=None):
    """Templates are looked up by slug, so a missing one means an unknown page."""
    if not ProductGroup.objects.filter(slug=slug, public=True).exists():
        raise Http404
    template_name = f'products/{slug}/{page}.html'
    try:
        template = get_template(template_name)
    except TemplateDoesNotExist:
        raise Http404 from None
    return HttpResponse(template.render(context, request))


def index(request):
    groups = get_list_or_404(ProductGroup)
    return render(request, 'products/index.html', {'groups': groups})


def group_list(request, slug):
    blades = None
    other = None
    group = get_object_or_404(ProductGroup, slug=slug)
    if slug in ('maschinensageblatter', 'metallstichsageblatter'):
        blades = SawBlade.objects.filter(group=group).select_related('group', 'clamping')
    elif slug == 'sabel-und-spezialsabelsageblatter':
        blades = SableSawBlade.objects.filter(group=group).select_related('group').prefetch_related('indicators')
    elif slug == 'metallhandsageblatter':
        blades = HackSawBlade.objects.filter(group=group).select_related('group').prefetch_related('indicators')
    elif slug == 'lochsagen':
        blades = HoleSaw.objects.all()
        other = HoleSawDiameter.objects.filter(advice=False).prefetch_related('blades')
    elif slug == 'metallsagebander':
        blades = BandSawBlade.objects.select_related('group')
        other = BandSawBladeIndicator.objects.all()
    elif slug == 'pendelhubstichsageblatter':
        blades = JigSawBlade.objects.all()
    elif slug == 'metallkreissageblatter':
        blades = CircularSawBlade.objects.all()
        other = CircularSawBladeIndicator.objects.all().order_by('diameter')
    return _render_or_404(request, slug, 'overview',
                          {'blades': blades,
                           'group': group,
                           'other': other})


def details(request, slug, type):
    # type is not unique across product groups
    blade = SawBlade.objects.filter(type=type, group__slug=slug).first()
    if blade is None:
        raise Http404
    return _render_or_404(request, slug, 'details',
                          {'blade': blade,
                           'clamping': blade.clamping,
                           'indicators': blade.indicators.order_by('width')})


def details_by_id(request, slug, id):
    blade = get_object_or_404(BandSawBlade, id=id, group__slug=slug)
    return _render_or_404(request, slug, 'details',
                          {'blade': blade,
                           'indicators': blade.bandsaw_indicators.all()})


def product_advices(request, slug):
    objects = None
    if slug == 'lochsagen':
        objects = HoleSawDiameter.objects.filter(advice=True)
    return _render_or_404(request, slug, 'advices', {'objects': objects})
