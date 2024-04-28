from django.core.management import BaseCommand
from apps.contacts.models import Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        contacts = [Contact(name=f'name{i}',
                            email=f'email{i}@gmail.com',
                            message=f'message{i}',
                            title=f'title{i}')
                    for i in range(1, 101)]
        Contact.objects.bulk_create(contacts)
        self.stdout.write(self.style.SUCCESS('100 contacts created'))
