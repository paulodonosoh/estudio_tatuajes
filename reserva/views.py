from django.shortcuts import render

# Create your views here.
def calendario_view(request):
    return render(request, 'reserva/calendario.html')


def formulario_reserva_view(request):
    return render(request, 'reserva/formulario_reserva.html')
