# Generated by Django 2.1.5 on 2019-01-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20190107_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='listId',
            new_name='list_id',
        ),
    ]
