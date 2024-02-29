from django.urls import path
from . import views
from .views import Productos, Carrito_mesa, MostrarCarrito, Carrito_domicilio, EliminarProductoDelCarrito, AgregarCantidadProducto
urlpatterns = [
    path('', views.home, name= 'Comanda'),
    path('domicilio/', views.domicilio, name='Domicilio'),
    path('salon/', views.salon, name='Salon'),
    path('Productos/', Productos.as_view() , name='Productos'),
    path('ver-carrito/', MostrarCarrito.as_view(), name='MostrarCarrito'),
    path('eliminar_producto/<int:carrito_item_id>/', EliminarProductoDelCarrito.as_view(), name='eliminar_producto_carrito'),
    path('carrito_por_mesa/<int:mesa_id>', Carrito_mesa.as_view(), name='carrito_por_mesa'),
    path('carrito_pedido_domicilio/', Carrito_domicilio.as_view(), name='carrito_pedido_domicilio'),
    path('agregar_cantidad_producto/<int:carrito_item_id>/', AgregarCantidadProducto.as_view(), name='agregar_cantidad_producto'),
]
