# Generated by Django 2.2.7 on 2019-12-01 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceStatus', '0009_auto_20191201_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusactivity',
            options={'get_latest_by': ['modified_at']},
        ),
        migrations.RenameField(
            model_name='statusactivity',
            old_name='device_id',
            new_name='device',
        ),
    ]
