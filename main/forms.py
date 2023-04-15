from django.forms import ModelForm, TextInput, Textarea
from .models import CallRequest


class CallRequestForm(ModelForm):
    class Meta:
        model = CallRequest
        fields = ('phone_number', 'wishes')
        widgets = {
            'phone_number': TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Номер телефона'}),

            'wishes': Textarea(attrs={
                'class': 'form-field',
                'placeholder': 'Пожелания (например, как к вам стоит обращаться и когда лучше позвонить)'})
        }
