from django.contrib import admin
from clients.models.client import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=(
        'company_name',
        'gst_number',
        'email'
    )
    search_fields=(
        'company_name',
        'gst_number'
    )


