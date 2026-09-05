from django.shortcuts import render

def lista_tatuajes(request):
    tatuajes_hechos = [
        {
            'nombre': 'Rosa Tradicional',
            'imagen': 'rosa.jpeg',
            'descripcion': 'Rosa estilo Old School ya cicatrizada.'
        },
        {
            'nombre': 'Lobo Geométrico',
            'imagen': 'lobo.jpeg',
            'descripcion': 'Lobo en blackwork con detalles geométricos.'
        },
        {
            'nombre': 'Dragón Japonés',
            'imagen': 'dragon.jpeg',
            'descripcion': 'Proyecto de manga completa estilo Irezumi.'
        }
    ]

    tatuajes_disponibles = [
        {
            'nombre': 'Old School clásico',
            'imagen': 'boceto1.jpeg',
            'descripcion': 'Diseño Old School clásico. Ideal para el pecho o mano.',
            'precio': '$40.000'
        },
        {
            'nombre': 'Geométricos',
            'imagen': 'boceto2.jpeg',
            'descripcion': 'Pieza Blackwork con puntillismo. Diseño único y exclusivo.',
            'precio': '$60.000'
        },
        {
            'nombre': 'Geisha Tradicional',
            'imagen': 'boceto3.jpeg',
            'descripcion': 'Boceto estilo Irezumi. Listo para adaptarse al antebrazo.',
            'precio': '$80.000'
        }
    ]

    context = {
        'tatuajes_hechos': tatuajes_hechos,
        'tatuajes_disponibles': tatuajes_disponibles,
        'titulo_seccion': 'Nuestra Galería de Trabajos'
    }
    return render(request, 'galeria/galeria.html', context)