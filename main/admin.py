from django.contrib import admin
from .models import Doctor, Service, Review, CarouselPicture


admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(CarouselPicture)