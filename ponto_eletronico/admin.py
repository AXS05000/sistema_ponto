from django.contrib import admin

from .models import Competencia, Departamento, Funcionario, Ponto, RegraDePonto


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'departamento', 'usuario')


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo_comp', 'mes', 'ano', 'data_inicio', 'data_fim')


@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    listdisplay = ('funcionario', 'data', 'competencia',
                   'entrada', 'entrada_almoco', 'saida_almoco', 'saida')


@admin.register(RegraDePonto)
class RegraDePontoAdmin(admin.ModelAdmin):
    listdisplay = ('nome', 'toleranciaentrada', 'toleranciasaida',
                   'horaextraautorizada', 'periodohoranoturnainicio', 'periodohoranoturna_fim')


admin.site.register(Departamento, DepartamentoAdmin)
