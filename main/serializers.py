from rest_framework import serializers
from .models import Doctor, Service, Review, CarouselPicture


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'picture', 'speciality', 'experience', 'education', 'additional_qualification')


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'price')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('author', 'text', 'creation_time', 'source')


class CarouselPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselPicture
        fields = ('description', 'picture')
