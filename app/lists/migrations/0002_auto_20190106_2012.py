# Generated by Django 2.1.5 on 2019-01-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='pos',
            field=models.PositiveIntegerField(blank=True, verbose_name="List's position data"),
        ),
    ]
