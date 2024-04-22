from django.contrib import admin

from apps.products.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'main_category', 'sub_category', 'title_uz', 'slug', 'title_ru', 'created_at')
    prepopulated_field = {'slug': ['title_uz,']}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product', 'ordering_number')
