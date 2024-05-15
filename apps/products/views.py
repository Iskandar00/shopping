from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Min

from apps.products.models import Product
from apps.features.models import Feature
from apps.products.serveces import product_rating_avg


def product_list(request):
    products = Product.objects.filter(product_features__isnull=False).order_by('-id').distinct()

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

    try:
        products_detail = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return redirect('product-list')

    price = products_detail.product_features.aggregate(Min('price'))['price__min']
    products_detail.price = price
    product_rating_avg(pk)

    features = Feature.objects.filter(feature_values__product_features__product_id=pk).distinct()

    products = Product.objects.filter(product_features__isnull=False).order_by('?').distinct()

    comments = products_detail.comments.all()

    """ start paginator """

    page = request.GET.get('page', '1')
    paginator = Paginator(comments, 5)
    product_comments = paginator.get_page(page)

    """ end paginator """

    context = {
        'products_detail': products_detail,
        'products': products,
        'features': products_detail.get_features(),
        'comments': product_comments,
    }
    return render(request, 'products/product_detail.html', context)
