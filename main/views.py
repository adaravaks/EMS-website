from django.shortcuts import render
from decouple import config
from .models import Doctor, Review, Service


def index(request):
    context = {
        'title': 'ЭМР - эффективные медицинские решения',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О нас',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/about-us.html', context=context)


def services(request):
    context = {
        'title': 'Услуги',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/services.html', context=context)


def doctors(request):
    our_doctors = Doctor.objects.all()
    context = {
        'title': 'Наши врачи',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'doctors': our_doctors
    }
    return render(request, 'main/doctors.html', context=context)


def promotions(request):
    context = {
        'title': 'Текущие акции',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/promotions.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/contacts.html', context=context)


def reviews(request):
    context = {
        'title': 'Отзывы пациентов',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/reviews.html', context=context)


def ass(request):
    context = {
        'title': 'ЖОПА',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
    }
    return render(request, 'main/ass.html', context=context)


def doctor(request, name_slug):
    the_doctor = Doctor.objects.get(slug=name_slug)
    their_services_raw = Doctor.services.through.objects.all()
    their_services = []

    for service in their_services_raw:
        their_services.append(Service.objects.get(pk=service.service_id))

    their_reviews = Review.objects.filter(doctor_mentioned=the_doctor.name)
    context = {
        'doctor': the_doctor,
        'services': their_services,
        'reviews': their_reviews,
        'title': f'ЭМР - {the_doctor.name}'
    }
    return render(request, 'main/doctor.html', context=context)
