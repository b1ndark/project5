# Generated by Django 3.2.23 on 2024-02-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20240216_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_images/default_profile.png', null=True, upload_to='profiles/'),
        ),
    ]
