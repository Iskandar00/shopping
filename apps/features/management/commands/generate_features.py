from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        features = [Feature(main_category_id=cat_id if cat_id % 2 else None,
                            sub_category_id=cat_id if not (cat_id % 2) else None,
                            name_uz=f'name_uz      name_uz{i}.{cat_id}',
                            slug=f'slug-{i}-{cat_id}',
                            name_ru=f'name_ru            name_ru{i}.{cat_id}', )
                    for i in range(1, 3)
                    for cat_id in range(1, 10)
                    ]
        Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS('20 features created'))

        feature_value = [
            FeatureValue(feature_id=j.pk,
                         value_uz=f'name_uz                No{i}.{j}',
                         slug=f'slug-No{i}-{j.pk}',
                         value_ru=f'name_ru               No{i}.{j}', )
            for i in range(1, 4)
            for j in Feature.objects.all()
        ]
        FeatureValue.objects.bulk_create(feature_value)
        self.stdout.write(self.style.SUCCESS('60 feature_value created'))
