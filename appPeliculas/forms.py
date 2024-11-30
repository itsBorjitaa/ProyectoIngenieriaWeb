from django import forms
from .models import Suscriptor

class FormularioSuscripcion(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu correo electrónico'
            }),
        }
