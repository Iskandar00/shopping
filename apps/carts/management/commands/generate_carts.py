from django.core.management import BaseCommand

from apps.carts.models import UserCart


class Command(BaseCommand):
    def handle(self, *args, **options):
        carts = [
            UserCart(
                user_id=f'{i}',
                product_feature_id=f'{i}',
                counts=f'{i}',
            )
            for i in range(1, 11)
        ]
        UserCart.objects.bulk_create(carts)
        self.stdout.write(self.style.SUCCESS('10 carts create!!!'))
