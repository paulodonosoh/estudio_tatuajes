from decimal import Decimal, InvalidOperation

from django.shortcuts import render

from .models import Cotizacion


def calcular_precio(request):
    precio_estimado = None
    error = None
    
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre', '').strip()
        tamaño = request.POST.get('tamano')
        if not nombre_cliente:
            error = 'Por favor, ingresa tu nombre para calcular y guardar la cotización.'
        elif not tamaño:
            error = 'Por favor, ingresa el tamaño del tatuaje en cm².'
        else:
            try:
                tamaño_cm = Decimal(tamaño)
                if not tamaño_cm.is_finite():
                    raise InvalidOperation
                precio_estimado = tamaño_cm * Decimal('15000')
                Cotizacion.objects.create(
                    nombre_cliente=nombre_cliente,
                    tamano_cm=tamaño_cm,
                    precio_estimado=precio_estimado,
                )
            except (InvalidOperation, ValueError):
                error = 'Por favor, ingresa un tamaño numérico válido.'

    return render(request, 'cotizador/calculadora.html', {
        'precio_estimado': precio_estimado,
        'error': error,
    })