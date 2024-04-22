from django.contrib import admin

from apps.orders.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'coupon_code', 'coupon_price',
                    'first_name', 'last_name', 'email', 'phone_number',)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_feature', 'counts',)
