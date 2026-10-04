from django.test import TestCase
from django.urls import reverse


class CotizadorTests(TestCase):
	def test_pagina_cotizador_carga(self):
		response = self.client.get(reverse('cotizador'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Cotiza tu Tatuaje')

	def test_calcula_precio_desde_el_formulario(self):
		response = self.client.post(reverse('cotizador'), {'tamano': '10'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Precio Estimado: $150000,0')
