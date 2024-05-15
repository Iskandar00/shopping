from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.users.models import CustomUser
from apps.products.models import Product
from apps.comments.serveces import normalize_text


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)

    message = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.message}'

    def get_normalize_fields(self):
        return [
            'name',
            'message'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
