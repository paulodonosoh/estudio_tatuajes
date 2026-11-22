from django.test import TestCase
from .models import Tatuaje


class GaleriaInicialTests(TestCase):
    def test_trabajos_y_bocetos_iniciales_se_cargan(self):
        imagenes_esperadas = {
            'galeria/images/dragon.jpeg': False,
            'galeria/images/lobo.jpeg': False,
            'galeria/images/rosa.jpeg': False,
            'galeria/images/boceto1.jpeg': True,
            'galeria/images/boceto2.jpeg': True,
            'galeria/images/boceto3.jpeg': True,
        }

        tatuajes = dict(
            Tatuaje.objects.values_list('imagen_url', 'es_disponible')
        )

        for imagen_url, es_disponible in imagenes_esperadas.items():
            with self.subTest(imagen_url=imagen_url):
                self.assertEqual(tatuajes.get(imagen_url), es_disponible)
