from django.test import TestCase

from apps.products.models import Product

for a in Product.objects.all():
    print(a.pk)
