# Generated by Django 2.1.1 on 2020-01-08 07:26

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skeleton', '0002_delete_carouselimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('interest', models.TextField(max_length=2000)),
            ],
        ),
    ]
