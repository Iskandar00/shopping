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
        self.stdout.write(self.style.SUCCESS('1000 contacts created'))

        services = [
            Service(title_uz=f'title_uz{i}', slug=f'slug{i}', title_ru=f'title-ru{i}')
            for i in range(1, 7)
        ]
        Service.objects.bulk_create(services)
        self.stdout.write(self.style.SUCCESS('6 contacts created'))

        # banner = [
        #     Banner(sub_category_id=i,
        #            title_uz=f'title_uz{i}',
        #            slug=f'slug{i}',
        #            title_ru=f'title-ru{i}',
        #            desc_uz=f'desc_uz{i}',
        #            desc_ru=f'desc_ru{i}', )
        #     for i in range(1, 7)
        # ]
        # Banner.objects.bulk_create(banner)
        # self.stdout.write(self.style.SUCCESS('6 contacts created'))

        payment_method = [
            PaymentMethod(name=f'name           No{i}',
                          slug=f'slug            No{i}', )
            for i in range(1, 11)
        ]
        PaymentMethod.objects.bulk_create(payment_method)
        self.stdout.write(self.style.SUCCESS('10 payment_method create'))

        coupon = [
            Coupon(title_uz=f'title_uz         No{i}',
                   slug=f'slug-{i}',
                   title_ru=f'title_ru         No{i}',
                   amount=f'{i+1.0}',
                   code=f'ABcd{i}', )
            for i in range(1, 1001)
        ]
        Coupon.objects.bulk_create(coupon)
        self.stdout.write(self.style.SUCCESS('1000 payment_method create'))

        social_link = [
            SocialLink(name=f'name          No{i}',
                       slug=f'slug-No{i}',
                       link=f'https://www.google.com/{i}', )
            for i in range(1, 1001)
        ]
        SocialLink.objects.bulk_create(social_link)
        self.stdout.write(self.style.SUCCESS('1000 payment_method create'))
