# Generated by Django 5.0.4 on 2024-05-05 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner_image/%Y/%m/%d')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.banner')),
            ],
        ),
    ]
