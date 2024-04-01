from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Cargo(models.Model):
    codigo = models.CharField(max_length = 15, unique = True)
    nombre  = models.CharField(max_length = 50)
    perfil = models.CharField(max_length = 3000)

    class Meta:
        verbose_name = _("cargo")
        verbose_name_plural =  _("cargos")

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    ficha = models.CharField(max_length = 15, unique = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.CharField(max_length = 15, default = 'recursos_humanos')

    class Meta:
        verbose_name = _("empleado")
        verbose_name_plural = _("empleados")

    def __str__(self) -> str:
        return self.usuario.username
    
    @property
    def is_employee(self):
        return True
    
    @property
    def is_rh_employee(self) -> bool:
        return self.departamento == "recursos_humanos"