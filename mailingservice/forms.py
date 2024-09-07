from django.forms import ModelForm

from mailingservice.models import Client, Message, Mailing
from users.forms import StyleFormMixin


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ("owner",)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ("owner",)


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        exclude = ("owner",)


class MailingModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ("is_active", "owner",)
