from django.urls import path
from . import views

urlpatterns = [
    path('calendario/', views.calendario_view, name='calendario'),
    path('formulario/', views.formulario_reserva_view, name='formulario_reserva'),
    path('lista/', views.lista_reservas_view, name='lista_reservas'),
    path('<int:reserva_id>/editar/', views.editar_reserva_view, name='editar_reserva'),
    path('<int:reserva_id>/eliminar/', views.eliminar_reserva_view, name='eliminar_reserva'),
]