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
    #----------------------------- Compras de Centro de Costos --------------------------------------
    path('compraCDC/', views.CompraCDC.as_view(), name='compraCDC'),
    path('crearCompraCDC/', views.CrearCompraCDC.as_view(), name='crearCompraCDC'),
    path('editarCompraCDC/', views.EditarCompraCDC.as_view(), name='editarCompraCDC'),
    #----------------------------- Compras de Proyectos --------------------------------------
    path('compraP/', views.CompraP.as_view(), name='compraP'),
    path('crearCompraP/', views.CrearCompraP.as_view(), name='crearCompraP'),
    path('editarCompraP/', views.EditarCompraP.as_view(), name='editarCompraP'),
    #----------------------------- Ventas --------------------------------------
    path('venta/', views.Venta.as_view(), name='venta'),
    path('crearVenta/', views.CrearVenta.as_view(), name='crearVenta'),
    path('editarVenta/', views.EditarVenta.as_view(), name='editarVenta'),
    #----------------------------- Proveedores --------------------------------------
    path('proveedor/', views.Proveedor.as_view(), name='proveedor'),
    path('crearProveedor/', views.CrearProveedor.as_view(), name='crearProveedor'),
    path('editarProveedor/', views.EditarProveedor.as_view(), name='editarProveedor'),
    #----------------------------- Impuestos --------------------------------------
    path('impuestos/', views.Impuestos.as_view(), name='impuestos'),
    path('crearImpuestos/', views.CrearImpuestos.as_view(), name='crearImpuestos'),
    path('editarImpuestos/', views.EditarImpuestos.as_view(), name='editarImpuestos'),
    #----------------------------- Impuestos --------------------------------------
    path('flujoDeCaja/', views.FlujoDeCaja.as_view(), name='flujoDeCaja'),
    path('crearFlujoDeCaja/', views.CrearFlujoDeCaja.as_view(), name='crearFlujoDeCaja'),
    path('editarFlujoDeCaja/', views.EditarFlujoDeCaja.as_view(), name='editarFlujoDeCaja'),


]
