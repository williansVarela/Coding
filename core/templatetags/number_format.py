from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter(name='currency')
def currency(value):
    number = round(float(value), 2)
    return f'R${(intcomma(int(number)))}'
