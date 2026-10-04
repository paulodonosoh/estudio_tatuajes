from django.urls import path

from . import views

urlpatterns = [
    path('', views.artistas, name='artistas'),
    path('gestionar/crear/', views.crear_artista, name='crear_artista'),
    path('gestionar/<int:pk>/editar/', views.editar_artista, name='editar_artista'),
    path('gestionar/<int:pk>/eliminar/', views.eliminar_artista, name='eliminar_artista'),
    path('<slug:url>/', views.detalle_artista, name='detalle_artista'),
]