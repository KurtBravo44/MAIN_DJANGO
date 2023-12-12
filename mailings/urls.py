from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

]