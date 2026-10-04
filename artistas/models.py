from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    estilos = models.JSONField(default=list, blank=True)
    descripcion = models.TextField(blank=True)
    contacto = models.CharField(max_length=150, blank=True)
    dias = models.CharField(max_length=150, blank=True)
    horarios = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='artistas/', blank=True, null=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre