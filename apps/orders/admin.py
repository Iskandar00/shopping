from django.contrib import admin

from apps.orders.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'coupon_code', 'coupon_price',
                    'first_name', 'last_name', 'email', 'phone_number',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_feature', 'counts',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
