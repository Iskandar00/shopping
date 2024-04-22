from django.db import models

from apps.users.models import CustomUser


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=50)
    email = models.EmailField()

    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.email}: {self.message}'

    def get_normalize_fields(self):
        return [
            'name',
            'title',
            'message'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)