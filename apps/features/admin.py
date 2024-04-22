from django.contrib import admin

from apps.features.models import Feature, FeatureValue, ProductFeature


class FeatureValueInline(admin.StackedInline):
    model = FeatureValue
    prepopulated_field = {'slug': ['name_uz']}


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'sub_category', 'name_uz', 'slug', 'name_ru',)
    prepopulated_field = {'slug': ['name_uz,']}
    inlines = [FeatureValueInline]


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    list_display = ('feature', 'value_uz', 'slug', 'value_ru',)
    list_filter = ['feature']
    search_fields = ['value_uz', 'value_ru']
    prepopulated_field = {'slug': ['value_uz']}


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'old_price', 'quantity',)
