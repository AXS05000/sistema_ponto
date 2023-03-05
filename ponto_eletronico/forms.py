from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Funcionario, Ponto


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'departamento', 'usuario')


class PontoForm(forms.ModelForm):
    class Meta:
        model = Ponto
        fields = ('data', 'competencia', 'entrada',
                  'entrada_almoco', 'saida_almoco', 'saida')
        widgets = {
            'data': SelectDateWidget,
        }
