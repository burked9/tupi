# Generated by Django 2.1.4 on 2019-01-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines',
            fields=[
                ('index', models.IntegerField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('alias', models.TextField(blank=True, null=True)),
                ('iata', models.TextField(blank=True, null=True)),
                ('icao', models.TextField(blank=True, null=True)),
                ('callsign', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('active', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'airlines',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('index', models.IntegerField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('icao', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('altitude', models.TextField(blank=True, null=True)),
                ('offset', models.TextField(blank=True, null=True)),
                ('dst', models.TextField(blank=True, null=True)),
                ('timezone', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'airports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('airline', models.TextField(blank=True, null=True)),
                ('airline_id', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('source_id', models.TextField(blank=True, null=True)),
                ('dest', models.TextField(blank=True, null=True)),
                ('dest_id', models.TextField(blank=True, null=True)),
                ('codeshare', models.TextField(blank=True, null=True)),
                ('stops', models.TextField(blank=True, null=True)),
                ('equipment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'routes',
                'managed': False,
            },
        ),
    ]