
from django import template
from ..models.genre import genre
from ..models.movie import movie

register = template.Library()

@register.simple_tag
def categoryList():
    return genre.objects.all().order_by("name")[:10]
