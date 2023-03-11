from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path(u'о-нас', views.about, name='about'),
    path(u'услуги', views.services, name='services'),
    path(u'наши-врачи', views.doctors, name='doctors'),
    path(u'акции', views.promotions, name='promotions'),
    path(u'контакты', views.contacts, name='contacts'),
    path(u'отзывы', views.reviews, name='reviews'),
    path(u'жопа', views.ass, name='ass'),
    path(u'наши-врачи/<str:name_slug>', views.doctor, name='doctor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
