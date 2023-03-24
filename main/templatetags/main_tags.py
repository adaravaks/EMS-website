from django import template
from main.models import *

register = template.Library()


@register.filter
def get_doctor_absolute_url_by_name(doctor_name):
    return Doctor.objects.get(name=doctor_name).get_absolute_url()


@register.inclusion_tag('main/carousel-ul.html')
def get_carousel_list():
    images = CarouselPicture.objects.all()
    slides_dict = {}
    inactive_list_items = []
    for index in range(len(images)):
        if index == 0:
            slides_dict['active_slide'] = images[index]
        else:
            inactive_list_items.append(images[index])
    slides_dict['inactive_slides'] = inactive_list_items
    return {'slides_dict': slides_dict}
