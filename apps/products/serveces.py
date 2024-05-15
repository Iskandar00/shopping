from django.db.models import Avg, Count

from apps.comments.models import Comment
from apps.products.models import Product


def product_rating_avg(product_id):
    rating = Comment.objects.filter(product_id=product_id).aggregate(a=Avg('rating', default=0))['a']
    Product.objects.filter(pk=product_id).update(rating=rating)
