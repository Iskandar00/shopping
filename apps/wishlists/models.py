from django.db import models

from apps.users.models import CustomUser
from apps.products.models import Product


class Wishlist(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user}: {self.product}'
