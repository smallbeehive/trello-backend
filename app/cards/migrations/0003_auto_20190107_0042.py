# Generated by Django 2.1.5 on 2019-01-07 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20190106_2349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['pos']},
        ),
    ]
