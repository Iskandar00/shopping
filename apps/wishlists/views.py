from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from apps.wishlists.models import Wishlist


def product_wishlists(request, pk):
    # print(request.user, request)
    redirect_url = request.META['HTTP_REFERER']
    user = request.user
    if not user.is_authenticated:
        return redirect('login-page')
    obj, created = Wishlist.objects.get_or_create(user_id=user.pk, product_id=pk)
    if not created:
        obj.delete()
    return redirect(redirect_url)


def wishlist(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login-page')
    wishlist_products = Wishlist.objects.order_by('-created_at').filter(user_id=user.pk)
    page = request.GET.get('page', '1')
    paginator = Paginator(wishlist_products, 9)
    paginator_obj = paginator.get_page(page)

    context = {
        'page_objects': paginator_obj
    }

    return render(request, 'wishlist/wishlist.html', context)
