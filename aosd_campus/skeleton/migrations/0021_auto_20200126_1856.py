# Generated by Django 2.1.1 on 2020-01-27 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0020_auto_20200126_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionlink',
            name='submit_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 27, 2, 56, 54, 274961, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
