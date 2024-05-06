from django.contrib import admin

from apps.wishlists.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at',)
    list_select_related = ()
