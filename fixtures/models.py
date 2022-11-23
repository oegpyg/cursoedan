from django.db import models


# ORM
# QATAR
class Paises(models.Model):
    """Esta es la clase para gestionar paises"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.nombre} [{self.codigo}]"

# GRUPO A


class FaseGrupos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nombre}"


class FaseGruposPaises(models.Model):
    id = models.AutoField(primary_key=True)
    fg = models.ForeignKey(FaseGrupos, on_delete=models.DO_NOTHING)
    pais = models.ForeignKey(Paises, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.fg} > {self.pais}'
