# Generated by Django 2.1.5 on 2019-01-09 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20190107_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='pos',
            field=models.DecimalField(decimal_places=17, default=65535, max_digits=30, verbose_name="List's position data"),
        ),
    ]