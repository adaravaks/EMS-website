from django.shortcuts import render
from decouple import config


def index(request):
    context = {
        'title': 'Главная страница',
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
    context = {
        'title': 'Наши врачи',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY')
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
