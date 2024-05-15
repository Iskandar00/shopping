from django.core.management import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            Product(
                sub_category_id=j if j % 2 else None,
                main_category_id=j if not (j % 2) else None,
                title_uz=f'title_uz No{j}.{i}',
                slug=f'slug-{j}-{i}',
                title_ru=f'title_ru No{j}-{i}',
                short_desc_uz=f'short_desc_uz No{i}',
                short_desc_ru=f'short_desc_ru No{i}',
                long_desc_uz=f'long_desc_uz No{i}',
                long_desc_ru=f'long_desc_ru No{i}',
            )
            for i in range(1, 4)
            for j in range(1, 10)
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('30 main_cats created'))
