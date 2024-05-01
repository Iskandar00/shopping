from django.shortcuts import render

from apps.products.models import Product
from apps.features.models import ProductFeature


def product_list(request):
    products = Product.objects.all().order_by('?')[:9]
    product_feature = ProductFeature.objects.all().order_by('?')

    context = {
        'products': products,

        'product_feature': product_feature
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    products = Product.objects.all().order_by('?')[:5]
    products_details = Product.objects.filter(pk=pk)

    context = {
        'products_details': products_details,
        'products': products
    }
    return render(request, 'products/product_detail.html', context)
