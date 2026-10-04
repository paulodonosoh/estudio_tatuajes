from django.shortcuts import render, redirect, get_object_or_404
from .models import Tatuaje
from .forms import TatuajeForm

def lista_tatuajes(request):
    # Filtramos: los que tienen False van a hechos, los que tienen True van a disponibles
    hechos = Tatuaje.objects.filter(es_disponible=False)
    disponibles = Tatuaje.objects.filter(es_disponible=True)
    
    return render(request, 'galeria/galeria.html', {
        'tatuajes_hechos': hechos,
        'tatuajes_disponibles': disponibles
    })

def crear_tatuaje(request):
    if request.method == 'POST':
        form = TatuajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tatuajes')
    else:
        form = TatuajeForm()
    return render(request, 'galeria/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_tatuaje(request, id):
    tatuaje = get_object_or_404(Tatuaje, id=id)
    if request.method == 'POST':
        form = TatuajeForm(request.POST, instance=tatuaje)
        if form.is_valid():
            form.save()
            return redirect('lista_tatuajes')
    else:
        form = TatuajeForm(instance=tatuaje)
    return render(request, 'galeria/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_tatuaje(request, id):
    tatuaje = get_object_or_404(Tatuaje, id=id)
    if request.method == 'POST':
        tatuaje.delete()
        return redirect('lista_tatuajes')
    return render(request, 'galeria/confirmar_eliminar.html', {'tatuaje': tatuaje})