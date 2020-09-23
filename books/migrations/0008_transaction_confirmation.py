# Generated by Django 3.1 on 2020-09-23 07:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200923_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction_confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_done', models.BooleanField(default=False)),
                ('bought_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', unique=True)),
            ],
        ),
    ]
