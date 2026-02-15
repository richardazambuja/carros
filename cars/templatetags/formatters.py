from django import template

register = template.Library()

@register.filter
def br_currency(value):
    if value is None:
        return ""
    
    value = f"{value:,.2f}"
    value = value.replace(",", "X").replace(".", ",").replace("X", ".")
    return value