# Generated by Django 2.2.6 on 2019-12-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulmannager', '0006_penetrationtestticketsubworkflow_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penetrationtestticketsubworkflow',
            name='action',
            field=models.CharField(max_length=10, verbose_name='操作'),
        ),
    ]
