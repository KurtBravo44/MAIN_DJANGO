from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'middle_name',
                    'email',
                    'message',)
    list_filter = ('first_name',)
    search_fields = ('first_name', 'last_name')
