from django.contrib import admin

from apps.features.models import ProductFeature
from apps.products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    min_num = 1
    max_num = 10


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'sub_category', 'title_uz', 'slug', 'title_ru', 'created_at')
    prepopulated_fields = {'slug': ['title_uz']}
    readonly_fields = ('review_counts', 'rating', 'created_at')
    inlines = [ProductImageInline, ProductFeatureInline]
    list_select_related = ('main_category', 'sub_category', 'sub_category__main_category',)

