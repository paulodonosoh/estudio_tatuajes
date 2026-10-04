from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArtistaForm
from .models import Artista


def artistas(request):
    artistas = Artista.objects.order_by('nombre')
    return render(request, 'artistas/home_artistas.html', {'artistas': artistas})


def detalle_artista(request, url):
    artista = get_object_or_404(Artista, url=url)
    return render(request, 'artistas/artistas.html', {'artista': artista})


def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artistas')
    else:
        form = ArtistaForm()
    return render(request, 'artistas/formulario_artista.html', {
        'form': form,
        'accion': 'Crear',
    })


def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artistas/formulario_artista.html', {
        'form': form,
        'accion': 'Editar',
    })


def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('artistas')
    return render(request, 'artistas/confirmar_eliminar_artista.html', {
        'artista': artista,
    })
