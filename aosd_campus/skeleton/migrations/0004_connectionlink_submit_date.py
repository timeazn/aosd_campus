# Generated by Django 2.1.1 on 2020-01-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skeleton', '0003_connectionlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionlink',
            name='submit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
