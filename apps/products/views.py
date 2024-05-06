from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from apps.products.models import Product


def product_list(request):
    products = Product.objects.all().order_by('-id')

    quare = request.GET.get('quare', '')
    if quare == '':
        request.session.quare = ''

    if quare:
        products = products.filter(Q(title_uz__icontains=quare) |
                                   Q(title_ru__icontains=quare) |
                                   Q(short_desc_uz__icontains=quare) |
                                   Q(short_desc_ru__icontains=quare) |
                                   Q(long_desc_ru__icontains=quare) |
                                   Q(long_desc_ru__icontains=quare))
    request.session['quare'] = quare
    page = request.GET.get('page', '1')
    paginator = Paginator(products, 9)
    paginator_obj = paginator.get_page(page)

    context = {
        'page_objects': paginator_obj,
        'paginator': paginator,
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
