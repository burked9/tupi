import datetime

from django.db import models
from django.utils import timezone

class Airline(models.Model):
    # The list of columns in the DB table
    index = models.IntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=False, primary_key=True)
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
    # The information which will be shown in the Admin Page
    def __str__(self):
        return self.name    

class Airport(models.Model):
    # The list of columns in the DB table
    index = models.IntegerField(blank=True, null=True)
    id = models.TextField(blank=True, null=False, primary_key=True)
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
    # The information which will be shown in the Admin Page
    def __str__(self):
        return self.name  

class Route(models.Model):
    # The list of columns in the DB table
    index = models.IntegerField(blank=True, null=False, primary_key=True)
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
    # The information which will be shown in the Admin Page
    def __str__(self):
        return str(self.dest) + " by " + str(self.source)  

class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')
    def __str__(self): 
        return self.question_text
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'

class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
    def __str__(self): 
        return self.choice_text

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()  
    location = models.CharField(max_length=100, blank=True)      
    def __str__(self):
        return self.name  
