from django.shortcuts import render, redirect
from rest_framework import generics
from decouple import config
from .models import Doctor, Review, Service, CarouselPicture, Certificate, IndexPicture
from .serializers import DoctorsSerializer, ServicesSerializer, ReviewsSerializer, CarouselPicturesSerializer
from .forms import CallRequestForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    photos = IndexPicture.objects.all()
    context = {
        'title': 'ЭМР - эффективные медицинские решения',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'photos': photos,
        'error': error
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    context = {
        'title': 'ЭМР - о нас',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/about-us.html', context=context)


def services(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_services = Service.objects.all()
    context = {
        'title': 'ЭМР - услуги',
        'services': our_services,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/services.html', context=context)


def dental(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_services = Service.objects.filter(category='Стоматология')
    context = {
        'title': 'ЭМР - стоматология',
        'services': our_services,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/dental.html', context=context)


def usr(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_services = Service.objects.filter(category='УЗИ')
    context = {
        'title': 'ЭМР - УЗИ',
        'services': our_services,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/usr.html', context=context)


def analyzes(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_services = Service.objects.filter(category='Анализы')
    subcategories = set()
    subcategories_slugs = {}
    for service in our_services:
        subcategories.add(service.subcategory)
        subcategories_slugs[service.subcategory] = service.subcategory_slug

    context = {
        'title': 'ЭМР - анализы',
        'subcategories': sorted(subcategories),
        'slugs': subcategories_slugs,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/analyzes.html', context=context)


def subcategory(request, subcategory_slug):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    analyzes_required = Service.objects.filter(subcategory_slug=subcategory_slug)

    context = {
        'title': 'ЭМР - анализы',
        'header': analyzes_required[0].subcategory,
        'services': analyzes_required,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/subcategory.html', context=context)


def service(request, service_slug):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    service_requested = Service.objects.get(slug=service_slug)
    context = {
        'title': f'ЭМР - {service_requested.name}',
        'service': service_requested,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/service.html', context=context)


def doctors(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_doctors = Doctor.objects.all()
    context = {
        'title': 'ЭМР - наши врачи',
        'doctors': our_doctors,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/doctors.html', context=context)


def promotions(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    context = {
        'title': 'ЭМР - текущие акции',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/promotions.html', context=context)


def contacts(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    context = {
        'title': 'ЭМР - контакты',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/contacts.html', context=context)


def reviews(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    our_reviews = Review.objects.all().order_by('creation_time')
    context = {
        'title': 'ЭМР - отзывы пациентов',
        'reviews': our_reviews,
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/reviews.html', context=context)


def certificates(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    all_certificates = Certificate.objects.all()
    context = {
        'title': 'ЭМР - документы',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'certificates': all_certificates,
        'form': form,
        'error': error
    }
    return render(request, 'main/certificates.html', context=context)


def requisites(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    context = {
        'title': 'ЭМР - реквизиты',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/requisites.html', context=context)


def doctor(request, name_slug):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
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
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/doctor.html', context=context)


def api(request):
    error = ''
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверный ввод'

    form = CallRequestForm()
    context = {
        'title': 'ЭМР - API сайта',
        'yandex_map_apikey': config('YANDEX_MAP_APIKEY'),
        'form': form,
        'error': error
    }
    return render(request, 'main/api.html', context=context)


class DoctorsAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer


class ServicesAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer


class ReviewsAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class CarouselPicturesAPIView(generics.ListAPIView):
    queryset = CarouselPicture.objects.all()
    serializer_class = CarouselPicturesSerializer
