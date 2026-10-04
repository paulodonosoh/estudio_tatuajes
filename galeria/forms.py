from django import forms
from .models import Tatuaje

class TatuajeForm(forms.ModelForm):
    class Meta:
        model = Tatuaje
        fields = '__all__'

    # Validación propia exigida por la rúbrica (ej: mínimo 3 caracteres)
    def clean_artista(self):
        artista = self.cleaned_data.get('artista')
        if len(artista) < 3:
            raise forms.ValidationError("El nombre del artista debe tener al menos 3 caracteres.")
        return artista