from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField(null=True)
    fecha_creacion=models.DateTimeField(null=True)
    