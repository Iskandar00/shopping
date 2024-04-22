from django.contrib import admin

from apps.users.models import CustomUser, UserAuthCode


@admin.register(CustomUser)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'address1', 'address2',
                    'country', 'region', 'district', 'zip_code')
    prepopulated_field = {'slug': ['name_uz,']}


@admin.register(UserAuthCode)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'expire_at')
