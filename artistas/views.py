from django.shortcuts import get_object_or_404, render

from .models import Artista

def artistas(request):
    artistas = Artista.objects.order_by('nombre')
    return render(request, 'artistas/home_artistas.html', {'artistas': artistas})

def detalle_artista(request, url):
    artista = get_object_or_404(Artista, url=url)
    return render(request, 'artistas/artistas.html', {'artista': artista})
