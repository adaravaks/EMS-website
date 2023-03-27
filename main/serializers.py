from rest_framework import serializers
from .models import Doctor


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'picture', 'speciality', 'experience', 'education', 'additional_qualification')
