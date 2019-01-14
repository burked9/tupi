# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Inventory(models.Model):
    ind = models.IntegerField(primary_key=True, blank=False, null=True)
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


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'
