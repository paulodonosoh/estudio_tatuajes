from django.db import migrations


INITIAL_ARTISTS = [
    {
        'nombre': 'Israel',
        'url': 'israel',
        'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional'],
        'descripcion': 'Israel combina el realismo y la tradición con un gran cuidado por el detalle y la precisión.',
        'contacto': 'israel@estudiotatuajes.cl | +56 9 1234 5678',
        'dias': 'Lunes, miércoles y viernes',
        'horarios': '10:00 a 18:00',
        'imagen': 'artistas/israel.jpg',
    },
    {
        'nombre': 'Paulo',
        'url': 'paulo',
        'estilos': ['Blackwork', 'Geométrico', 'Minimalista'],
        'descripcion': 'Paulo crea composiciones limpias y expresivas, combinando líneas firmes con geometría y contraste.',
        'contacto': 'paulo@estudiotatuajes.cl | +56 9 2345 6789',
        'dias': 'Martes, jueves y sábado',
        'horarios': '11:00 a 19:00',
        'imagen': 'artistas/paulo.jpg',
    },
    {
        'nombre': 'Noah',
        'url': 'noah',
        'estilos': ['Japonés', 'Ilustrativo', 'Color'],
        'descripcion': 'Noah desarrolla piezas llenas de color e inspiración japonesa, con una mirada especialmente ilustrativa.',
        'contacto': 'noah@estudiotatuajes.cl | +56 9 3456 7890',
        'dias': 'Lunes, martes y jueves',
        'horarios': '12:00 a 20:00',
        'imagen': 'artistas/noah.jpg',
    },
]


def create_initial_artists(apps, schema_editor):
    Artista = apps.get_model('artistas', 'Artista')
    database = schema_editor.connection.alias

    for perfil in INITIAL_ARTISTS:
        datos = perfil.copy()
        url = datos.pop('url')
        artista = Artista.objects.using(database).filter(url=url).first()
        if artista is None:
            Artista.objects.using(database).create(url=url, **datos)
            continue

        campos_actualizados = []
        for campo, valor in datos.items():
            if not getattr(artista, campo) and valor:
                setattr(artista, campo, valor)
                campos_actualizados.append(campo)
        if campos_actualizados:
            artista.save(using=database, update_fields=campos_actualizados)


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_rename_bio_artista_descripcion_and_more'),
    ]

    operations = [
        migrations.RunPython(create_initial_artists, migrations.RunPython.noop),
    ]
