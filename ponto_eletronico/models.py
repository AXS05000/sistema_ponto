from django.db import models
from django.utils import timezone

from usuarios.models import CustomUsuario

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


class RegraDePonto(models.Model):
    nome = models.CharField('Nome da Regra de Ponto', max_length=80)
    toleranciaentrada = models.DurationField()
    toleranciasaida = models.DurationField()
    horaextraautorizada = models.BooleanField(default=False)
    periodohoranoturna_inicio = models.TimeField()
    periodohoranoturna_fim = models.TimeField()

    def __str__(self):
        return f"{self.nome}"


class Departamento(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Filial(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class CentroDeCusto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    rg = models.CharField('RG', max_length=54)
    cpf = models.DecimalField(
        'CPF', max_digits=11, decimal_places=0, null=True, blank=True)
    pis = models.DecimalField(
        'PIS', max_digits=15, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.nome


class AdmissaoFuncionario(models.Model):
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(
        'Departamento', on_delete=models.SET_NULL, null=True, blank=True)
    filial = models.ForeignKey(
        'Filial', on_delete=models.SET_NULL, null=True, blank=True)
    centraodecusto = models.ForeignKey(
        CentroDeCusto, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField('Status Ativo/Inativo', default=False)
    matricula = models.DecimalField(
        'Matricula', max_digits=15, decimal_places=0, null=True, blank=True)
    regradeponto = models.ForeignKey(
        RegraDePonto, on_delete=models.SET_NULL, null=True, blank=True)
    data_admissao = models.DateField()
    data_demissao = models.DateField()

    def __str__(self):
        return self.funcionario.nome


class Ponto(models.Model):
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField(default=timezone.now)
    competencia = models.ForeignKey(
        Competencia, on_delete=models.SET_NULL, null=True, blank=True,)
    entrada = models.TimeField(blank=True, null=True)
    entrada_almoco = models.TimeField(blank=True, null=True)
    saida_almoco = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.funcionario} - {self.data}"
