# Generated by Django 3.1 on 2020-09-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_transaction_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_confirmation',
            name='bought_book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
