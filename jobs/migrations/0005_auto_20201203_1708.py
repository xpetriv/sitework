# Generated by Django 3.1 on 2020-12-03 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201203_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
