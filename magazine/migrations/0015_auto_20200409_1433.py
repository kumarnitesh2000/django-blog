# Generated by Django 2.1.4 on 2020-04-10 00:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('magazine', '0014_auto_20200409_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='casts',
            name='publish_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='published_by', to='accounts.UserModel'),
        ),
        migrations.AlterField(
            model_name='casts',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 14, 33, 25, 476692)),
        ),
    ]
