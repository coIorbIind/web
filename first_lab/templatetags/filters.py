from django import template

register = template.Library()


@register.filter(name='split')
def split_filter(value, arg):
    if arg == "\\n":
        return value.splitlines()
    return value.split(arg)


@register.filter
def index(iterable, i):
    return iterable[i]
