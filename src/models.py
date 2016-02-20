# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


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


class Info(models.Model):
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    p1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    p3 = models.FloatField(blank=True, null=True)
    p4 = models.FloatField(blank=True, null=True)
    p5 = models.FloatField(blank=True, null=True)
    p6 = models.FloatField(blank=True, null=True)
    p7 = models.FloatField(blank=True, null=True)
    p8 = models.FloatField(blank=True, null=True)
    p9 = models.FloatField(blank=True, null=True)
    p10 = models.FloatField(blank=True, null=True)
    p11 = models.FloatField(blank=True, null=True)
    p12 = models.FloatField(blank=True, null=True)
    p13 = models.FloatField(blank=True, null=True)
    p14 = models.FloatField(blank=True, null=True)
    p15 = models.FloatField(blank=True, null=True)
    p16 = models.FloatField(blank=True, null=True)
    p17 = models.FloatField(blank=True, null=True)
    p18 = models.FloatField(blank=True, null=True)
    p19 = models.FloatField(blank=True, null=True)
    p20 = models.FloatField(blank=True, null=True)
    p21 = models.FloatField(blank=True, null=True)
    p22 = models.FloatField(blank=True, null=True)
    p23 = models.FloatField(blank=True, null=True)
    p24 = models.FloatField(blank=True, null=True)
    p25 = models.FloatField(blank=True, null=True)
    p26 = models.FloatField(blank=True, null=True)
    p27 = models.FloatField(blank=True, null=True)
    p28 = models.FloatField(blank=True, null=True)
    p29 = models.FloatField(blank=True, null=True)
    p30 = models.FloatField(blank=True, null=True)
    p31 = models.FloatField(blank=True, null=True)
    p32 = models.FloatField(blank=True, null=True)
    p33 = models.FloatField(blank=True, null=True)
    p34 = models.FloatField(blank=True, null=True)
    p35 = models.FloatField(blank=True, null=True)
    p36 = models.FloatField(blank=True, null=True)
    p37 = models.FloatField(blank=True, null=True)
    p38 = models.FloatField(blank=True, null=True)
    p39 = models.FloatField(blank=True, null=True)
    p40 = models.FloatField(blank=True, null=True)
    p41 = models.FloatField(blank=True, null=True)
    p42 = models.FloatField(blank=True, null=True)
    p43 = models.FloatField(blank=True, null=True)
    p44 = models.FloatField(blank=True, null=True)
    p45 = models.FloatField(blank=True, null=True)
    p46 = models.FloatField(blank=True, null=True)
    p47 = models.FloatField(blank=True, null=True)
    p48 = models.FloatField(blank=True, null=True)
    p49 = models.FloatField(blank=True, null=True)
    p50 = models.FloatField(blank=True, null=True)
    p51 = models.FloatField(blank=True, null=True)
    p52 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info'
