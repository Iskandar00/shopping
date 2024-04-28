from django.contrib import admin

from apps.features.models import Feature, FeatureValue, ProductFeature


class FeatureValueInline(admin.StackedInline):
    model = FeatureValue
    prepopulated_field = {'slug': ['name_uz']}
    min_num = 2


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'sub_category', 'name_uz', 'slug', 'name_ru',)
    prepopulated_fields = {'slug': ['name_uz']}
    list_filter = ('main_category', 'sub_category',)
    inlines = [FeatureValueInline]
    list_display_links = list_display

