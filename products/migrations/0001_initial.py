# Generated by Django 3.2.23 on 2024-01-25 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('friendly_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='products/no_product_image.webp', null=True, upload_to='products/')),
                ('description', models.TextField()),
                ('brand', models.CharField(blank=True, choices=[('select', 'Brand'), ('acer', 'Acer'), ('apple', 'Apple'), ('asus', 'Asus'), ('google', 'Google'), ('toshiba', 'Toshiba'), ('sony', 'Sony')], default='', max_length=30, null=True)),
                ('operating_system', models.CharField(blank=True, choices=[('select', 'Operating System'), ('android', 'Android'), ('ios', 'iOS'), ('linux', 'Linux'), ('windows', 'Windows'), ('macos', 'macOS')], default='', max_length=30, null=True)),
                ('sku', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
