# from django.db import models

# Create your models here.

# Departamentos solo se traen del módulo Administración

# class CentroDeCostos(models.Model):
#     """Model definition for CentroDeCostos."""

#     # Define fields here

    # departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    # nombre = models.CharField(max_length=50)
    # codigo = models.CharField(max_length=50)
    # fecha_creado = models.DateField(auto_now=False, auto_now_add=False)

#     class Meta:
#         """Meta definition for CentroDeCostos."""

#         verbose_name = 'CentroDeCostos'
#         verbose_name_plural = 'CentroDeCostos'

#     def __str__(self):
#         """Unicode representation of CentroDeCostos."""
#         pass


# class Presupuesto(models.Model):
#     """Model definition for Presupuesto."""

#     # Define fields here

    # centro_de_costos = models.ForeignKey('CentrodeCostos', related_name='presupuesto', on_delete=models.CASCADE)
    # nombre = models.CharField(max_length=50)
    # codigo = models.CharField(max_length=50)
    # fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    # fecha_limite = models.DateField(auto_now=False, auto_now_add=False)
    # total = models.IntegerField()

#     class Meta:
#         """Meta definition for Presupuesto."""

#         verbose_name = 'Presupuesto'
#         verbose_name_plural = 'Presupuestos'

#     def __str__(self):
#         """Unicode representation of Presupuesto."""
#         pass


# class PresupuestoLista(models.Model):
#     """Model definition for PresupuestoLista."""

#     # Define fields here
        # lista = models.ForeignKey('Presupuesto', related_name='lista', on_delete=models.CASCADE)
        # descripcion = models.CharField(max_length=50)
        # codigo = models.CharField(max_length=50)
        # neto = models.CharField(max_length=50)

        # ----------- A Revisión y Consultas ---------------
        # impuesto = models.ForeignKey('Impuesto', related_name='impuesto', on_delete=models.CASCADE)
        # O solamente IVA
        # ---------------------------------------------------

        # total = models.IntegerField()


#     class Meta:
#         """Meta definition for PresupuestoLista."""

#         verbose_name = 'PresupuestoLista'
#         verbose_name_plural = 'PresupuestoListas'

#     def __str__(self):
#         """Unicode representation of PresupuestoLista."""
#         pass
