from django.template import Variable, resolve_variable
from django.template import VariableDoesNotExist

from django import template

register = template.Library()

# Constants
DOTFIELD = "<i class='fa fa-circle'></i>"


@register.filter()
def next(value, arg):
    """ Get next element inside a forloop """
    try:
        return value[int(arg)+1]
    except:
        return None


@register.filter(is_safe=True)
def check_zpz(val):
    if val:
        return DOTFIELD
    else:
        return ""


@register.simple_tag
def show_diameters(val):
    # The first value of val is always true. So always add one dotfield
    formatField = "<td>" + DOTFIELD + "</td>"
    length = len(val)

    if length == 3:
        return formatField + formatField + formatField

    if length > 1:
        if val[1].ordernr == "J":
            return formatField + formatField + "<td></td>"
        else:
            return formatField + "<td></td>" + formatField
    else:
        return formatField + "<td></td>" + "<td></td>"


@register.simple_tag
def getDotfield():
    return DOTFIELD