# Generated by Django 2.1.5 on 2019-01-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190106_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bgColor',
            field=models.CharField(default='rgb(0, 121, 191)', max_length=50, verbose_name="Board's background color"),
        ),
    ]
