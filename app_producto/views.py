from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm


# Create your views here.
def index(request):
  return render(request, 'productos/index.html', {
    'productos': Producto.objects.all()
  })


def view_producto(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST, request.FILES)
    if form.is_valid():
      new_nombre_producto = form.cleaned_data['nombre_producto']
      new_cantidad = form.cleaned_data['cantidad']
      new_proveedor_id = form.cleaned_data['proveedor_id']
      new_precio = form.cleaned_data['precio']
      new_almacen_id = form.cleaned_data['almacen_id']
      new_foto = form.cleaned_data['foto']

      new_producto = Producto(
        nombre_producto=new_nombre_producto,
        cantidad=new_cantidad,
        proveedor_id=new_proveedor_id,
        precio=new_precio,
        almacen_id=new_almacen_id,
        foto=new_foto
      )
      new_producto.save()
      return render(request, 'productos/add.html', {
        'form': ProductoForm(),
        'success': True
      })
  else:
    form = ProductoForm()
  return render(request, 'productos/add.html', {
    'form': ProductoForm()
  })


def edit(request, id):
  if request.method == 'POST':
    producto = Producto.objects.get(pk=id)
    form = ProductoForm(request.POST, request.FILES, instance=producto)
    if form.is_valid():
      form.save()
      return render(request, 'productos/edit.html', {
        'form': form,
        'success': True
      })
  else:
    producto = Producto.objects.get(pk=id)
    form = ProductoForm(instance=producto)
  return render(request, 'productos/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    producto = Producto.objects.get(pk=id)
    producto.delete()
  return HttpResponseRedirect(reverse('index'))