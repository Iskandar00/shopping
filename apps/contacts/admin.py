from django.contrib import admin

from apps.contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'title', 'message')

    readonly_fields = ('user', 'name', 'email', 'title', 'message')

