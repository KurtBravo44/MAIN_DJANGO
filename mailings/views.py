from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mailings.models import Mailing, LogMailing



class MailingListView(ListView):
    model = Mailing

class MailingCreateView(CreateView):
    model = Mailing
    fields = ('owner', 'message_title', 'message_body', 'start', 'stop', 'period',)
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('owner', 'message_title', 'message_body', 'start', 'stop', 'period',)
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.save()

        return super().form_valid(form)

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailings_list')


