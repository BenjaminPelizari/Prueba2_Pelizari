from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
            'fecha_incorporacion': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
            },
            'fecha_incorporacion': {
                'required': 'Este campo es obligatorio.',
            },
            'año_nacimiento': {
                'required': 'Este campo es obligatorio.',
            },
            'telefono': {
                'required': 'Este campo es obligatorio.',
            },
            'correo_electronico': {
                'required': 'Este campo es obligatorio.',
            },
            'sexo': {
                'required': 'Este campo es obligatorio.',
            },
            'estado': {
                'required': 'Este campo es obligatorio.',
            },
        }
