from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue, ProductFeature


class Command(BaseCommand):
    def handle(self, *args, **options):
        features = [Feature(main_category_id=i if i % 2 else None,
                            sub_category_id=i if not (i % 2) else None,
                            name_uz=f'name_uz      name_uz{i}',
                            slug=f'slug-{i}',
                            name_ru=f'name_ru            name_ru{i}', )
                    for i in range(1, 21)
                    ]
        print(list(map(lambda el: el.slug, features)))
        # Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS('20 features created'))
        #
        # feature_value = [
        #     FeatureValue(feature_id=j.pk,
        #                  value_uz=f'name_uz                No{i}',
        #                  slug=f'slug-No{i}-{j}',
        #                  value_ru=f'name_ru               No{i}', )
        #     for i in range(1, 4)
        #     for j in Feature.objects.all()
        # ]
        # FeatureValue.objects.bulk_create(feature_value)
        # self.stdout.write(self.style.SUCCESS('60 feature_value created'))

        # product_feature = [
        #     ProductFeature(
        #         product_id=i,
        #         feature_value_id=i,
        #         price=i,
        #         quantity=i,
        #     )
        #     for i in range(1, 1001)
        #
        # ]
        # ProductFeature.objects.bulk_create(product_feature)
        # self.stdout.write(self.style.SUCCESS('1000 product_feature created'))
