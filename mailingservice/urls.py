from django.urls import path

from mailingservice.apps import MailingserviceConfig
from mailingservice.views import home, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, \
    ClientDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView, mailing_stats

app_name = MailingserviceConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/client_detail/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/client_edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/client_delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('<int:pk>/message_detail/', MessageDetailView.as_view(), name='message_detail'),
    path('<int:pk>/message_edit/', MessageUpdateView.as_view(), name='message_edit'),
    path('<int:pk>/message_delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('<int:pk>/mailing_detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/mailing_edit/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('<int:pk>/mailing_delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('<int:pk>/mailing_stats/', mailing_stats, name='mailing_stats'),
]
