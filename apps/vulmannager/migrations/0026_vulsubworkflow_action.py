# Generated by Django 2.2.6 on 2019-12-20 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vulmannager', '0025_auto_20191218_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulsubworkflow',
            name='action',
            field=models.CharField(max_length=10, verbose_name='操作'),
            preserve_default=False,
        ),
    ]
