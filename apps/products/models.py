from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import get_language

from apps.categories.models import MainCategory, SubCategory
from apps.comments.serveces import normalize_text


class Product(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT,
                                      blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT,
                                     blank=True, null=True)

    title_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title_ru = models.CharField(max_length=100, blank=True)
    short_desc_uz = models.CharField(max_length=250)
    short_desc_ru = models.CharField(max_length=250, blank=True)
    long_desc_uz = models.TextField(max_length=1500)
    long_desc_ru = models.TextField(max_length=1500, blank=True)
    review_counts = models.PositiveSmallIntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('MainCategory yoki SubCategorydan birini tanlang!!!')

    def get_title(self):
        return getattr(self, f'title_{get_language()}')

    def __str__(self):
        return self.title_uz

    def get_normalize_fields(self):
        return ['title_uz',
                'title_ru',
                'short_desc_uz',
                'short_desc_ru',
                'long_desc_uz',
                'long_desc_ru',
                ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    ordering_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('product', 'ordering_number')
