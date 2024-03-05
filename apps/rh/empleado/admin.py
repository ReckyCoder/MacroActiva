from django.contrib import admin
from .models import Cargo, Empleado
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ["usuario", "cargo"]

admin.site.register(Cargo)
admin.site.register(Empleado, EmpleadoAdmin)