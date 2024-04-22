from django.core.management import BaseCommand
from apps.contacts.models import Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = [Contact(name=f'name{i}',
                         email=f'email{i}@gmail.com',
                         message=f'message{i}',
                         title=f'title{i}')
                 for i in range(1000)]
        Contact.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('1000 comments created'))
