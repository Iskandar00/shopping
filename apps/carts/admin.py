from django.contrib import admin

from apps.carts.models import UserCart


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'counts', 'created_at')
    list_display_links = list_display

    def has_add_permission(self, request):
        return False
