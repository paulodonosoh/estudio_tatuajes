from django.shortcuts import render

# Create your views here.
def artistas(request):
    return render(request, 'artistas/artistas.html')

def israel(request):
    context = {
        'nombre': 'Israel', 
        'estilos': ['Realismo', 'Tradicional', 'Neo Tradicional']
    }
    return render(request, 'artistas/israel.html', context)