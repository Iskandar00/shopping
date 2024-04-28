from django.core.management import BaseCommand
from apps.comments.models import Comment
from apps.products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        comments = [Comment(product_id=j.pk,
                            name=f'diyoroviskandar{i}',
                            email=f'diyoroviskandar{i}@gmail.com',
                            rating=f'{5}',
                            message=f'message{i}')
                    for i in range(1, 6)
                    for j in Product.objects.all()]
        Comment.objects.bulk_create(comments)
        self.stdout.write(self.style.SUCCESS('150 comments created'))
