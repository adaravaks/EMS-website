from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('о-нас', views.about, name='about'),
    path('новости', views.news, name='news'),
    path('новости/<str:title_slug>', views.news_post, name='news-post'),
    path('услуги', views.services, name='services'),
    path('услуги/стоматология', views.dental, name='dental'),
    path('услуги/узи', views.usr, name='usr'),
    path('услуги/онкология-маммология', views.onco_mammo, name='onco-mammo'),
    path('услуги/кардиология', views.cardiology, name='cardiology'),
    path('услуги/анализы', views.analyzes, name='analyzes'),
    path('услуги/анализы/<str:subcategory_slug>', views.subcategory, name='subcategory'),
    path('наши-врачи', views.doctors, name='doctors'),
    # path('акции', views.promotions, name='promotions'),
    # path('контакты', views.contacts, name='contacts'),
    path('отзывы', views.reviews, name='reviews'),
    path('сертификаты', views.certificates, name='certificates'),
    path('реквизиты', views.requisites, name='requisites'),
    # path('наши-врачи/<str:name_slug>', views.doctor, name='doctor'),
    # path('услуги/<str:service_slug>', views.service, name='service'),
    # path('api', views.api, name='api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
