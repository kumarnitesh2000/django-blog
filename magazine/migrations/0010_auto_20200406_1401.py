# Generated by Django 2.1.4 on 2020-04-07 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0009_auto_20200406_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casts',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 14, 1, 25, 880929)),
        ),
    ]
