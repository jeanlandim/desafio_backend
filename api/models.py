from django.db import models

class Api(models.Model):
    titulo = models.CharField(max_length=20)
    texto = models.TextField()

