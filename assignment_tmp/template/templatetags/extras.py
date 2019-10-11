from django import template

register = template.Library()


@register.filter(name='inc')
def get_sum_of_args(a, b):
    try:
        a = int(a)
        b = int(b)
        return a + b
    except:
        return ''


@register.simple_tag(name='division')
def devide(a, b, to_int=False):
    try:
        a = int(a)
        b = int(b)
        if to_int:
            return int(a / b)
        else:
            return a / b
    except:
        return ''
