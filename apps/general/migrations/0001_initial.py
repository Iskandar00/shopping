# Generated by Django 5.0.4 on 2024-04-22 09:59

import apps.users.valedate
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('title_ru', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, help_text="So'mda yoki foizda kiriting!!!", max_digits=10)),
                ('amount_is_percent', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='general/logo')),
                ('phone_number', models.CharField(max_length=13, validators=[apps.users.valedate.validate_phone_number])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField(max_length=35, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='general/payment_method/logo/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('title_ru', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(upload_to='general/service/image/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='general/social_link/icon/')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('title_ru', models.CharField(blank=True, max_length=50)),
                ('desc_uz', models.CharField(max_length=50)),
                ('desc_ru', models.CharField(blank=True, max_length=50)),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory')),
            ],
        ),
    ]
