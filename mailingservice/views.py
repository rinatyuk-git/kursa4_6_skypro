from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailingservice.models import Client, Message, Mailing, Attempt
from mailingservice.services import send_mailing


def home(request):
    return render(request, "mailingservice/home.html")


def mailing_stats(request, pk):
    attempts = Attempt.objects.filter(mailing_id=pk)
    context = {'attempts': attempts}
    return render(request, 'mailingservice/mailing_stats.html', context)


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('client_name', 'client_email', 'client_info')
    success_url = reverse_lazy('mailingservice:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('client_name', 'client_email', 'client_info')
    success_url = reverse_lazy('mailingservice:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailingservice:client_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('message_name', 'message_body')
    success_url = reverse_lazy('mailingservice:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('message_name', 'message_body')
    success_url = reverse_lazy('mailingservice:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailingservice:message_list')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailingservice:mailing_list')

    def form_valid(self, form):
        obj = form.save()
        send_mailing(obj)
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailingservice:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailingservice:mailing_list')
