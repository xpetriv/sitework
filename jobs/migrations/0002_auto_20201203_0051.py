# Generated by Django 3.1 on 2020-12-02 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Оголошення', 'verbose_name_plural': 'Оголошення'},
        ),
        migrations.AddField(
            model_name='articles',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='articles',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]