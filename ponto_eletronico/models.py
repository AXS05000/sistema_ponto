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


MESES_CHOICES = (
    ('Janeiro', 'Janeiro'),
    ('Fevereiro', 'Fevereiro'),
    ('Março', 'Março'),
    ('Abril', 'Abril'),
    ('Maio', 'Maio'),
    ('Junho', 'Junho'),
    ('Julho', 'Julho'),
    ('Agosto', 'Agosto'),
    ('Setembro', 'Setembro'),
    ('Outubro', 'Outubro'),
    ('Novembro', 'Novembro'),
    ('Dezembro', 'Dezembro'),
)

ANOS_CHOICES = (
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
)

TIPO_CHOICES = (
    ('21 a 20', '21 a 20'),
    ('01 a 30', '01 a 30'),

)


class Competencia(models.Model):
    tipo_comp = models.CharField(
        'Tipo de Competência', max_length=50, choices=TIPO_CHOICES)
    mes = models.CharField('Mês', max_length=50, choices=MESES_CHOICES)
    ano = models.CharField('Ano', max_length=50, choices=ANOS_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.mes}/{self.ano}"


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
