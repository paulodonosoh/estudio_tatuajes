from django.test import TestCase
from django.urls import reverse

from .models import Artista


class ArtistaViewsTests(TestCase):
	def setUp(self):
		self.artista = Artista.objects.create(
			nombre='Noah prueba',
			estilos=['Japonés', 'Ilustrativo', 'Color'],
			descripcion='Piezas con inspiración japonesa.',
			contacto='noah@example.com',
			dias='Lunes y jueves',
			horarios='12:00 a 20:00',
			url='noah-prueba',
		)

	def test_listado_usa_artistas_guardados(self):
		response = self.client.get(reverse('artistas'))

		self.assertContains(response, 'Noah prueba')
		self.assertContains(response, reverse('detalle_artista', args=['noah-prueba']))

	def test_detalle_muestra_datos_guardados(self):
		response = self.client.get(reverse('detalle_artista', args=['noah-prueba']))

		self.assertContains(response, 'Japonés, Ilustrativo, Color')
		self.assertContains(response, 'Piezas con inspiración japonesa.')
		self.assertContains(response, 'noah@example.com')
		self.assertContains(response, 'Lunes y jueves')
		self.assertContains(response, '12:00 a 20:00')

	def test_listado_no_falla_si_artista_no_tiene_url(self):
		Artista.objects.create(nombre='Artista sin URL')

		response = self.client.get(reverse('artistas'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Artista sin URL')
