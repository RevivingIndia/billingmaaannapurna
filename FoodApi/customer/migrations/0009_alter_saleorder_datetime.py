# Generated by Django 4.0.6 on 2023-03-24 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_saleorder_discount_alter_saleorder_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleorder',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 14, 54, 22, 140234)),
        ),
    ]
