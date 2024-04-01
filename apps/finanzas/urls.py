from django.urls import path

from . import views

app_name = "app_finanzas"

urlpatterns = [
    #----------------------------- Departamentos ---------------------------
    path('departamentos/', views.Departamentos.as_view(), name='departamentos'),

    #---------------------------- Centro de Costos ----------------------
    path('centroDeCostos/', views.CentroDeCostos.as_view(), name='centroDeCostos'),
    path('crearCentroDeCostos/', views.CrearCentroDeCostos.as_view(), name='crearCentroDeCostos'),
    path('editarCentroDeCostos/', views.EditarCentroDeCostos.as_view(), name='editarCentroDeCostos'),
    #---------------------------- Proyectos ---------------------------
    path('proyectos/', views.Proyectos.as_view(), name='proyectos'),
    path('crearProyectos/', views.CrearProyectos.as_view(), name='crearProyectos'),
    path('editarProyectos/', views.EditarProyectos.as_view(), name='editarProyectos'),
    #----------------------------- Presupuestos de Centro de Costos -------------------------------
    path('presupuestosCDC/', views.PresupuestosCDC.as_view(), name='presupuestosCDC'),
    path('crearPresupuestosCDC/', views.CrearPresupuestosCDC.as_view(), name='crearPresupuestosCDC'),
    path('editarPresupuestosCDC/', views.EditarPresupuestosCDC.as_view(), name='editarPresupuestosCDC'),
    #----------------------------- Presupuestos de Proyectos --------------------------------------
    path('presupuestosP/', views.PresupuestosP.as_view(), name='presupuestosP'),
    path('crearPresupuestosP/', views.CrearPresupuestosP.as_view(), name='crearPresupuestosP'),
    path('editarPresupuestosP/', views.EditarPresupuestosP.as_view(), name='editarPresupuestosP'),

    #----------------------------- Compras --------------------------------------------------
    path('compra/', views.Compra.as_view(), name='compra'),
    path('crearCompra/', views.CrearCompra.as_view(), name='crearCompra'),
    path('editarCompra/', views.EditarCompra.as_view(), name='editarCompra'),
    #----------------------------- Cotizaciones --------------------------------------------------
    path('cotizacionesCompra/', views.CotizacionesCompra.as_view(), name='cotizacionesCompra'),
    path('crearCotizacionesCompra/', views.CrearCotizacionesCompra.as_view(), name='crearCotizacionesCompra'),
    path('editarCotizacionesCompra/', views.EditarCotizacionesCompra.as_view(), name='editarCotizacionesCompra'),
    #----------------------------- Ordenes de Compra --------------------------------------------------
    path('ordenesDeCompra/', views.OrdenesDeCompra.as_view(), name='ordenesDeCompra'),
    path('crearOrdenesDeCompra/', views.CrearOrdenesDeCompra.as_view(), name='crearOrdenesDeCompra'),
    path('editarOrdenesDeCompra/', views.EditarOrdenesDeCompra.as_view(), name='editarOrdenesDeCompra'),
    #----------------------------- Facturas --------------------------------------------------
    path('facturasCompra/', views.FacturasCompra.as_view(), name='facturasCompra'),
    path('crearFacturasCompra/', views.CrearFacturasCompra.as_view(), name='crearFacturasCompra'),
    path('editarFacturasCompra/', views.EditarFacturasCompra.as_view(), name='editarFacturasCompra'),

    #----------------------------- Ventas --------------------------------------
    path('venta/', views.Venta.as_view(), name='venta'),
    path('crearVenta/', views.CrearVenta.as_view(), name='crearVenta'),
    path('editarVenta/', views.EditarVenta.as_view(), name='editarVenta'),
    #----------------------------- Cotizaciones --------------------------------------------------
    path('cotizacionesVenta/', views.CotizacionesVenta.as_view(), name='cotizacionesVenta'),
    path('crearCotizacionesVenta/', views.CrearCotizacionesVenta.as_view(), name='crearCotizacionesVenta'),
    path('editarCotizacionesVenta/', views.EditarCotizacionesVenta.as_view(), name='editarCotizacionesVenta'),
    #----------------------------- Ordenes de Venta --------------------------------------------------
    path('ordenesDeVenta/', views.OrdenesDeVenta.as_view(), name='ordenesDeVenta'),
    path('crearOrdenesDeVenta/', views.CrearOrdenesDeVenta.as_view(), name='crearOrdenesDeVenta'),
    path('editarOrdenesDeVenta/', views.EditarOrdenesDeVenta.as_view(), name='editarOrdenesDeVenta'),
    #----------------------------- Facturas --------------------------------------------------
    path('facturasVenta/', views.FacturasVenta.as_view(), name='facturasVenta'),
    path('crearFacturasVenta/', views.CrearFacturasVenta.as_view(), name='crearFacturasVenta'),
    path('editarFacturasVenta/', views.EditarFacturasVenta.as_view(), name='editarFacturasVenta'),
    
    #----------------------------- Proveedores --------------------------------------
    path('proveedor/', views.Proveedor.as_view(), name='proveedor'),
    path('crearProveedor/', views.CrearProveedor.as_view(), name='crearProveedor'),
    path('editarProveedor/', views.EditarProveedor.as_view(), name='editarProveedor'),
    #----------------------------- Impuestos --------------------------------------
    path('impuestos/', views.Impuestos.as_view(), name='impuestos'),
    path('crearImpuestos/', views.CrearImpuestos.as_view(), name='crearImpuestos'),
    path('editarImpuestos/', views.EditarImpuestos.as_view(), name='editarImpuestos'),
    #----------------------------- Flujo de Caja --------------------------------------
    path('flujoDeCaja/', views.FlujoDeCaja.as_view(), name='flujoDeCaja'),
    path('crearFlujoDeCaja/', views.CrearFlujoDeCaja.as_view(), name='crearFlujoDeCaja'),
    path('editarFlujoDeCaja/', views.EditarFlujoDeCaja.as_view(), name='editarFlujoDeCaja'),

        #----------------------------- Contabilidad --------------------------------------
    path('cuentasContables/', views.CuentasContables.as_view(), name='cuentasContables'),
    path('crearCuentasContables/', views.CrearCuentasContables.as_view(), name='crearCuentasContables'),
    path('editarCuentasContables/', views.EditarCuentasContables.as_view(), name='editarCuentasContables'),


]
