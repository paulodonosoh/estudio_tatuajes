from datetime import timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import ReservaForm
from .models import Reserva

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
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La reserva se creó correctamente.')
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(
        request,
        'reserva/formulario_reserva.html',
        {'form': form},
    )


def lista_reservas_view(request):
    reservas = Reserva.objects.select_related('artista').all()
    return render(
        request,
        'reserva/lista_reservas.html',
        {'reservas': reservas},
    )


def editar_reserva_view(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'La reserva se actualizó correctamente.')
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(
        request,
        'reserva/editar_reserva.html',
        {'form': form, 'reserva': reserva},
    )


def eliminar_reserva_view(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'La reserva se eliminó correctamente.')
        return redirect('lista_reservas')

    return render(
        request,
        'reserva/confirmar_eliminacion.html',
        {'reserva': reserva},
    )
