# Generated by Django 2.1.5 on 2019-01-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_card_img_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='img_cover',
            field=models.ImageField(blank=True, default='', upload_to='card', verbose_name="Card's attached image"),
        ),
    ]
