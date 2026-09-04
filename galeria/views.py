from django.shortcuts import render

def lista_tatuajes(request):
    artistas = [
        {
            'persona': 'Israel Vargas',
            'estilo': 'Old School',
            'creados': ['Rosa Tradicional', 'Ancla clásica'],
            'puede_hacer': ['Pantera Negra', 'Daga Tradicional'],
            'imagen': 'galeria/img/tatuaje1.jpg'
        },
        {
            'persona': 'Paulo Donoso',
            'estilo': 'Blackwork',
            'creados': ['Lobo Geométrico', 'Mandalas'],
            'puede_hacer': ['Geometría Sagrada', 'Dotwork'],
            'imagen': 'galeria/img/tatuaje2.jpg'
        },
        {
            'persona': 'Noah Del Desposito',
            'estilo': 'Irezumi',
            'creados': ['Dragón Japonés', 'Koi Fish'],
            'puede_hacer': ['Hannya Mask', 'Samurai'],
            'imagen': 'galeria/img/tatuaje3.jpg'
        }
    ]
    
    context = {
        'artistas': artistas,
        'titulo_seccion': 'Nuestros Artistas y Trabajos'
    }
    return render(request, 'galeria/galeria.html', context)