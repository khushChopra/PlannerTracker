# Generated by Django 3.0 on 2019-12-14 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('HabitType', models.BooleanField()),
                ('creationDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HabitEntryDecimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('HabitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.Habit')),
            ],
        ),
        migrations.CreateModel(
            name='HabitEntryBool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HabitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.Habit')),
            ],
        ),
    ]