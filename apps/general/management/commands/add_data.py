import os

from django.core.management import BaseCommand
from apps.general.models import General, Service, Banner, SocialLink, PaymentMethod, Coupon


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('makemigrations')
        os.system('python manage.py makemigrations')
        print('migrate')
        os.system('python manage.py migrate')
        print('createsuperuser')
        # os.system('python manage.py createsuperuser')
        print('generate_users')
        os.system('python manage.py generate_users')
        print('generate_categories')
        os.system('python manage.py generate_categories')
        print('generate_contacts')
        os.system('python manage.py generate_contacts')
        print('generate_general')
        os.system('python manage.py generate_general')
        print('generate_comments')
        os.system('python manage.py generate_comments')
        print('generate_features')
        os.system('python manage.py generate_features')
        print('generate_carts')
        os.system('python manage.py generate_carts')
