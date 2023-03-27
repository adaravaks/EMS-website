from django.shortcuts import render
from rest_framework import generics
from decouple import config
from .models import Doctor, Review, Service
from .serializers import DoctorsSerializer


def index(request):
    context = {
        'title': 'ЭМР - эффективные медицинские решения',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'ЭМР - о нас',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/about-us.html', context=context)


def services(request):
    our_services = Service.objects.all()
    context = {
        'title': 'ЭМР - услуги',
        'services': our_services,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/services.html', context=context)


def service(request, service_slug):
    service_requested = Service.objects.get(slug=service_slug)
    context = {
        'title': f'ЭМР - {service_requested.name}',
        'service': service_requested,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/service.html', context=context)


def doctors(request):
    our_doctors = Doctor.objects.all()
    context = {
        'title': 'ЭМР - наши врачи',
        'doctors': our_doctors,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/doctors.html', context=context)


def promotions(request):
    context = {
        'title': 'ЭМР - текущие акции',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/promotions.html', context=context)


def contacts(request):
    context = {
        'title': 'ЭМР - контакты',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/contacts.html', context=context)


def reviews(request):
    our_reviews = Review.objects.all()
    context = {
        'title': 'ЭМР - отзывы пациентов',
        'reviews': our_reviews,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/reviews.html', context=context)


def papers(request):
    context = {
        'title': 'ЭМР - документы',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/papers.html', context=context)


def doctor(request, name_slug):
    the_doctor = Doctor.objects.get(slug=name_slug)
    their_services_raw = the_doctor.services.through.objects.filter(doctor_id=the_doctor.pk)
    their_services = []

    for service in their_services_raw:
        their_services.append(Service.objects.get(pk=service.service_id))

    their_reviews = []
    for review in Review.objects.all():
        if the_doctor in review.doctors_mentioned.all():
            their_reviews.append(review)
    context = {
        'doctor': the_doctor,
        'services': their_services,
        'reviews': their_reviews,
        'title': f'ЭМР - {the_doctor.name}',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/doctor.html', context=context)


class DoctorsAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
