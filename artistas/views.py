from django.shortcuts import render

def artistas(request):
    artistas = [
        {
            'nombre': 'Israel',
            'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional'],
            'descripcion': 'Israel combina el realismo y la tradición con un gran cuidado por el detalle y la precisión.',
            'imagen': 'https://images.unsplash.com/photo-1598373182133-52452f7691ef?auto=format&fit=crop&w=900&q=85',
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
    return render(request, 'artistas/artistas.html', {'artistas': artistas})
