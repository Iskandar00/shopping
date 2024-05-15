from django.db import models
from django.core.exceptions import ValidationError

from apps.categories.models import MainCategory, SubCategory
from apps.comments.serveces import normalize_text
from apps.features.models import FeatureValue
from apps.general.services import get_field_by_language


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

    def get_features(self):
        features = {}
        features_values = FeatureValue.objects.filter(product_features__product_id=self.pk).distinct().select_related('feature')
        for features_value in features_values:
            feature = features_value.feature
            feature_id = feature.pk
            feature_name = feature.name
            value = {'id': features_value.pk, 'name': features_value.value}

            if feature_id not in features:
                features[feature_id] = {'name': feature_name, 'values': [value]}
            else:
                features[feature_id]['values'].append(value)
        return features

    def get_first_image(self):
        return self.productimage_set.first()

    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('MainCategory yoki SubCategorydan birini tanlang!!!')

    @property
    def title(self):
        return get_field_by_language(self, 'title')

    @property
    def short_desc(self):
        return get_field_by_language(self, 'title')

    @property
    def long_desc(self):
        return get_field_by_language(self, 'title')

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
        if self.sub_category:
            self.main_category = self.sub_category.main_category

        normalize_text(self)

        super().save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordering_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('product', 'ordering_number')
