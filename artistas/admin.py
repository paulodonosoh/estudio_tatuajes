from django.contrib import admin

from .models import Artista


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'url', 'contacto', 'dias', 'horarios')
	search_fields = ('nombre', 'descripcion', 'contacto')
	ordering = ('nombre',)
