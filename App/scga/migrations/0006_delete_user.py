# Generated by Django 4.1.4 on 2022-12-20 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scga', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]