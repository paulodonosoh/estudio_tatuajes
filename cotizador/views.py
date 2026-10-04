from django.shortcuts import render

def calcular_precio(request):
    precio_estimado = None
    
    if request.method == 'POST':
        tamaño = request.POST.get('tamano')
        if tamaño:
            try:
                tamaño_cm = float(tamaño)
                precio_estimado = tamaño_cm * 15000 
            except ValueError:
                precio_estimado = "Error: Por favor ingresa un número válido."

    return render(request, 'cotizador/calculadora.html', {
        'precio_estimado': precio_estimado
    })