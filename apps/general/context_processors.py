from apps.general.models import General
from apps.wishlists.models import Wishlist


def general(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user.pk).values_list('product_id', flat=True)
    generals = General.objects.all()

    context = {
        'generals': generals,
        'wishlists': wishlists
    }

    return context

