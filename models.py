# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airlines(models.Model):
    index = models.IntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    iata = models.TextField(blank=True, null=True)
    icao = models.TextField(blank=True, null=True)
    callsign = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    active = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airlines'


class Airports(models.Model):
    index = models.IntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    icao = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    altitude = models.TextField(blank=True, null=True)
    offset = models.TextField(blank=True, null=True)
    dst = models.TextField(blank=True, null=True)
    timezone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airports'


class Routes(models.Model):
    index = models.IntegerField(blank=True, null=True)
    airline = models.TextField(blank=True, null=True)
    airline_id = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    dest = models.TextField(blank=True, null=True)
    dest_id = models.TextField(blank=True, null=True)
    codeshare = models.TextField(blank=True, null=True)
    stops = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'
