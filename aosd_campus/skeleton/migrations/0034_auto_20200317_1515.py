# Generated by Django 2.1.1 on 2020-03-17 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0033_auto_20200317_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionlink',
            name='submit_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 3, 17, 22, 15, 58, 732797, tzinfo=utc), null=True),
        ),
    ]
