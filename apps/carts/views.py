from django.contrib import messages
from django.db.models import Sum, F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.carts.models import UserCart
from apps.features.models import ProductFeature
from apps.general.models import Coupon, General, PaymentMethod


def carts_add(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('login-page')

    counts = request.POST.get('counts', 1)
    features = [
        int(request.POST[feature])
        for feature in request.POST if feature.startswith('feature_')]

    product_feature = ProductFeature.objects.filter(product_id=pk, feature_value__id__in=features).first()
    if product_feature:
        UserCart.objects.create(product_feature_id=product_feature.pk, user_id=user.pk, counts=counts)
    return redirect(request.META['HTTP_REFERER'])


def carts_page(request):
    user = request.user
    user_carts = UserCart.objects.filter(user=user)
    subtotal = UserCart.objects.filter(user=user).aggregate(s=Sum(F('product_feature__price') * F('counts'), default=0))['s']

    shipping = General.objects.all().values('shipping').first()['shipping']

    context = {
        'user_carts': user_carts,
        'subtotal': subtotal,
        'shipping': shipping
    }
    coupon_code = request.POST.get('coupon_code')

    if coupon_code:
        coupon = Coupon.check_coupon(coupon_code)
        if coupon:
            context['coupon'] = coupon
            messages.success(request, 'Your coupon is activated.')
        else:
            messages.error(request, 'Coupon code is not valid.')
    return render(request, 'cart.html', context)


@login_required
def delete_cart(request, pk):
    obj = UserCart.objects.filter(pk=pk).last()
    obj.delete()
    return redirect('carts-page')


@login_required
def update_cart(request, pk):
    user = request.user
    if not user:
        return redirect('login-page')
    user_cart = UserCart.objects.filter(pk=pk)
    count = request.POST.get('count')
    quantity = user_cart.last().product_feature.quantity
    if quantity < int(count):
        user_cart.update(counts=quantity)
        messages.error(request, f'{quantity}-limit')
    else:
        user_cart.update(counts=count)

    return redirect('carts-page')


def checkout_page(request):
    user = request.user
    user_carts = UserCart.objects.filter(user=user)
    subtotal = UserCart.objects.filter(user=user).aggregate(s=Sum(F('product_feature__price') * F('counts'), default=0))['s']
    shipping = General.objects.all().values('shipping').first()['shipping']
    payment_methods = PaymentMethod.objects.all()

    context = {
        'user_carts': user_carts,
        'subtotal': subtotal,
        'shipping': shipping,
        'payment_methods': payment_methods
    }
    return render(request, 'checkout.html', context)
