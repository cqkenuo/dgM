# Generated by Django 2.2.6 on 2019-12-17 07:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulmannager', '0019_auto_20191217_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='pics',
            field=models.ManyToManyField(related_name='pics', to=settings.AUTH_USER_MODEL),
        ),
    ]
