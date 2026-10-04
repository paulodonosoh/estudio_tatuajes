from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tatuajes, name='lista_tatuajes'),
    path('crear/', views.crear_tatuaje, name='crear_tatuaje'),
    path('editar/<int:id>/', views.editar_tatuaje, name='editar_tatuaje'),
    path('eliminar/<int:id>/', views.eliminar_tatuaje, name='eliminar_tatuaje'),
]