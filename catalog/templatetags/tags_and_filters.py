from django import template

register = template.Library()


@register.filter()
def media(path_image_product):
    if path_image_product is not None:
        return f"/media/{path_image_product}"
    return '#'
