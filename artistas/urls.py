from django.urls import path

from . import views

urlpatterns = [
    path('', views.artistas, name='artistas'),
    path('israel/', views.israel, name='israel'),
    path('paulo/', views.paulo, name='paulo'),
    path('noah/', views.noah, name='noah'),
]