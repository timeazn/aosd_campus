# Generated by Django 2.1.1 on 2020-01-13 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0017_auto_20200110_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionlink',
            name='submit_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 13, 20, 58, 27, 232683, tzinfo=utc), null=True),
        ),
    ]
