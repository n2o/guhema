from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

# Constants
DOTFIELD = mark_safe("<i class='fa fa-circle'></i>")
DOTCELL = format_html("<td>{}</td>", DOTFIELD)
EMPTYCELL = mark_safe("<td></td>")


@register.filter(name='next')
def next_item(value, arg):
    """ Get next element inside a forloop """
    try:
        return value[int(arg)+1]
    except (IndexError, TypeError, ValueError):
        return None


@register.filter
def check_zpz(val):
    return DOTFIELD if val else ""


@register.filter
def bandsawIndicatorCheck(val):
    if val == "1":
        return format_html("<span class='indicator-dot'>{}</span>", DOTFIELD)
    return format_html("<strong>{}</strong>", val)


@register.simple_tag
def show_diameters(val):
    # The first value of val is always true. So always add one dotfield
    length = len(val)

    if length == 3:
        return DOTCELL + DOTCELL + DOTCELL

    if length > 1:
        if val[1].ordernr == "J":
            return DOTCELL + DOTCELL + EMPTYCELL
        return DOTCELL + EMPTYCELL + DOTCELL
    return DOTCELL + EMPTYCELL + EMPTYCELL


@register.simple_tag
def getDotfield():
    return DOTFIELD


@register.simple_tag
def validBandsawIndicator(ind):
    if ind.L:
        return "L"
    elif ind.W:
        return "W"
    elif ind.T:
        return "T"
    elif ind.Z:
        return "Z"
    elif ind.VP:
        return "VP"
    elif ind.TP:
        return "TP"
    elif ind.F:
        return "F"
    elif ind.E:
        return "E"
    else:
        return "L"
