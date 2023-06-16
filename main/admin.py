from django.contrib import admin
from .models import Doctor, Service, Review, CarouselPicture, CallRequest, Certificate, IndexPicture

admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(CarouselPicture)
admin.site.register(CallRequest)
admin.site.register(Certificate)
admin.site.register(IndexPicture)