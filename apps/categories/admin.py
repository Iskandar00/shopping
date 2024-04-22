from django.contrib import admin

from apps.categories.models import MainCategory, SubCategory


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    prepopulated_field = {'slug': ['name_uz']}


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'slug', 'name_ru', 'image',)
    prepopulated_field = {'slug': ['name_uz,']}
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'name_uz', 'slug', 'name_ru')
    list_filter = ['main_category']
    search_fields = ['name_uz', 'name_ru']
    prepopulated_field = {'slug': ['name_uz']}
