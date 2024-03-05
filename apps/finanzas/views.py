from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView

# Create your views here.


#ListView
class Departamentos(TemplateView):
    # model = MODEL_NAME
    template_name = "finanzas/departamentos/departamentos.html"

    # def get_queryset(self):
    #     queryset = super(model, self).get_queryset()
    #     queryset = queryset.
    #     return queryset


#------------------------ Vista de Centro de Costos con CRUD ------------------------------

#ListView
class CentroDeCostos(TemplateView):
    template_name = "finanzas/centro-de-costos/centroDeCostos.html"


#CreateView
class CrearCentroDeCostos(TemplateView):
    template_name = "finanzas/centro-de-costos/crearCentroDeCostos.html"

#UpdateView
class EditarCentroDeCostos(TemplateView):
    template_name = "finanzas/centro-de-costos/editarCentroDeCostos.html"



#------------------------------------------------------------------------------------------
    

#------------------------------- Vista de Proyectos con CRUD ------------------------------

#ListView
class Proyectos(TemplateView):
    template_name = "finanzas/proyectos/proyectos.html"


#CreateView
class CrearProyectos(TemplateView):
    template_name = "finanzas/proyectos/crearProyectos.html"

#UpdateView
class EditarProyectos(TemplateView):
    template_name = "finanzas/proyectos/editarProyectos.html"



#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Presupuestos de Centro de Costos con CRUD ------------------------------
    
#ListView
class PresupuestosCDC(TemplateView):
    template_name = "finanzas/presupuestos/centro-de-costos/presupuestos.html"


#CreateView
class CrearPresupuestosCDC(TemplateView):
    template_name = "finanzas/presupuestos/centro-de-costos/crearPresupuestos.html"

#UpdateView
class EditarPresupuestosCDC(TemplateView):
    template_name = "finanzas/presupuestos/centro-de-costos/editarPresupuestos.html"

#------------------------------------------------------------------------------------------

#---------------------------- Vista de Presupuestos de Proyectos con CRUD ------------------------------
    
#ListView
class PresupuestosP(TemplateView):
    template_name = "finanzas/presupuestos/proyectos/presupuestos.html"


#CreateView
class CrearPresupuestosP(TemplateView):
    template_name = "finanzas/presupuestos/proyectos/crearPresupuestos.html"

#UpdateView
class EditarPresupuestosP(TemplateView):
    template_name = "finanzas/presupuestos/proyectos/editarPresupuestos.html"



#------------------------------------------------------------------------------------------

#---------------------------- Vista de Compras de Centro de Costos con CRUD ------------------------------
    
#ListView
class CompraCDC(TemplateView):
    template_name = "finanzas/compra/centro-de-costos/compra.html"


#CreateView
class CrearCompraCDC(TemplateView):
    template_name = "finanzas/compra/centro-de-costos/crearCompra.html"

#UpdateView
class EditarCompraCDC(TemplateView):
    template_name = "finanzas/compra/centro-de-costos/editarCompra.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Compras de Proyectos con CRUD ------------------------------
    
#ListView
class CompraP(TemplateView):
    template_name = "finanzas/compra/proyectos/compra.html"

#CreateView
class CrearCompraP(TemplateView):
    template_name = "finanzas/compra/proyectos/crearCompra.html"

#UpdateView
class EditarCompraP(TemplateView):
    template_name = "finanzas/compra/proyectos/editarCompra.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de ventas con CRUD ------------------------------
    
#ListView
class Venta(TemplateView):
    template_name = "finanzas/venta/venta.html"

#CreateView
class CrearVenta(TemplateView):
    template_name = "finanzas/venta/crearVenta.html"

#UpdateView
class EditarVenta(TemplateView):
    template_name = "finanzas/venta/editarVenta.html"


#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Proveedores con CRUD ------------------------------
    
class Proveedor(TemplateView):
    template_name = "finanzas/proveedores/proveedores.html"

#CreateView
class CrearProveedor(TemplateView):
    template_name = "finanzas/proveedores/crearProveedores.html"

#UpdateView
class EditarProveedor(TemplateView):
    template_name = "finanzas/proveedores/editarProveedores.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Impuestos con CRUD ------------------------------
    
class Impuestos(TemplateView):
    template_name = "finanzas/impuestos/impuestos.html"

#CreateView
class CrearImpuestos(TemplateView):
    template_name = "finanzas/impuestos/crearImpuestos.html"

#UpdateView
class EditarImpuestos(TemplateView):
    template_name = "finanzas/impuestos/editarImpuestos.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Flujo de Caja con CRUD ------------------------------
    
class FlujoDeCaja(TemplateView):
    template_name = "finanzas/flujo-de-caja/flujoDeCaja.html"

#CreateView
class CrearFlujoDeCaja(TemplateView):
    template_name = "finanzas/flujo-de-caja/crearFlujoDeCaja.html"

#UpdateView
class EditarFlujoDeCaja(TemplateView):
    template_name = "finanzas/flujo-de-caja/editarFlujoDeCaja.html"