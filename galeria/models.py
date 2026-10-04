from django.db import models

class Tatuaje(models.Model):
    artista = models.CharField(max_length=100)
    estilo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    imagen_url = models.CharField(max_length=255, help_text="Ruta estática o URL")
    # COLUMNA PARA SEPARAR PESTAÑAS:
    es_disponible = models.BooleanField(default=False, verbose_name="¿Es un diseño disponible (boceto)?")

    def __str__(self):
        return f"{self.titulo} - {self.artista}"