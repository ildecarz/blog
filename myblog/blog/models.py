from django.db import models

# Create your models here.
class Blog(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	fecha = models.DateTimeField()
	autor = models.CharField(max_length=20)
	publicado = models.BooleanField(blank=False)