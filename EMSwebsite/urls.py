"""EMSwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import DoctorsAPIView, ServicesAPIView, ReviewsAPIView, CarouselPicturesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/doctorslist', DoctorsAPIView.as_view(), name='doctors-api'),
    path('api/v1/serviceslist', ServicesAPIView.as_view(), name='services-api'),
    path('api/v1/reviewslist', ReviewsAPIView.as_view(), name='reviews-api'),
    path('api/v1/carouselpictureslist', CarouselPicturesAPIView.as_view(), name='carousel-images-api')
]
