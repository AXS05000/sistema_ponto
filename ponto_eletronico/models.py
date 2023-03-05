from django.db import models
from django.utils import timezone

from usuarios.models import CustomUsuario


class Departamento(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    usuario = models.OneToOneField(CustomUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Ponto(models.Model):
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    competencia = models.CharField(max_length=7)
    entrada = models.TimeField(blank=True, null=True)
    entrada_almoco = models.TimeField(blank=True, null=True)
    saida_almoco = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.funcionario} - {self.data}"
