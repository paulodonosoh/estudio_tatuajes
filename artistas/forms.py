from django import forms

from .models import Artista


class ArtistaForm(forms.ModelForm):
	estilos = forms.CharField(
		required=False,
		help_text='Separa los estilos con comas.',
	)

	class Meta:
		model = Artista
		fields = [
			'nombre',
			'estilos',
			'descripcion',
			'contacto',
			'dias',
			'horarios',
			'imagen',
			'url',
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if self.instance and self.instance.pk and not self.is_bound:
			self.initial['estilos'] = ', '.join(self.instance.estilos)

	def clean_estilos(self):
		return [
			estilo.strip()
			for estilo in self.cleaned_data['estilos'].split(',')
			if estilo.strip()
		]