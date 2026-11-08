from django.utils import timezone
from rest_framework import serializers

from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = (
            'id',
            'nombre_cliente',
            'telefono',
            'email',
            'artista',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'descripcion',
            'estado',
            'creado_en',
            'actualizado_en',
        )
        read_only_fields = ('id', 'creado_en', 'actualizado_en')

    def validate_fecha(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError(
                'La fecha de la reserva no puede estar en el pasado.'
            )
        return value

    def validate(self, attrs):
        hora_inicio = attrs.get(
            'hora_inicio',
            getattr(self.instance, 'hora_inicio', None),
        )
        hora_fin = attrs.get(
            'hora_fin',
            getattr(self.instance, 'hora_fin', None),
        )
        if hora_inicio and hora_fin and hora_fin <= hora_inicio:
            raise serializers.ValidationError({
                'hora_fin': 'Debe ser posterior a hora_inicio.',
            })
        return attrs
