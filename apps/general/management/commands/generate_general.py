from django.core.management import BaseCommand
from apps.general.models import General, Service, Banner, SocialLink, PaymentMethod, Coupon


class Command(BaseCommand):
    def handle(self, *args, **options):
        general = [
            General(name=f'name{1}',
                    phone_number=f'+{998901234567}',
                    email=f'diyoroviskandar@gmail.com',
                    address=f'address',
                    desc=f'desc', )
        ]
        General.objects.bulk_create(general)
        self.stdout.write(self.style.SUCCESS('general created'))

        services = [
            Service(title_uz=f'title_uz{i}', slug=f'slug{i}', title_ru=f'title-ru{i}')
            for i in range(1, 7)
        ]
        Service.objects.bulk_create(services)
        self.stdout.write(self.style.SUCCESS('6 services created'))

        banners = [
            Banner(sub_category_id=i,
                   title_uz=f'title_uz{i}',
                   slug=f'slug{i}',
                   title_ru=f'title-ru{i}',
                   desc_uz=f'desc_uz{i}',
                   desc_ru=f'desc_ru{i}', )
            for i in range(1, 6)
        ]
        Banner.objects.bulk_create(banners)
        self.stdout.write(self.style.SUCCESS('5 banners created'))

        payment_methods = [
            PaymentMethod(name=f'name           No{i}',
                          slug=f'slug            No{i}', )
            for i in range(1, 6)
        ]
        PaymentMethod.objects.bulk_create(payment_methods)
        self.stdout.write(self.style.SUCCESS('5 payment_methods create'))

        coupon = [
            Coupon(title_uz=f'title_uz         No{i}',
                   slug=f'slug-{i}',
                   title_ru=f'title_ru         No{i}',
                   amount=f'{i+1.0}',
                   code=f'ABcd{i}', )
            for i in range(1, 101)
        ]
        Coupon.objects.bulk_create(coupon)
        self.stdout.write(self.style.SUCCESS('100 payment_method create'))

        social_links = [
            SocialLink(name=f'name          No{i}',
                       slug=f'slug-No{i}',
                       link=f'https://www.google.com/{i}', )
            for i in range(1, 5)
        ]
        SocialLink.objects.bulk_create(social_links)
        self.stdout.write(self.style.SUCCESS('4 social_links create'))
