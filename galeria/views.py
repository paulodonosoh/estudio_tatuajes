from django.shortcuts import render

def lista_tatuajes(request):
    tatuajes = [
        {'nombre': 'Rosa Tradicional', 'estilo': 'Old School'},
        {'nombre': 'Lobo Geométrico', 'estilo': 'Blackwork'},
        {'nombre': 'Dragón Japonés', 'estilo': 'Irezumi'}
    ]
    
    context = {
        'tatuajes': tatuajes,
        'titulo_seccion': 'Nuestra Galería de Trabajos'
    }
    return render(request, 'galeria/galeria.html', context)