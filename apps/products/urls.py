from django.urls import path
from apps.products.views import product_list

urlpatterns = [
    path('', product_list, name='product_list-page'),
]
