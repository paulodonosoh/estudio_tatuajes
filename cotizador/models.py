from django.db import models


class Cotizacion(models.Model):
	nombre_cliente = models.CharField(max_length=100)
	tamano_cm = models.DecimalField(max_digits=8, decimal_places=2)
	precio_estimado = models.DecimalField(max_digits=12, decimal_places=2)
	creado_en = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-creado_en']

	def __str__(self):
		return f'{self.nombre_cliente}: {self.tamano_cm} cm² - ${self.precio_estimado}'
