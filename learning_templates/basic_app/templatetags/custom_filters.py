from django import template

regiser = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Cuts out all values of "arg" from the "value" string
    """
    return value.replace(arg, '')

# @register.filter(name='cut')        [ @decorator ]
#     is the same as:
# register.filter('cut', cut)
#     is the same as:
# @register.filter                    [ @decorator ]
#
# NOTE - If you leave off the name argument Django will use the
# functions name as the filter name
#
# THE MENTIONED register.filter() SIMPLY REGISTERS THE
# ASSICIATED CUSTOM FILTER WITH DJANGO FOR USE IN TEMPLATES ALONG
# WITH THE {% load custom_filters %} CALL, WHERE "custom_filters"
# REFERS TO THE NAME OF THE "custom_filter.py" FILE (CAN BE CALLED)
# ANYTHING!!
