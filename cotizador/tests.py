from django.test import TestCase
from django.urls import reverse

from .models import Cotizacion


class CotizadorTests(TestCase):
	def test_pagina_cotizador_carga(self):
		response = self.client.get(reverse('cotizador'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Cotiza tu Tatuaje')

	def test_calcula_precio_desde_el_formulario(self):
		response = self.client.post(reverse('cotizador'), {
			'nombre': 'Ana Pérez',
			'tamano': '10',
		})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Precio Estimado: $150000')
		self.assertEqual(Cotizacion.objects.count(), 1)
		cotizacion = Cotizacion.objects.get()
		self.assertEqual(cotizacion.nombre_cliente, 'Ana Pérez')
		self.assertEqual(cotizacion.tamano_cm, 10)
		self.assertEqual(cotizacion.precio_estimado, 150000)
		self.assertIsNotNone(cotizacion.creado_en)

	def test_no_guarda_cotizacion_sin_nombre(self):
		response = self.client.post(reverse('cotizador'), {'tamano': '10'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'ingresa tu nombre')
		self.assertEqual(Cotizacion.objects.count(), 0)
