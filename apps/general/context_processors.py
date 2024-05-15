from apps.carts.models import UserCart
from apps.general.models import General, PaymentMethod
from apps.wishlists.models import Wishlist


def general(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user.pk).values_list('product_id', flat=True)
    generals = General.objects.all()
    user_cart_count = UserCart.objects.all().count()
    payment_methods_logo = PaymentMethod.objects.all()


    context = {
        'generals': generals,
        'wishlists': wishlists,
        'user_cart_count': user_cart_count,
        'payment_methods_logo': payment_methods_logo,
    }

    return context

