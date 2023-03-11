from django.contrib import admin
from .models import Doctor, Service, Review


admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Review)
