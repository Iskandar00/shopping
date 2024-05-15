from django.core.management import BaseCommand
from apps.features.models import Feature, FeatureValue


class Command(BaseCommand):
    def handle(self, *args, **options):
        features = [Feature(main_category_id=j if j % 2 else None,
                            sub_category_id=j if not (j % 2) else None,
                            name_uz=f'name_uz{i}.{j}',
                            slug=f'slug-{i}-{j}',
                            name_ru=f'name_ru{i}.{j}', )
                    for i in range(1, 3)
                    for j in range(1, 10)
                    ]
        Feature.objects.bulk_create(features)
        self.stdout.write(self.style.SUCCESS('20 features created'))

        feature_value = [
            FeatureValue(feature_id=j.pk,
                         value_uz=f'name_uz No{i}.{j.pk}',
                         slug=f'slug-No{i}-{j.pk}',
                         value_ru=f'name_ru No{i}.{j.pk}', )
            for i in range(1, 4)
            for j in Feature.objects.all()
        ]
        FeatureValue.objects.bulk_create(feature_value)
        self.stdout.write(self.style.SUCCESS('60 feature_value created'))
