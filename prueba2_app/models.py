from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator

class Socio(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    ESTADO_CHOICES = [
        ('V', 'Vigente'),
        ('S', 'Suspendido'),
        ('R', 'Retirado'),
    ]

    nombre = models.CharField(max_length=80, validators=[MaxLengthValidator(80)])
    fecha_incorporacion = models.DateField()
    año_nacimiento = models.IntegerField()
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(validators=[EmailValidator(message='Ingresa una dirección de correo electrónico válida.')])
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
