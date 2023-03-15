from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('о-нас', views.about, name='about'),
    path('услуги', views.services, name='services'),
    path('наши-врачи', views.doctors, name='doctors'),
    path('акции', views.promotions, name='promotions'),
    path('контакты', views.contacts, name='contacts'),
    path('отзывы', views.reviews, name='reviews'),
    path('документы', views.papers, name='papers'),
    path('наши-врачи/<str:name_slug>', views.doctor, name='doctor'),
    path('услуги/<str:service_slug>', views.service, name='service')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
