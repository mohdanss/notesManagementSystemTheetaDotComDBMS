# Generated by Django 3.1.4 on 2021-01-05 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDBMSapp', '0015_auto_20210105_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='userMain',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 5, 14, 42, 44, 507468)),
        ),
    ]