from django.shortcuts import render

def artistas(request):
    artistas = [
        {
            'nombre': 'Israel',
            'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional'],
            'descripcion': 'Israel combina el realismo y la tradición con un gran cuidado por el detalle y la precisión.',
            'imagen': '/media/artistas/israel.jpg',
            'url': 'israel',
        },
        {
            'nombre': 'Paulo',
            'estilos': ['Blackwork', 'Geométrico', 'Minimalista'],
            'descripcion': 'Paulo crea composiciones limpias y expresivas, combinando líneas firmes con geometría y contraste.',
            'imagen': '/media/artistas/paulo.jpg',
            'url': 'paulo',
        },
        {
            'nombre': 'Noah',
            'estilos': ['Japonés', 'Ilustrativo', 'Color'],
            'descripcion': 'Noah desarrolla piezas llenas de color e inspiración japonesa, con una mirada especialmente ilustrativa.',
            'imagen': '/media/artistas/noah.jpg',
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
        'imagen': '/media/artistas/israel.jpg',
    })

def paulo(request):
    return render(request, 'artistas/paulo.html', {
        'nombre': 'Paulo',
        'estilos': ['Blackwork', 'Geométrico', 'Minimalista'],
        'descripcion': 'Paulo crea composiciones limpias y expresivas, combinando líneas firmes con geometría y contraste.',
        'contacto': 'paulo@estudiotatuajes.cl | +56 9 2345 6789',
        'dias': 'Martes, jueves y sábado',
        'horarios': '11:00 a 19:00',
        'imagen': '/media/artistas/paulo.jpg',
    })

def noah(request):
    return render(request, 'artistas/noah.html', {
        'nombre': 'Noah',
        'estilos': ['Japonés', 'Ilustrativo', 'Color'],
        'descripcion': 'Noah desarrolla piezas llenas de color e inspiración japonesa, con una mirada especialmente ilustrativa.',
        'contacto': 'noah@estudiotatuajes.cl | +56 9 3456 7890',
        'dias': 'Lunes, martes y jueves',
        'horarios': '12:00 a 20:00',
        'imagen': '/media/artistas/noah.jpg',
    })
