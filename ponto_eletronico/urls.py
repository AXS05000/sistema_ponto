from django.urls import path

from .views import (FuncionarioCreateView, FuncionarioDeleteView,
                    FuncionarioListView, FuncionarioUpdateView,
                    PontoCreateView, PontoDeleteView, PontoListView,
                    PontoUpdateView)

urlpatterns = [
    path('funcionarios/', FuncionarioListView.as_view(), name='funcionariolist'),
    path('funcionarios/novo/', FuncionarioCreateView.as_view(),
         name='funcionariocreate'),
    path('funcionarios/editar/<int:pk>/', FuncionarioUpdateView.as_view(),
         name='funcionarioupdate'),
    path('funcionarios/excluir/<int:pk>/', FuncionarioDeleteView.as_view(),
         name='funcionariodelete'),
    path('ponto/', PontoListView.as_view(), name='pontolist'),
    path('ponto/novo/', PontoCreateView.as_view(), name='pontocreate'),
    path('ponto/editar/<int:pk>/', PontoUpdateView.as_view(), name='pontoupdate'),
    path('ponto/excluir/<int:pk>/', PontoDeleteView.as_view(), name='pontodelete'),
]
