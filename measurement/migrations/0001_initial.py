# Generated by Django 4.1.4 on 2023-10-15 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Температура измерения')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата и время измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
        ),
    ]
