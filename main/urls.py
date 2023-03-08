from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('о-нас', views.about, name='about'),
    path('услуги', views.services, name='services'),
    path('наши-врачи', views.doctors, name='doctors'),
    path('акции', views.promotions, name='promorions'),
    path('контакты', views.contacts, name='contacts'),
    path('отзывы', views.reviews, name='reviews'),
    path('жопа', views.ass, name='ass'),
]
