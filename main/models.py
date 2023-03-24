from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField('Название процедуры', max_length=300)
    price = models.IntegerField('Цена, руб.')
    slug = models.SlugField('Ссылка, которая будет вести к услуге. Это поле заполняется само, не нужно его трогать. Вписав сюда что-то, вы ничего не испортите, но и лучше от этого не станет.', blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = cyrillic_slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Doctor(models.Model):
    name = models.CharField('Фамилия, имя и отчество врача', max_length=150, unique=True)
    picture = models.FileField('Фото врача', upload_to='doctors_pictures/%Y/%m/%d')
    speciality = models.CharField('Специализация', max_length=300)
    experience = models.CharField('Стаж работы', max_length=100)
    education = models.TextField('Образование')
    additional_qualification = models.TextField('Повышение квалификации', blank=True)
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    slug = models.SlugField('Ссылка, которая будет вести к врачу. Это поле заполняется само, не нужно его трогать. Вписав сюда что-то, вы ничего не испортите, но и лучше от этого не станет.', blank=True, allow_unicode=True)

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

    def __str__(self):
        return f'Отзыв от пользователя {self.author}'

    @staticmethod
    def get_absolute_url():
        return reverse('reviews')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


def cyrillic_slugify(string):
    list_of_words_raw = string.strip().split(' ')
    list_of_words = []
    for index in range(len(list_of_words_raw)):
        if len(list_of_words_raw[index]) > 0:
            list_of_words.append(list_of_words_raw[index])
    func_slug = ''
    for word in list_of_words:
        func_slug += word + '-'
    return func_slug.strip('-').lower()
