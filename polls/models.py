from datetime import datetime

from django.db import models
from django.utils import timezone

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


class SalesReport(models.Model): # Still need to change the four date columns from TEXT to DATE function
    #id = models.SmallIntegerField() # Need to find a way to add autoincrement column in first field as ID for import
    consignment_code = models.CharField(db_column='Consignment Code', max_length=30)  # Field renamed to remove unsuitable characters.
    project = models.CharField(db_column='Project', blank=True, null=True, max_length=20)  
    po = models.CharField(db_column='PO', max_length=10)  
    application_code = models.CharField(db_column='Application Code', max_length=20)  # Field renamed to remove unsuitable characters.
    tag_field = models.CharField(db_column='Tag #', blank=False, primary_key=True, max_length=30)  # Field renamed because it ended with '_'. 
    rec_date = models.CharField(db_column='REC Date', max_length=15)  # Field renamed to remove unsuitable characters. 
    stk_field = models.SmallIntegerField(db_column='STK #')  # Field renamed to remove unsuitable characters. 
    route_code = models.CharField(db_column='Route Code', max_length=20)  # Field renamed to remove unsuitable characters. 
    pn = models.CharField(db_column='PN', max_length=40)  # Field name made lowercase. 
    description = models.CharField(db_column='Description', max_length=55)  # Field name made lowercase. 
    cond = models.CharField(db_column='COND', max_length=2)  # Field name made lowercase. 
    sn = models.CharField(db_column='SN', max_length=30)  # Field name made lowercase. 
    loc_whse = models.CharField(db_column='LOC / WHSE', max_length=15)  # Field renamed to remove unsuitable characters. 
    ro_field = models.CharField(db_column='RO #', max_length=10)  # Field renamed because it ended with '_'. 
    so_field = models.CharField(db_column='SO #', max_length=10)  # Field renamed because it ended with '_'. 
    invc_field = models.CharField(db_column='INVC #', max_length=15)  # Field renamed because it ended with '_'. 
    invc_date = models.DateField(db_column='INVC Date')  # Field renamed to remove unsuitable characters. 
    ship_date = models.DateField(db_column='Ship Date')  # Field renamed to remove unsuitable characters. 
    post_date = models.DateField(db_column='Post Date')  # Field renamed to remove unsuitable characters. 
    inv_status = models.SmallIntegerField(db_column='INV Status')  # Field renamed to remove unsuitable characters. 
    inv_qty = models.SmallIntegerField(db_column='INV Qty')  # Field renamed to remove unsuitable characters. 
    gross_sales = models.FloatField(db_column='Gross Sales')  # Field renamed to remove unsuitable characters. 
    total_cost = models.FloatField(db_column='Total Cost')  # Field renamed to remove unsuitable characters. 
    freight_cost = models.FloatField(db_column='Freight Cost')  # Field renamed to remove unsuitable characters. 
    tax_amt = models.FloatField(db_column='Tax AMT')  # Field renamed to remove unsuitable characters. 
    commision = models.FloatField(db_column='Commision\nCommission')  # Field renamed to remove unsuitable characters. 
    unit_price = models.FloatField(db_column='Unit Price\nUnit Price')  # Field renamed to remove unsuitable characters. 
    ovhl_cost = models.FloatField(db_column='OVHL Cost')  # Field renamed to remove unsuitable characters. 
    unit_cost = models.FloatField(db_column='Unit Cost')  # Field renamed to remove unsuitable characters. 
    net_sales = models.FloatField(db_column='Net Sales')  # Field renamed to remove unsuitable characters. 
    list_price = models.FloatField(db_column='List Price')  # Field renamed to remove unsuitable characters.  
    lp_date = models.DateField(db_column='LP Date')  # Field renamed to remove unsuitable characters.  
    company_name_code = models.CharField(db_column='Company Name (Code)', max_length=55)  # Field renamed because it ended with '_'. 
    contact = models.CharField(db_column='Contact', max_length=30, blank=True)  # 
    country = models.CharField(db_column='Country', max_length=55, blank=True)  # 
    state = models.CharField(db_column='State', blank=True, max_length=15)  # 
    user_name = models.CharField(db_column='User Name', blank=True, null=True, max_length=30)  # Field renamed to remove unsuitable characters. 
    customer_type = models.CharField(db_column='Customer Type', blank=True, null=True, max_length=20)  # Field renamed to remove unsuitable characters. 
    airline = models.CharField(db_column='Airline', blank=True, null=True, max_length=20)  # 
    repair = models.CharField(db_column='Repair', blank=True, null=True, max_length=15)  # 
    remarks = models.CharField(db_column='REMARKS', blank=True, null=True, max_length=30)  # 
    time_life = models.CharField(db_column='TIME_LIFE', blank=True, null=True, max_length=5)  # 

    def __str__(self):
        return "pn " + str(self.pn) + " , " + str(self.invc_date) + " , " + str(self.ship_date) + " , " + str(self.post_date) 
    
    class Meta:
        managed = False
        db_table = 'sales'



