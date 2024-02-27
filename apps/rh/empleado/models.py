from django.db import models
from django.contrib.auth.models import User
from apps.rh.empleado.models import *

# Create your models here.


class Cargo(models.Model):
    nombre  = models.CharField(max_length=50)
    perfil = models.CharField(max_length=3000)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.__getattribute__("username")