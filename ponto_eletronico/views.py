
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FuncionarioForm, PontoForm
from .models import Funcionario, Ponto


class FuncionarioListView(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'ponto/funcionario_list.html'
    context_object_name = 'funcionarios'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(nome__icontains=query) |
                Q(cpf__icontains=query)
            ).distinct()
        else:
            object_list = self.model.objects.all()
        return object_list


class FuncionarioCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'ponto/funcionario_form.html'
    success_url = reverse_lazy('funcionariolist')


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'ponto/funcionario_form.html'
    success_url = reverse_lazy('funcionariolist')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Funcionario, pk=pk)


class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    template_name = 'ponto/funcionario_confirm_delete.html'
    success_url = reverse_lazy('funcionariolist')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Funcionario, pk=pk)


class PontoListView(LoginRequiredMixin, ListView):
    model = Ponto
    template_name = 'ponto/ponto_list.html'
    context_object_name = 'pontos'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(funcionario__nome__icontains=query) |
                Q(funcionario__departamento__icontains=query)
            ).distinct()
        else:
            object_list = self.model.objects.all()
        return object_list


class PontoCreateView(LoginRequiredMixin, CreateView):
    model = Ponto
    form_class = PontoForm
    template_name = 'ponto/ponto_form.html'
    success_url = reverse_lazy('pontolist')

    def form_valid(self, form):
        form.instance.funcionario = self.request.user.funcionario
        return super().form_valid(form)


class PontoUpdateView(LoginRequiredMixin, UpdateView):
    model = Ponto
    form_class = PontoForm
    template_name = 'ponto/ponto_form.html'
    success_url = reverse_lazy('pontolist')


class PontoDeleteView(LoginRequiredMixin, DeleteView):
    model = Ponto
    template_name = 'ponto/ponto_confirm_delete.html'
    success_url = reverse_lazy('pontolist')
