from django.db import migrations


TATUAJES_INICIALES = [
    {
        'artista': 'Por asignar',
        'estilo': 'Japonés',
        'titulo': 'Dragón japonés',
        'imagen_url': 'galeria/images/dragon.jpeg',
        'es_disponible': False,
    },
    {
        'artista': 'Por asignar',
        'estilo': 'Geométrico',
        'titulo': 'Lobo geométrico',
        'imagen_url': 'galeria/images/lobo.jpeg',
        'es_disponible': False,
    },
    {
        'artista': 'Por asignar',
        'estilo': 'Tradicional',
        'titulo': 'Rosa tradicional',
        'imagen_url': 'galeria/images/rosa.jpeg',
        'es_disponible': False,
    },
    {
        'artista': 'Por asignar',
        'estilo': 'Tradicional',
        'titulo': 'Flash tradicional',
        'imagen_url': 'galeria/images/boceto1.jpeg',
        'es_disponible': True,
    },
    {
        'artista': 'Por asignar',
        'estilo': 'Geométrico',
        'titulo': 'Diseños geométricos',
        'imagen_url': 'galeria/images/boceto2.jpeg',
        'es_disponible': True,
    },
    {
        'artista': 'Por asignar',
        'estilo': 'Japonés',
        'titulo': 'Retratos japoneses',
        'imagen_url': 'galeria/images/boceto3.jpeg',
        'es_disponible': True,
    },
]


def cargar_tatuajes(apps, schema_editor):
    Tatuaje = apps.get_model('galeria', 'Tatuaje')
    for tatuaje in TATUAJES_INICIALES:
        imagen_url = tatuaje['imagen_url']
        Tatuaje.objects.using(schema_editor.connection.alias).get_or_create(
            imagen_url=imagen_url,
            defaults=tatuaje,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_tatuaje_es_disponible'),
    ]

    operations = [
        migrations.RunPython(cargar_tatuajes, migrations.RunPython.noop),
    ]
