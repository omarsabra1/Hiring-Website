# Generated by Django 4.0.6 on 2022-08-21 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_city_profile_profile_image_profile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image',
        ),
    ]
