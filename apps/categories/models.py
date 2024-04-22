from django.db import models
from apps.comments.serveces import normalize_text


class MainCategory(models.Model):

    name_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='category/image/%Y/%m/%d')

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):

    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.main_category}:{self.name_uz}'

    def get_normalize_fields(self):
        return [
            'name_uz',
            'name_ru',
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)