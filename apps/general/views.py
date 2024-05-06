from django.shortcuts import render

from apps.categories.models import MainCategory
from apps.products.models import Product
from apps.general.models import Service, SocialLink, Banner, PaymentMethod


def home(request):
    # main_cat = MainCategory.objects.filter()
    products = Product.objects.all().order_by('?')[0:8]
    recent_products = Product.objects.all().order_by('-pk')[0:8]
    services = Service.objects.all()
    social_links = SocialLink.objects.all()
    banners = Banner.objects.all()
    payment_methods = PaymentMethod.objects.all()

    context = {
        'products': products,
        'services': services,
        'social_links': social_links,
        'recent_products': recent_products,
        'banners': banners,
        'payment_methods': payment_methods,
    }

    return render(request, 'index.html', context)
