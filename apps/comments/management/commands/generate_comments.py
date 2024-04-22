from django.core.management import BaseCommand
from apps.comments.models import Comment
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        comment = [Comment(product_id=j.pk,
                           name=f'diyoroviskandar{i}',
                           email=f'diyoroviskandar{i}@gmail.com',
                           rating=f'{1}',
                           message=f'message{i}')
                   for i in range(1, 6)
                   for j in Product.objects.all()]
        Comment.objects.bulk_create(comment)
        self.stdout.write(self.style.SUCCESS('5000 contacts created'))
