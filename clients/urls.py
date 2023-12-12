from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientListView, ClientDeleteView, ClientCreateView, ClientUpdateView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clients_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete')
]