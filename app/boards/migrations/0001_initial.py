# Generated by Django 2.1.5 on 2019-01-06 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name="Board's content")),
                ('bgColor', models.CharField(blank=True, max_length=50, verbose_name="Board's background color")),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
