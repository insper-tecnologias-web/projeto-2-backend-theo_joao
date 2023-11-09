from django.db import models


class Filme(models.Model):
    title = models.CharField(max_length=200)
    generos = models.JSONField()
    streamings = models.JSONField()
    links = models.JSONField()
    def __str__(self):
        return self.title

class Usuario(models.Model):
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    favoritos = models.ManyToManyField(Filme, blank=True, null=True)
    def __str__(self):
        return self.login
    