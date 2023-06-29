from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField('Название процедуры', max_length=3000, null=True)
    category = models.CharField('Категория', max_length=1000)
    subcategory = models.CharField('Подкатегория (только для анализов)', null=True, blank=True, max_length=2000)
    subcategory_slug = models.CharField('Слаг подкатегории (только для анализов, оставьте пустым — поле заполняется само)', null=True, blank=True, max_length=2000)
    biomaterial = models.CharField('Биоматериал (только для анализов)', null=True, blank=True, max_length=2000)
    time = models.CharField('Срок выполнения в рабочих днях без учёта дня забора (только для анализов)', null=True, blank=True, max_length=2000)
    price = models.CharField('Цена, руб.', null=True, max_length=2000)

    def save(self, *args, **kwargs):
        self.subcategory_slug = cyrillic_slugify(self.subcategory) if self.subcategory else ''
        super(Service, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.subcategory_slug = cyrillic_slugify(self.subcategory) if self.subcategory else ''
        super(Service, self).save(*args, **kwargs)

    @staticmethod
    def get_absolute_url():
        return reverse('services')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Doctor(models.Model):
    name = models.CharField('Фамилия, имя и отчество врача', max_length=150, unique=True)
    picture = models.FileField('Фото врача', upload_to='doctors_pictures/%Y/%m/%d')
    speciality = models.CharField('Специализация', max_length=300)
    experience = models.CharField('(пока не используется на сайте) Стаж работы', max_length=100, blank=True)
    education = models.TextField('(пока не используется на сайте) Образование', blank=True)
    slug = models.SlugField('(пока не используется на сайте) Ссылка, которая будет вести к врачу. Это поле заполняется само, не нужно его трогать. Вписав сюда что-то, вы ничего не испортите, но и лучше от этого не станет.', blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = cyrillic_slugify(self.name)
        super(Doctor, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug = cyrillic_slugify(self.name)
        super(Doctor, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'name_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Review(models.Model):
    doctors_mentioned = models.ManyToManyField(Doctor, verbose_name='Доктора, о которых идёт речь')
    source = models.CharField('Ссылка на источник', max_length=300)
    author = models.CharField('Автор', max_length=150)
    text = models.TextField('Отзыв')
    creation_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Отзыв от пользователя {self.author}'

    @staticmethod
    def get_absolute_url():
        return reverse('reviews')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class CarouselPicture(models.Model):
    picture = models.FileField(upload_to='carousel_pictures', verbose_name='Изображение')
    description = models.CharField('Короткое описание', max_length=150)

    def __str__(self):
        return f'Изображение для слайд-шоу: {self.description}'

    class Meta:
        verbose_name = 'Изображение для слайд-шоу'
        verbose_name_plural = 'Изображения для слайд-шоу'


class CallRequest(models.Model):
    phone_number = models.CharField('Номер телефона', max_length=20)
    wishes = models.CharField('Пожелания', max_length=2000)

    def __str__(self):
        return f'Запрос звонка на {self.phone_number}'

    class Meta:
        verbose_name = 'Запрос звонка'
        verbose_name_plural = 'Запросы звонков'


class Certificate(models.Model):
    picture = models.FileField(upload_to='certificates', verbose_name='Фото/скан сертификата')
    description = models.CharField('Короткое описание (о чём сертификат?)', max_length=1000)

    def __str__(self):
        return f'Сертификат: {self.description}'

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class IndexPicture(models.Model):
    picture = models.FileField(upload_to='index_pictures', verbose_name='Фото/скан сертификата')
    description = models.CharField('Короткое описание (что на фотке?)', max_length=1000)

    def __str__(self):
        return f'Фото: {self.description}'

    class Meta:
        verbose_name = 'Фото для главной страницы'
        verbose_name_plural = 'Фото для главной страницы'


def cyrillic_slugify(string):
    list_of_words_raw = string.strip(', -/').split(' ')
    list_of_words = []
    for index in range(len(list_of_words_raw)):
        if len(list_of_words_raw[index]) > 0:
            list_of_words.append(list_of_words_raw[index])
    func_slug = ''
    for word in list_of_words:
        func_slug += word.strip(", -/()'") + '-'
    return func_slug.strip('-()').lower()
