# Generated by Django 2.1.5 on 2019-01-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20190107_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, verbose_name="Card's description"),
        ),
    ]
