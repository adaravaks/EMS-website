from django import template
from main.models import *

register = template.Library()


@register.filter
def get_doctor_absolute_url_by_name(doctor_name):
    return Doctor.objects.get(name=doctor_name).get_absolute_url()
