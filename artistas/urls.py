from django.urls import path

from . import views

urlpatterns = [
    path('', views.artistas, name='artistas'),
    path('<slug:url>/', views.detalle_artista, name='detalle_artista'),
]