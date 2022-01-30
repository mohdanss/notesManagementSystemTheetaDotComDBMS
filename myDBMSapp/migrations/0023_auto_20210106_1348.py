# Generated by Django 3.1.4 on 2021-01-06 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDBMSapp', '0022_auto_20210106_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_messaged',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 13, 48, 17, 506089)),
        ),
        migrations.AlterField(
            model_name='contributions',
            name='contribution_link',
            field=models.URLField(blank=True, max_length=128, null=True, verbose_name='Content-Link'),
        ),
    ]