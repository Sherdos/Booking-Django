# Generated by Django 4.1.1 on 2022-09-29 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_hotel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='slug',
            new_name='city',
        ),
    ]