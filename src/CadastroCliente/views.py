from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cliente


class ClienteList(ListView):
    model = Cliente


class ClienteCreate(CreateView):
    model = Cliente
    # template_name_suffix = '_form'
    fields = ['nome', 'email', 'endereco', 'telefone', 'observacoes']
    success_url = reverse_lazy('cliente_list')


class ClienteUpdate(UpdateView):
    model = Cliente
    # template_name_suffix = '_form'
    fields = ['nome', 'email', 'endereco', 'telefone', 'observacoes']
    success_url = reverse_lazy('cliente_list')


class ClienteDelete(DeleteView):
    model = Cliente
    # template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('cliente_list')


class ClienteDetail(DetailView):
    model = Cliente