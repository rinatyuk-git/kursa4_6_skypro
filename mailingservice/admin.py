from django.contrib import admin

from mailingservice.models import Client, Message, Mailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "client_name", "client_email",)
    list_filter = ("client_name",)
    search_fields = ("client_name", "client_email",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "message_name", "message_body",)
    list_filter = ("message_name",)
    search_fields = ("message_name", "message_body",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "mailing_name", "started_at", "finished_at", "periodic", "status",)
    list_filter = ("mailing_name", "clients", "started_at", "finished_at",)
    search_fields = ("mailing_name", "status", "periodic",)

