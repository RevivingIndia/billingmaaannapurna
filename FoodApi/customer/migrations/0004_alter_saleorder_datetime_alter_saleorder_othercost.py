# Generated by Django 4.0.6 on 2023-03-24 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_saleorder_datetime_alter_saleorder_othercost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorder',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 12, 26, 20, 651857)),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='otherCost',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
