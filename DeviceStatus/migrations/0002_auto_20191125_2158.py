# Generated by Django 2.2.7 on 2019-11-25 18:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceStatus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='device_name',
            field=models.CharField(default=datetime.datetime(2019, 11, 25, 18, 58, 32, 722682, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
