from django.contrib import admin
from django.contrib.auth.models import Group

from apps.users.models import CustomUser, UserAuthCode


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'address1', 'address2',
                    'country', 'region', 'district', 'zip_code')

    readonly_fields = ('last_login', 'date_joined', 'email',)

    fields = ('password', 'last_login', 'is_active', 'date_joined', 'email', 'first_name', 'last_name', 'phone_number',
              'address1', 'address2',
              'country', 'region', 'district', 'zip_code')

    def save_formset(self, request, obj, form, change):
        if obj.pk and CustomUser.objects.get('pk=obj.pk').password != obj.password:
            obj.set_password(obj.password)
        obj.save()


@admin.register(UserAuthCode)
class UserAuthCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'expire_at')

    def has_add_permission(self, request):
        return False
