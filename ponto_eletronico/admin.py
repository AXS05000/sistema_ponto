from django.contrib import admin

from .models import Competencia, Departamento, Funcionario, Ponto


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'departamento', 'usuario')


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo_comp', 'mes', 'ano', 'data_inicio', 'data_fim')


class PontoAdmin(admin.ModelAdmin):
    listdisplay = ('funcionario', 'data', 'competencia',
                   'entrada', 'entrada_almoco', 'saida_almoco', 'saida')


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Ponto, PontoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
