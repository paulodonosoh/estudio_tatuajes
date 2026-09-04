from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def calendario_view(request):
    hoy = timezone.localdate()
    lunes = hoy - timedelta(days=hoy.weekday())
    dias = [
        {
            'fecha': lunes + timedelta(days=numero_dia),
            'nombre': nombre_dia,
        }
        for numero_dia, nombre_dia in enumerate(
            ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        )
    ]
    horas = [
        '09:00', '10:00', '11:00', '12:00',
        '13:00', '14:00', '15:00', '16:00', '17:00',
    ]

    # Datos de prueba hasta que exista el modelo de reservas.
    horas_ocupadas = {
        (1, '09:00'), (4, '09:00'),
        (2, '10:00'),
        (0, '11:00'), (3, '11:00'),
        (1, '12:00'),
        (0, '13:00'), (1, '13:00'), (4, '13:00'),
        (2, '14:00'),
        (1, '15:00'), (3, '15:00'),
        (2, '16:00'),
        (3, '17:00'),
    }
    filas_calendario = []
    for hora in horas:
        celdas = []
        for numero_dia, dia in enumerate(dias):
            ocupado = (numero_dia, hora) in horas_ocupadas
            celdas.append({
                'fecha': dia['fecha'],
                'estado': 'Ocupado' if ocupado else 'Disponible',
                'ocupado': ocupado,
            })
        filas_calendario.append({'hora': hora, 'celdas': celdas})

    contexto = {
        'dias': dias,
        'filas_calendario': filas_calendario,
        'inicio_semana': dias[0]['fecha'],
        'fin_semana': dias[-1]['fecha'],
    }
    return render(request, 'reserva/calendario.html', contexto)


def formulario_reserva_view(request):
    contexto = {
        'artistas': [
            {'valor': 'israel', 'nombre': 'Israel'},
            {'valor': 'noah', 'nombre': 'Noah'},
            {'valor': 'paulo', 'nombre': 'Paulo'},
        ],
        'fecha_minima': timezone.localdate().isoformat(),
        'hora_inicial': '09:00',
    }
    return render(request, 'reserva/formulario_reserva.html', contexto)
