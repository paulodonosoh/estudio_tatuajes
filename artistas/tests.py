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

	def test_datos_del_artista_persisten_en_base(self):
		artista_guardado = Artista.objects.get(pk=self.artista.pk)

		self.assertEqual(artista_guardado.estilos, ['Japonés', 'Ilustrativo', 'Color'])
		self.assertEqual(artista_guardado.contacto, 'noah@example.com')

	def test_listado_no_falla_si_artista_no_tiene_url(self):
		Artista.objects.create(nombre='Artista sin URL')

		response = self.client.get(reverse('artistas'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Artista sin URL')

	def test_crear_artista_desde_formulario(self):
		response = self.client.post(reverse('crear_artista'), {
			'nombre': 'Paula nueva',
			'estilos': 'Tradicional, Blackwork',
			'descripcion': 'Diseños personalizados.',
			'contacto': 'paula@example.com',
			'dias': 'Martes',
			'horarios': '10:00 a 18:00',
			'url': 'paula-nueva',
		})

		self.assertRedirects(response, reverse('artistas'))
		artista = Artista.objects.get(url='paula-nueva')
		self.assertEqual(artista.estilos, ['Tradicional', 'Blackwork'])

	def test_editar_artista_desde_formulario(self):
		response = self.client.post(reverse('editar_artista', args=[self.artista.pk]), {
			'nombre': 'Noah actualizado',
			'estilos': 'Japonés, Color',
			'descripcion': 'Nueva descripción.',
			'contacto': 'noah@example.com',
			'dias': 'Lunes',
			'horarios': '12:00 a 20:00',
			'url': 'noah-prueba',
		})

		self.assertRedirects(response, reverse('artistas'))
		self.artista.refresh_from_db()
		self.assertEqual(self.artista.nombre, 'Noah actualizado')
		self.assertEqual(self.artista.estilos, ['Japonés', 'Color'])

	def test_eliminar_artista_requiere_confirmacion_post(self):
		url = reverse('eliminar_artista', args=[self.artista.pk])
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTrue(Artista.objects.filter(pk=self.artista.pk).exists())

		response = self.client.post(url)

		self.assertRedirects(response, reverse('artistas'))
		self.assertFalse(Artista.objects.filter(pk=self.artista.pk).exists())
