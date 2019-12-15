# Generated by Django 2.2.8 on 2019-12-14 23:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryDate', models.DateField(default=datetime.datetime(2019, 12, 14, 23, 59, 28, 768476, tzinfo=utc))),
                ('title', models.CharField(max_length=150)),
                ('isComplete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DailyNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryDate', models.DateField(default=datetime.datetime(2019, 12, 14, 23, 59, 28, 788219, tzinfo=utc))),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MainGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLongTerm', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=150)),
                ('isComplete', models.BooleanField(default=False)),
            ],
        ),
    ]