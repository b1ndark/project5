# Generated by Django 3.2.23 on 2024-03-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20240223_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fav_brand',
            field=models.CharField(blank=True, choices=[('acer', 'Acer'), ('apple', 'Apple'), ('asus', 'Asus'), ('dell', 'Dell'), ('google', 'Google'), ('hp', 'HP'), ('msi', 'MSI'), ('toshiba', 'Toshiba'), ('sony', 'Sony'), ('samsung', 'Samsung'), ('hisense', 'Hisense')], default='', max_length=30, null=True, verbose_name='Favourite Brand'),
        ),
    ]