from django.core.management import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            Product(
                sub_category_id=cat_id if cat_id % 2 else None,
                main_category_id=cat_id if not (cat_id % 2) else None,
                title_uz=f'title_uz        No{cat_id}.{i}',
                slug=f'slug-{cat_id}-{i}',
                title_ru=f'title_ru        No{cat_id}-{i}',
                short_desc_uz=f'short_desc_uz             No{i}',
                short_desc_ru=f'short_desc_ru           No{i}',
                long_desc_uz=f'long_desc_uz          No{i}',
                long_desc_ru=f'long_desc_ru            No{i}',
            )
            for i in range(1, 4)
            for cat_id in range(1, 10)
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('30 main_cats created'))
