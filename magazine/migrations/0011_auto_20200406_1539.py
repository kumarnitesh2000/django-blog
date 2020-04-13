# Generated by Django 2.1.4 on 2020-04-07 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_auto_20200406_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casts',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 15, 39, 26, 823975)),
        ),
        migrations.AlterField(
            model_name='casts',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique_for_date=True),
        ),
    ]
