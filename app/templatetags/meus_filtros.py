from django import template

register=template.Library()


@register.filter(name='addclass')

def addClass(value,arg):
    return value.as_widget(attrs={'class':arg})