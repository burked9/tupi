# Generated by Django 2.1.4 on 2019-01-09 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_monthlyweatherbycity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
    ]
