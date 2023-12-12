from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from clients.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'middle_name', 'last_name', 'email', 'message',)
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'middle_name', 'last_name', 'email', 'message',)
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.save()

        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')
