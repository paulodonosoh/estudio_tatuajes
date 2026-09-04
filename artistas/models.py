from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='artistas/', blank=True, null=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre