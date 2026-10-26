from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

register = template.Library()

# Constants
DOT_ICON = mark_safe("<i class='fa fa-circle' aria-hidden='true'></i>")
EMPTYCELL = mark_safe("<td></td>")

# Tooth-count columns in the order they are preferred for the example article number
ZPZ_FIELDS = "L C E G H I J M N O T U V W UE".split()
BANDSAW_FIELDS = "L W T Z VP TP F E".split()


def dotfield():
    """Visible dot for sighted users, a word for screen readers (translated per request)."""
    return format_html("{}<span class='sr-only'>{}</span>", DOT_ICON, _("lieferbar"))


def dotcell():
    return format_html("<td>{}</td>", dotfield())


@register.filter(name='next')
def next_item(value, arg):
    """ Get next element inside a forloop """
    try:
        return value[int(arg)+1]
    except (IndexError, TypeError, ValueError):
        return None


@register.filter
def check_zpz(val):
    return dotfield() if val else ""


@register.filter
def bandsawIndicatorCheck(val):
    if val == "1":
        return format_html("<span class='indicator-dot'>{}</span>", dotfield())
    return format_html("<strong>{}</strong>", val)


@register.simple_tag
def show_diameters(val):
    # The first value of val is always true. So always add one dotfield
    length = len(val)

    if length == 3:
        return dotcell() + dotcell() + dotcell()

    if length > 1:
        if val[1].ordernr == "J":
            return dotcell() + dotcell() + EMPTYCELL
        return dotcell() + EMPTYCELL + dotcell()
    return dotcell() + EMPTYCELL + EMPTYCELL


@register.simple_tag
def getDotfield():
    """Legend dot: purely visual, the legend text says what it means."""
    return DOT_ICON


def _article_code(ind, fields):
    """Code of the first tooth count this indicator really offers, L as fallback."""
    if not ind:  # no indicator (templates pass "" for a missing one)
        return ""
    field = next((f for f in fields if getattr(ind, f, False)), "L")
    return {"UE": "Ü"}.get(field, field)


@register.simple_tag
def zpzCode(ind, without=""):
    """without: tooth-count columns the page's table does not show"""
    return _article_code(ind, [f for f in ZPZ_FIELDS if f not in without.split()])


@register.simple_tag
def validBandsawIndicator(ind):
    return _article_code(ind, BANDSAW_FIELDS)
