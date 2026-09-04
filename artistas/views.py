from django.shortcuts import render

def artistas(request):
    artistas = [
        {
            'nombre': 'Israel',
            'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional'],
            'descripcion': 'Israel combina el realismo y la tradición con un gran cuidado por el detalle y la precisión.',
            'imagen': 'https://duckduckgo.com/?q=foto+de+un+tatuador&t=brave&ia=images&iax=images&iai=https%3A%2F%2Felinformantememphis.com%2Fwp-content%2Fuploads%2F2025%2F09%2FIMG_3131-2-scaled.jpg',
            'url': 'israel',
        },
        {
            'nombre': 'Paulo',
            'estilos': ['Blackwork', 'Geométrico', 'Minimalista'],
            'descripcion': 'Paulo crea composiciones limpias y expresivas, combinando líneas firmes con geometría y contraste.',
            'imagen': 'https://images.unsplash.com/photo-1565051-5d0b4b8a9f2f?auto=format&fit=crop&w=900&q=85',
            'url': 'paulo',
        },
        {
            'nombre': 'Noah',
            'estilos': ['Japonés', 'Ilustrativo', 'Color'],
            'descripcion': 'Noah desarrolla piezas llenas de color e inspiración japonesa, con una mirada especialmente ilustrativa.',
            'imagen': 'https://images.unsplash.com/photo-1611501275019-9b5c2c0f0e1a?auto=format&fit=crop&w=900&q=85',
            'url': 'noah',
        },
    ]
    return render(request, 'artistas/home_artistas.html', {'artistas': artistas})

def israel(request):
    return render(request, 'artistas/israel.html', {
        'nombre': 'Israel',
        'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional'],
        'descripcion': 'Israel combina el realismo y la tradición con un gran cuidado por el detalle y la precisión.',
        'contacto': 'israel@estudiotatuajes.cl | +56 9 1234 5678',
        'dias': 'Lunes, miércoles y viernes',
        'horarios': '10:00 a 18:00',
        'imagen': 'https://duckduckgo.com/?q=foto+de+un+tatuador&t=brave&ia=images&iax=images&iai=https%3A%2F%2Felinformantememphis.com%2Fwp-content%2Fuploads%2F2025%2F09%2FIMG_3131-2-scaled.jpg',
    })

def paulo(request):
    return render(request, 'artistas/paulo.html', {
        'nombre': 'Paulo',
        'estilos': ['Blackwork', 'Geométrico', 'Minimalista'],
        'descripcion': 'Paulo crea composiciones limpias y expresivas, combinando líneas firmes con geometría y contraste.',
        'contacto': 'paulo@estudiotatuajes.cl | +56 9 2345 6789',
        'dias': 'Martes, jueves y sábado',
        'horarios': '11:00 a 19:00',
        'imagen': 'https://images.unsplash.com/photo-1565051-5d0b4b8a9f2f?auto=format&fit=crop&w=1200&q=85',
    })

def noah(request):
    return render(request, 'artistas/noah.html', {
        'nombre': 'Noah',
        'estilos': ['Japonés', 'Ilustrativo', 'Color'],
        'descripcion': 'Noah desarrolla piezas llenas de color e inspiración japonesa, con una mirada especialmente ilustrativa.',
        'contacto': 'noah@estudiotatuajes.cl | +56 9 3456 7890',
        'dias': 'Lunes, martes y jueves',
        'horarios': '12:00 a 20:00',
        'imagen': 'https://images.unsplash.com/photo-1611501275019-9b5c2c0f0e1a?auto=format&fit=crop&w=1200&q=85',
    })
