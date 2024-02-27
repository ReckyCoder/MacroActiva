from django.db import models
from django.contrib.auth.models import User
from apps.rh.empleado.models import *

# Create your models here.


class Cargo(models.Model):
    nombre  = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario.__getattribute__("username")