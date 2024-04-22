from django.core.management import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product = [
            Product(
                sub_category_id=i,
                title_uz=f'title_uz        No{i}',
                slug=f'slug-{i}',
                title_ru=f'title_ru        No{i}',
                short_desc_uz=f'short_desc_uz             No{i}',
                short_desc_ru=f'short_desc_ru           No{i}',
                long_desc_uz=f'long_desc_uz          No{i}',
                long_desc_ru=f'long_desc_ru            No{i}',
            )
            for i in range(1, 1001)
        ]
        Product.objects.bulk_create(product)
        self.stdout.write(self.style.SUCCESS('1000 main_cat created'))