class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # 
    idx = models.TextField(blank=True, null=True)  # 
    stat = models.TextField(blank=True, null=True)  # 

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'

"""
class Inventory(models.Model):
    ind = models.IntegerField(primary_key=True, blank=True, null=False)
    cons_code = models.TextField(blank=True, null=True)
    pn = models.TextField()
    description = models.TextField(blank=True, null=True)
    sn = models.TextField(blank=True, null=True)
    app_code = models.TextField(blank=True, null=True)
    ctrl_number = models.IntegerField(blank=True, null=True)
    mfg_code = models.TextField(blank=True, null=True)
    series_number = models.IntegerField(blank=True, null=True)
    part_cert_number = models.TextField(blank=True, null=True)
    sl = models.IntegerField(blank=True, null=True)
    rec_date = models.DateTimeField(blank=True, null=True)
    rep_date = models.DateTimeField(blank=True, null=True)
    rcvr = models.TextField(blank=True, null=True)
    qty_avl = models.IntegerField(blank=True, null=True)
    qty_oh = models.IntegerField(blank=True, null=True)
    total_qty = models.IntegerField(blank=True, null=True)
    lcn_code = models.TextField(blank=True, null=True)
    warehouse_code = models.TextField(blank=True, null=True)
    cond = models.TextField(blank=True, null=True)
    serialized = models.TextField(blank=True, null=True)
    traceable_to = models.TextField(blank=True, null=True)
    freight_cost = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    obtained_from = models.TextField(blank=True, null=True)
    trace_to = models.TextField(blank=True, null=True)
    time_life = models.TextField(blank=True, null=True)
    tag_date = models.DateTimeField(blank=True, null=True)
    tagged_by = models.TextField(blank=True, null=True)
    tag_details = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    ils_flag_code = models.TextField(blank=True, null=True)
    so_type = models.TextField(blank=True, null=True)
    lp = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    lp_date = models.DateTimeField(blank=True, null=True)
    unit_price = models.IntegerField(blank=True, null=True)
    mfg_usd_lp = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    exch_rate = models.IntegerField(blank=True, null=True)
    visible_mkt = models.TextField(blank=True, null=True)
    po_cost = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    inv_cost = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    origin = models.TextField(blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    cycle_rem = models.IntegerField(blank=True, null=True)
    cycles_new = models.IntegerField(blank=True, null=True)
    cycles_ovhl = models.TextField(blank=True, null=True)
    time_rem = models.IntegerField(blank=True, null=True)
    time_new = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    time_ovhl = models.TextField(blank=True, null=True)
    po_number = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    repair_cost = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    repair_date = models.DateTimeField(blank=True, null=True)
    ata = models.TextField(db_column='ATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'
    # The information which will be shown in the Admin Page
    def __str__(self):
        return self.pn   

class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'



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
"""
