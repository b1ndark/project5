# Generated by Django 3.2.23 on 2024-02-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240125_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default_images/no_product_image.webp', null=True, upload_to='products/'),
        ),
    ]
