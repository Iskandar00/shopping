from django.contrib import admin

from apps.contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'title', 'message')
    list_display_links = list_display
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
