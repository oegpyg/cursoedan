from django.db import models


# ORM

class Paises(models.Model):
    """Esta es la clase para gestionar paises"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.nombre} [{self.codigo}]"


class FaseGrupos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nombre}"
