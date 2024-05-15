from django.urls import path

from apps.carts.views import carts_add, carts_page, delete_cart, update_cart, checkout_page

urlpatterns = [
    path('add/<int:pk>/', carts_add, name='carts_add-page'),
    path('', carts_page, name='carts-page'),
    path('delete-cart/<int:pk>/', delete_cart, name='delete_cart-page'),
    path('update-cart/<int:pk>/', update_cart, name='update_cart-page'),
    path('checkout-page/', checkout_page, name='checkout-page'),
]
