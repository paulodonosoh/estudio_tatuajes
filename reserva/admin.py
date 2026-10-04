from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	list_display = (
		'nombre_cliente',
		'artista',
		'fecha',
		'hora_inicio',
		'hora_fin',
		'estado',
		'telefono',
	)
	list_filter = ('estado', 'artista')
	search_fields = ('nombre_cliente', 'telefono', 'email')
	date_hierarchy = 'fecha'
	ordering = ('fecha', 'hora_inicio')
	readonly_fields = ('creado_en', 'actualizado_en')
