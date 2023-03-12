from django.contrib import admin

from .models import Client, ClientAddress

admin.site.register(Client)
admin.site.register(ClientAddress)

