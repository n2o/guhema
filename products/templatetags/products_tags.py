from django.template import Variable, resolve_variable
from django.template import VariableDoesNotExist

from django import template

register = template.Library()


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
        return "<i class='fa fa-circle'></i>"
    else:
        return ""


@register.simple_tag()
def resolve(diameters, diameter, *args, **kwargs):
    print(diameter)
    if diameter in diameters:
        print("True")
    return None

    # if extension == 'pdf':
    #     return "<i class='fa fa-file-pdf-o fa-lg'></i>"
    # elif extension == 'jpg' or extension == 'png':
    #     return "<i class='fa fa-picture-o fa-lg'></i>"
    # elif extension == 'doc' or extension == 'docx':
    #     return "<i class='fa fa-file-word-o fa-lg'></i>"
    # elif extension == 'xls' or extension == 'xlsx':
    #     return "<i class='fa fa-file-excel-o fa-lg'></i>"
    # else:
    #     return extension
#
#
#
# @register.filter(is_safe=True)
# def houseDetailsLink(value, text):
#     if value:
#         return """<span style='margin-right: 1em;'>
#                   <a href='{1}'>
#                     {0}
#                   </a>
#               </span>
#         """.format(text, value)
#     else:
#         return ""