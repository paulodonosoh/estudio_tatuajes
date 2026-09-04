from django.urls import path
from . import views

urlpatterns = [
    path('calendario/', views.calendario_view, name='calendario'),
    path('formulario/', views.formulario_reserva_view, name='formulario_reserva'),
]