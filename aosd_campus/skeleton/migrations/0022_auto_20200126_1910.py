# Generated by Django 2.1.1 on 2020-01-27 03:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0021_auto_20200126_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionlink',
            name='submit_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 27, 3, 10, 4, 247694, tzinfo=utc), null=True),
        ),
    ]
