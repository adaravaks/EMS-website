# Generated by Django 4.1.7 on 2023-06-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='index_pictures', verbose_name='Фото/скан сертификата')),
                ('description', models.CharField(max_length=1000, verbose_name='Короткое описание (что на фотке?)')),
            ],
            options={
                'verbose_name': 'Фото для главной страницы',
                'verbose_name_plural': 'Фото для главной страницы',
            },
        ),
        migrations.AlterField(
            model_name='certificate',
            name='picture',
            field=models.FileField(upload_to='certificates', verbose_name='Фото/скан сертификата'),
        ),
    ]
