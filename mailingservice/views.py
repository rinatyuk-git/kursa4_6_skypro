from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailingservice.models import Client, Message, Mailing, Attempt
from mailingservice.services import send_mailing


def home(request):
    context = {'mailings_count': Mailing.objects.all().count(),  # количество рассылок всего,
               'active_mailings_count': Mailing.objects.filter(is_active=True).count(),  # количество активных рассылок,
               'client_count': Client.objects.all().count(),  # количество уникальных клиентов для рассылок,

               }
    return render(request, "mailingservice/home.html", context=context)


def mailing_stats(request, pk):
    attempts = Attempt.objects.filter(mailing_id=pk)
    context = {'attempts': attempts}
    return render(request, 'mailingservice/mailing_stats.html', context)


# class AtttemptListView(ListView):
#     model = Attempt
#
#     def get_queryset(self):

def mailing_run(request, pk):
    obj = get_object_or_404(Mailing, pk=pk)
    send_mailing(obj)
    messages.success(request, 'Рассылка отправлена успешно!')
    return redirect('mailingservice:mailing_detail', pk=pk)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(owner=user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('client_name', 'client_email', 'client_info')
    success_url = reverse_lazy('mailingservice:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('client_name', 'client_email', 'client_info')
    success_url = reverse_lazy('mailingservice:client_list')

    def get_success_url(self):
        return reverse("mailingservice:client_detail", args=[self.kwargs.get("pk")])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailingservice:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Message.objects.all()
        else:
            return Message.objects.filter(owner=user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('message_name', 'message_body')
    success_url = reverse_lazy('mailingservice:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('message_name', 'message_body')
    success_url = reverse_lazy('mailingservice:message_list')

    def get_success_url(self):
        return reverse("mailingservice:message_detail", args=[self.kwargs.get("pk")])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailingservice:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(owner=user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailingservice:mailing_list')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailingservice:mailing_list')

    def get_success_url(self):
        return reverse("mailingservice:mailing_detail", args=[self.kwargs.get("pk")])


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailingservice:mailing_list')
