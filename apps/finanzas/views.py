from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView

# Create your views here.


#ListView
class Departamentos(TemplateView):
    # model = MODEL_NAME
    template_name = "pages/finanzas/departamentos/departamentos.html"

    # def get_queryset(self):
    #     queryset = super(model, self).get_queryset()
    #     queryset = queryset.
    #     return queryset


#------------------------ Vista de Centro de Costos con CRUD ------------------------------

#ListView
class CentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/centroDeCostos.html"


#CreateView
class CrearCentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/crearCentroDeCostos.html"

#UpdateView
class EditarCentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/editarCentroDeCostos.html"



#------------------------------------------------------------------------------------------
    

#------------------------------- Vista de Proyectos con CRUD ------------------------------

#ListView
class Proyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/proyectos.html"


#CreateView
class CrearProyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/crearProyectos.html"

#UpdateView
class EditarProyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/editarProyectos.html"



#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Presupuestos de Centro de Costos con CRUD ------------------------------
    
#ListView
class PresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/presupuestos.html"


#CreateView
class CrearPresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/crearPresupuestos.html"

#UpdateView
class EditarPresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/editarPresupuestos.html"

#------------------------------------------------------------------------------------------

#---------------------------- Vista de Presupuestos de Proyectos con CRUD ------------------------------
    
#ListView
class PresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/presupuestos.html"


#CreateView
class CrearPresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/crearPresupuestos.html"

#UpdateView
class EditarPresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/editarPresupuestos.html"



#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Compras con CRUD ------------------------------
    
#ListView
class Compra(TemplateView):
    template_name = "pages/finanzas/compra/compra.html"


#CreateView
class CrearCompra(TemplateView):
    template_name = "pages/finanzas/compra/crearCompra.html"

#UpdateView
class EditarCompra(TemplateView):
    template_name = "pages/finanzas/compra/editarCompra.html"

#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Cotizaciones de Compra con CRUD ------------------------------
    

#ListView
class CotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/cotizaciones.html"


#CreateView
class CrearCotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/crearCotizaciones.html"

#UpdateView
class EditarCotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/editarCotizaciones.html"
    

#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Ordenes de Compra con CRUD ------------------------------
    
#ListView
class OrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/ordenesDeCompra.html"


#CreateView
class CrearOrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/crearOrdenesDeCompra.html"

#UpdateView
class EditarOrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/editarOrdenesDeCompra.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Cotizaciones de Compra con CRUD ------------------------------
    

#ListView
class FacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/facturas.html"

#CreateView
class CrearFacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/crearFactura.html"

#UpdateView
class EditarFacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/editarFactura.html"


#------------------------------------------------------------------------------------------
    
    
#---------------------------- Vista de Ventas con CRUD ------------------------------
    
#ListView
class Venta(TemplateView):
    template_name = "pages/finanzas/venta/venta.html"

#CreateView
class CrearVenta(TemplateView):
    template_name = "pages/finanzas/venta/crearVenta.html"

#UpdateView
class EditarVenta(TemplateView):
    template_name = "pages/finanzas/venta/editarVenta.html"

#------------------------------------------------------------------------------------------

#---------------------------- Vista de Cotizaciones de Venta con CRUD ------------------------------
    

#ListView
class CotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/cotizaciones.html"


#CreateView
class CrearCotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/crearCotizaciones.html"

#UpdateView
class EditarCotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/editarCotizaciones.html"


#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Ordenes de Venta con CRUD ------------------------------
    
#ListView
class OrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/ordenesDeVenta.html"


#CreateView
class CrearOrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/crearOrdenesDeVenta.html"

#UpdateView
class EditarOrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/editarOrdenesDeVenta.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Cotizaciones de Venta con CRUD ------------------------------
    

#ListView
class FacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/facturas.html"

#CreateView
class CrearFacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/crearFactura.html"

#UpdateView
class EditarFacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/editarFactura.html"


#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Proveedores con CRUD ------------------------------
    
class Proveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/proveedores.html"

#CreateView
class CrearProveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/crearProveedores.html"

#UpdateView
class EditarProveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/editarProveedores.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Impuestos con CRUD ------------------------------
    
class Impuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/impuestos.html"

#CreateView
class CrearImpuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/crearImpuestos.html"

#UpdateView
class EditarImpuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/editarImpuestos.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Flujo de Caja con CRUD ------------------------------
    
class FlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/flujoDeCaja.html"

#CreateView
class CrearFlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/crearFlujoDeCaja.html"

#UpdateView
class EditarFlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/editarFlujoDeCaja.html"


#---------------------------- Vista de Contabilidad ------------------------------
    

#ListView
class Contabilidad(TemplateView):
    template_name = "pages/finanzas/contabilidad/contabilidad.html"