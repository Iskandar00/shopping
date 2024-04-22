from django.db import models

from apps.users.models import CustomUser
from apps.features.models import ProductFeature


class Wishlist(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_feature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.product}'
