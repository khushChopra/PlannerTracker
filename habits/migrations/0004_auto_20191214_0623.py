# Generated by Django 2.2 on 2019-12-14 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20191214_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitentrydecimal',
            old_name='habitID',
            new_name='habit',
        ),
    ]
