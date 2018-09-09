from django.db import models

class Egresados(models.Model):
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	promocion = models.CharField(max_length=5)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=40)
	correo_electronico = models.CharField(max_length=40)
	ultimos_estudios = models.CharField(max_length=40)
	lugar_ultimo_estudio = models.CharField(max_length=80)