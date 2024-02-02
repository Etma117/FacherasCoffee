from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Producto
from .forms import ProductoForm

class MenuListar(ListView):
    model = Producto
    template_name = 'Menu.html'
    context_object_name = 'Producto'
    

class ProductoCrearView(CreateView):
    model = Producto
    template_name = 'crear_producto.html'
    context_object_name = 'Producto'
    form_class = ProductoForm
    success_url = reverse_lazy('Menu')
    
    def form_valid(self, form):
        messages.success(self.request, 'El platillo se ha creado exitosamente.')
        return super().form_valid(form)
    
class ProductoEditarView(UpdateView):
    model = Producto
    template_name = 'editar_producto.html'
    context_object_name = 'Producto'
    form_class = ProductoForm
    success_url = reverse_lazy('Menu')
    
    def form_valid(self, form):
        messages.success(self.request, 'El platillo se ha editado exitosamente.')
        return super().form_valid(form)
    

class ProductoEliminarView(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    context_object_name = 'Producto'
    success_url = reverse_lazy('Menu')

    def form_valid(self, form):
        messages.error(self.request, 'El platillo se ha dado de baja del menú.')
        return super().form_valid(form)


class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'
    context_object_name = 'Producto'  # Nombre de la variable en la plantilla
    pk_url_kwarg = 'producto_id'  # Nombre del parámetro en la URL