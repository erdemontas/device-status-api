# Generated by Django 2.2.7 on 2019-11-29 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceStatus', '0005_auto_20191126_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='status',
        ),
    ]
