from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase

from artistas.models import Artista

from .models import Reserva


class ReservaAPITests(APITestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='api-test-user',
			password='test-password',
		)
		self.artista = Artista.objects.create(nombre='Artista de prueba')
		self.list_url = '/api/reservas/'
		self.payload = {
			'nombre_cliente': 'Cliente API',
			'telefono': '56912345678',
			'email': 'cliente@example.com',
			'artista': self.artista.pk,
			'fecha': (timezone.localdate() + timedelta(days=1)).isoformat(),
			'hora_inicio': '10:00:00',
			'hora_fin': '11:00:00',
			'descripcion': 'Reserva creada en una prueba API',
		}

	def authenticate(self):
		response = self.client.post(
			'/api/token/',
			{'username': 'api-test-user', 'password': 'test-password'},
			format='json',
		)
		self.assertEqual(response.status_code, 200)
		self.client.credentials(
			HTTP_AUTHORIZATION=f"Bearer {response.data['access']}"
		)

	def test_obtiene_tokens_jwt(self):
		response = self.client.post(
			'/api/token/',
			{'username': 'api-test-user', 'password': 'test-password'},
			format='json',
		)

		self.assertEqual(response.status_code, 200)
		self.assertIn('access', response.data)
		self.assertIn('refresh', response.data)

	def test_listado_publico_devuelve_json(self):
		response = self.client.get(self.list_url)

		self.assertEqual(response.status_code, 200)
		self.assertIsInstance(response.data, list)

	def test_creacion_sin_token_es_rechazada(self):
		response = self.client.post(self.list_url, self.payload, format='json')

		self.assertEqual(response.status_code, 401)

	def test_crud_autenticado(self):
		self.authenticate()

		create_response = self.client.post(
			self.list_url,
			self.payload,
			format='json',
		)
		self.assertEqual(create_response.status_code, 201)
		reserva_id = create_response.data['id']

		detail_url = f'{self.list_url}{reserva_id}/'
		retrieve_response = self.client.get(detail_url)
		self.assertEqual(retrieve_response.status_code, 200)

		update_response = self.client.patch(
			detail_url,
			{'estado': Reserva.Estado.CONFIRMADA},
			format='json',
		)
		self.assertEqual(update_response.status_code, 200)
		self.assertEqual(update_response.data['estado'], Reserva.Estado.CONFIRMADA)

		delete_response = self.client.delete(detail_url)
		self.assertEqual(delete_response.status_code, 204)

	def test_datos_invalidos_devuelven_errores_json(self):
		self.authenticate()
		invalid_date_payload = {
			**self.payload,
			'fecha': (timezone.localdate() - timedelta(days=1)).isoformat(),
		}
		date_response = self.client.post(
			self.list_url,
			invalid_date_payload,
			format='json',
		)

		self.assertEqual(date_response.status_code, 400)
		self.assertIn('fecha', date_response.data)

		invalid_time_payload = {
			**self.payload,
			'hora_inicio': '14:00:00',
			'hora_fin': '13:00:00',
		}
		time_response = self.client.post(
			self.list_url,
			invalid_time_payload,
			format='json',
		)

		self.assertEqual(time_response.status_code, 400)
		self.assertIn('hora_fin', time_response.data)
