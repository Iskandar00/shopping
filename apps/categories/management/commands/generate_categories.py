from django.core.management import BaseCommand
from apps.categories.models import MainCategory, SubCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        main_cats = [
            MainCategory(name_uz=f'name_uz{i}',
                         slug=f'slag-slag{i}',
                         name_ru=f'name_ru{i}', )
            for i in range(1, 11)
        ]
        MainCategory.objects.bulk_create(main_cats)
        self.stdout.write(self.style.SUCCESS('10 main_cats created'))

        sub_cats = [
            SubCategory(main_category_id=i.pk,
                        name_uz=f'name_uz{i.pk}.{j}',
                        slug=f'slag-slag{i.pk}.{j}',
                        name_ru=f'name_ru{i.pk}.{j}', )
            for j in range(1, 5)
            for i in MainCategory.objects.all()
        ]
        SubCategory.objects.bulk_create(sub_cats)
        self.stdout.write(self.style.SUCCESS('40 sub_cats created'))
