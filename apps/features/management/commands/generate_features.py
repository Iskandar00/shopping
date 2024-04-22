from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue, ProductFeature


class Command(BaseCommand):
    def handle(self, *args, **options):
        feature = [
            Feature(sub_category_id=i,
                    name_uz=f'name_uz      name_uz{i}',
                    slug=f'slug-{i}',
                    name_ru=f'name_ru            name_ru{i}', )
            for i in range(1, 1001)
        ]
        Feature.objects.bulk_create(feature)
        self.stdout.write(self.style.SUCCESS('1000 main_cat created'))

        feature_value = [
            FeatureValue(feature_id=j.pk,
                         value_uz=f'name_uz                No{i}',
                         slug=f'slug-No{i}-{j}',
                         value_ru=f'name_ru               No{i}', )
            for i in range(1, 4)
            for j in Feature.objects.all()
        ]
        Feature.objects.bulk_create(feature_value)
        self.stdout.write(self.style.SUCCESS('3000 main_cat created'))

        product_feature = [
            ProductFeature(
                product_id=f'{i}',
                feature_value_id=f'{i}',
                price=f'{i}',
                old_price=f'{i}',
                quantity=f'{i}',
            )
            for i in range(1, 1001)

        ]
        ProductFeature.objects.bulk_create(product_feature)
        self.stdout.write(self.style.SUCCESS('1000 main_cat created'))
