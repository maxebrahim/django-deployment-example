from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    :param value:
    :param arg:
    :return: this cuts out all values
    """
    return value.replace(arg, "")


# register.filter('cut', cut)
