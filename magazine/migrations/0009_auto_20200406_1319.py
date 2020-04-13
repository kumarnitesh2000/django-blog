# Generated by Django 2.1.4 on 2020-04-06 23:19

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('magazine', '0008_auto_20200406_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='casts',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='casts',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 13, 19, 44, 977922)),
        ),
    ]
