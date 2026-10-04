from datetime import datetime, time, timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from artistas.models import Artista

from .forms import ReservaForm
from .models import Reserva

# Create your views here.
def calendario_view(request):
    hoy = timezone.localdate()
    lunes_actual = hoy - timedelta(days=hoy.weekday())
    try:
        semana_actual = int(request.GET.get('semana', 0))
    except (TypeError, ValueError):
        semana_actual = 0
    semana_actual = max(0, min(semana_actual, 3))
    lunes = lunes_actual + timedelta(weeks=semana_actual)
    dias = [
        {
            'fecha': lunes + timedelta(days=numero_dia),
            'nombre': nombre_dia,
        }
        for numero_dia, nombre_dia in enumerate(
            ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        )
    ]
    horas = [time(hora, 0) for hora in range(9, 18)]
    semanas = [
        {
            'numero': numero_semana,
            'inicio': lunes_actual + timedelta(weeks=numero_semana),
            'fin': lunes_actual + timedelta(weeks=numero_semana, days=4),
        }
        for numero_semana in range(4)
    ]
    artistas = Artista.objects.order_by('nombre')
    artista_id = request.GET.get('artista')
    artista_seleccionado = artistas.filter(pk=artista_id).first()
    if artista_seleccionado is None:
        artista_seleccionado = artistas.first()

    reservas = Reserva.objects.filter(
        fecha__range=(dias[0]['fecha'], dias[-1]['fecha']),
        estado__in=(
            Reserva.Estado.PENDIENTE,
            Reserva.Estado.CONFIRMADA,
        ),
    )
    if artista_seleccionado is not None:
        reservas = reservas.filter(artista=artista_seleccionado)

    reservas_por_fecha = {}
    for reserva in reservas:
        reservas_por_fecha.setdefault(reserva.fecha, []).append(reserva)

    filas_calendario = []
    for hora in horas:
        hora_fin = (datetime.combine(lunes, hora) + timedelta(hours=1)).time()
        celdas = []
        for dia in dias:
            ocupado = any(
                reserva.hora_inicio < hora_fin and reserva.hora_fin > hora
                for reserva in reservas_por_fecha.get(dia['fecha'], [])
            )
            celdas.append({
                'fecha': dia['fecha'],
                'estado': 'Ocupado' if ocupado else 'Disponible',
                'ocupado': ocupado,
            })
        filas_calendario.append({'hora': hora, 'celdas': celdas})

    contexto = {
        'dias': dias,
        'filas_calendario': filas_calendario,
        'artistas': artistas,
        'artista_seleccionado': artista_seleccionado,
        'semana_actual': semana_actual,
        'semanas': semanas,
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
