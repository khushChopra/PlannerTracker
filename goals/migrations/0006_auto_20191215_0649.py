# Generated by Django 2.2.8 on 2019-12-15 01:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_auto_20191215_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailygoals',
            name='entryDate',
            field=models.DateField(default=datetime.datetime(2019, 12, 15, 1, 19, 57, 781108, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dailynote',
            name='entryDate',
            field=models.DateField(default=datetime.datetime(2019, 12, 15, 1, 19, 57, 800396, tzinfo=utc), unique=True),
        ),
        migrations.AlterField(
            model_name='maingoals',
            name='creationDate',
            field=models.DateField(default=datetime.datetime(2019, 12, 15, 1, 19, 57, 800917, tzinfo=utc)),
        ),
    ]
