# Generated by Django 3.2.23 on 2024-03-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_alter_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
