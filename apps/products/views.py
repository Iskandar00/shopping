from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from apps.products.models import Product
from apps.features.models import Feature


def product_list(request):
    products = Product.objects.all().order_by('-id')

    """ start search_filters """

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

    """ end search_filters """

    """ start category_filters """

    main_cat_id, sub_cat_id = request.GET.get('main_cat_id', ''), request.GET.get('sub_cat_id', '')

    if main_cat_id.isdigit():
        products = Product.objects.filter(main_category_id=main_cat_id)
        features = Feature.objects.filter(main_category_id=main_cat_id)
    else:
        features = Feature.objects.all().order_by('-id')[:3]

    if sub_cat_id.isdigit():
        products = Product.objects.filter(sub_category_id=sub_cat_id)
        features = Feature.objects.filter(sub_category_id=sub_cat_id)

    """ end category_filters """
    feat_values = request.GET.getlist('feature_values')
    if feat_values:
        products = products.filter(product_features__feature_value__id__in=feat_values).distinct()

    """ start paginator """

    page = request.GET.get('page', '1')
    paginator = Paginator(products, 9)
    paginator_obj = paginator.get_page(page)

    """ end paginator """

    context = {
        'page_objects': paginator_obj,
        'paginator': paginator,
        'features': features,
        'feat_values': list(map(int, feat_values))
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    products = Product.objects.all().order_by('?')
    products_details = Product.objects.filter(pk=pk)

    context = {
        'products_details': products_details,
        'products': products
    }
    return render(request, 'products/product_detail.html', context)
