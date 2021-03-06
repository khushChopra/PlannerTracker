# Generated by Django 2.2.8 on 2019-12-15 01:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_auto_20191215_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='maingoals',
            name='creationDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailygoals',
            name='entryDate',
            field=models.DateField(default=datetime.datetime(2019, 12, 15, 1, 18, 0, 494903, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dailynote',
            name='entryDate',
            field=models.DateField(default=datetime.datetime(2019, 12, 15, 1, 18, 0, 514287, tzinfo=utc), unique=True),
        ),
    ]
