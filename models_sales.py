# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inventory(models.Model):
    ind = models.IntegerField(primary_key=True, blank=True, null=True)
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


class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsPerson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    birth_date = models.DateField()
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'polls_person'


class PollsQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Sales(models.Model):
    consignment_code = models.TextField(db_column='Consignment Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    project = models.TextField(db_column='Project', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    po = models.TextField(db_column='PO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    application_code = models.TextField(db_column='Application Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    tag_field = models.TextField(db_column='Tag #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    rec_date = models.TextField(db_column='REC Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    stk_field = models.TextField(db_column='STK #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    route_code = models.TextField(db_column='Route Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    pn = models.TextField(db_column='PN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cond = models.TextField(db_column='COND', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sn = models.TextField(db_column='SN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loc_whse = models.TextField(db_column='LOC / WHSE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ro_field = models.TextField(db_column='RO #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    so_field = models.TextField(db_column='SO #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    invc_field = models.TextField(db_column='INVC #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    invc_date = models.TextField(db_column='INVC Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ship_date = models.TextField(db_column='Ship Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    post_date = models.TextField(db_column='Post Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    inv_status = models.TextField(db_column='INV Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    inv_qty = models.TextField(db_column='INV Qty', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    gross_sales = models.TextField(db_column='Gross Sales', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    total_cost = models.TextField(db_column='Total Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    freight_cost = models.TextField(db_column='Freight Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    tax_amt = models.TextField(db_column='Tax AMT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    commision_commission = models.TextField(db_column='Commision\nCommission', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    unit_price_unit_price = models.TextField(db_column='Unit Price\nUnit Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ovhl_cost = models.TextField(db_column='OVHL Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    unit_cost = models.TextField(db_column='Unit Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    net_sales = models.TextField(db_column='Net Sales', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    list_price = models.TextField(db_column='List Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    lp_date = models.TextField(db_column='LP Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    company_name_code_field = models.TextField(db_column='Company Name (Code)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    contact = models.TextField(db_column='Contact', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    user_name = models.TextField(db_column='User Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    customer_type = models.TextField(db_column='Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    airline = models.TextField(db_column='Airline', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair = models.TextField(db_column='Repair', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    time_life = models.TextField(db_column='TIME_LIFE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sales'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'
