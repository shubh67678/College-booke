# Generated by Django 3.1 on 2020-09-23 03:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='request',
            new_name='request_book',
        ),
    ]
