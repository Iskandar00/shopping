from django.contrib import admin
from apps.general.models import General, Service, Banner, SocialLink,  PaymentMethod, Coupon


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'phone_number', 'email', 'address', 'desc')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'slug', 'title_ru', 'icon',)
    prepopulated_field = {'slug': ['title_uz,']}


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'slug', 'title_ru', 'code', 'from_date', 'to_date', 'amount', 'amount_is_percent',)
    prepopulated_field = {'slug': ['title_uz,']}


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'slug', 'link',)
    prepopulated_field = {'slug': ['name,']}


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'logo',)
    prepopulated_field = {'slug': ['name,']}


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('SubCategory', 'title_uz', 'slug', 'title_ru', 'desc_uz', 'desc_ru',)
    prepopulated_field = {'slug': ['title_uz,']}

