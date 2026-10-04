from django.db import models
from django.db.models import F, Q

from artistas.models import Artista


class Reserva(models.Model):
	class Estado(models.TextChoices):
		PENDIENTE = 'pendiente', 'Pendiente'
		CONFIRMADA = 'confirmada', 'Confirmada'
		CANCELADA = 'cancelada', 'Cancelada'
		COMPLETADA = 'completada', 'Completada'
		NO_ASISTIO = 'no_asistio', 'No asistió'

	nombre_cliente = models.CharField(max_length=100)
	telefono = models.CharField(max_length=25)
	email = models.EmailField(blank=True)
	artista = models.ForeignKey(
		Artista,
		on_delete=models.PROTECT,
		related_name='reservas',
	)
	inicio = models.DateTimeField()
	fin = models.DateTimeField()
	descripcion = models.TextField(blank=True)
	estado = models.CharField(
		max_length=20,
		choices=Estado,
		default=Estado.PENDIENTE,
	)
	creado_en = models.DateTimeField(auto_now_add=True)
	actualizado_en = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['inicio']
		constraints = [
			models.CheckConstraint(
				condition=Q(fin__gt=F('inicio')),
				name='reserva_fin_despues_de_inicio',
			),
		]
		indexes = [
			models.Index(fields=['artista', 'inicio']),
			models.Index(fields=['estado', 'inicio']),
		]

	def __str__(self):
		return f'{self.nombre_cliente} - {self.inicio:%d/%m/%Y %H:%M}'
