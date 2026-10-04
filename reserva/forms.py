from django import forms
from django.utils import timezone

from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = (
            'nombre_cliente',
            'telefono',
            'email',
            'artista',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'descripcion',
        )
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.localdate():
            raise forms.ValidationError(
                'La fecha de la reserva no puede estar en el pasado.'
            )
        return fecha