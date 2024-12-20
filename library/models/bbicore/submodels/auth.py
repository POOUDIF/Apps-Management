from django.db import models


class UserSession(models.Model):
    username        = models.CharField(max_length=50, unique=True)
    business_unit   = models.CharField(max_length=50, default='BBI1')
    is_locked       = models.BooleanField(default=False)
    is_first_login  = models.BooleanField(default=True, editable=False)
    last_login      = models.DateTimeField(auto_now=True)
    failed_attemps  = models.IntegerField(default=0)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'user_session'
        ordering = ['-last_login']


class LoginLog(models.Model):
    username        = models.CharField(max_length=50, blank=True, null=True)
    business_unit   = models.CharField(max_length=50, default='BBI1')
    ip_addr         = models.CharField(max_length=16)
    is_success      = models.BooleanField()
    err_msg         = models.CharField(max_length=500, blank=True, null=True)
    date            = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'login_log'
        ordering = ['-date']


class V_UserLogin(models.Model):
    username        = models.CharField(max_length=20, primary_key=True)
    fail_count      = models.IntegerField()

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_user_login'



class V_BbiSmgUser(models.Model):
    nik                 = models.CharField(max_length=20, primary_key=True)
    name                = models.CharField(max_length=200)
    department_name     = models.CharField(max_length=200)
    subdept_name        = models.CharField(max_length=200)
    position            = models.CharField(max_length=100)
    factory             = models.CharField(max_length=20)
    password            = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_bbismg_user'

class BBIUserData(models.Model):
    username            = models.CharField(max_length=20, primary_key=True)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    organization        = models.CharField(max_length=200)
    organization_name   = models.CharField(max_length=200)
    position            = models.CharField(max_length=200)
    position_name       = models.CharField(max_length=200)
    pos_hie             = models.CharField(max_length=100)
    business_unit       = models.CharField(max_length=100)
    job                 = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_user_bbip'

class BBIUserQC(models.Model):
    nik            = models.CharField(max_length=20, primary_key=True)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    organization        = models.CharField(max_length=200)
    organization_name   = models.CharField(max_length=200)
    position_name       = models.CharField(max_length=200)
    business_unit       = models.CharField(max_length=100)
    job                 = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_user_qc'


class AllUserData(models.Model):
    username            = models.CharField(max_length=20, primary_key=True)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    organization        = models.CharField(max_length=200)
    organization_name   = models.CharField(max_length=200)
    path                = models.TextField()
    position            = models.CharField(max_length=200)
    position_name       = models.CharField(max_length=200)
    pos_hie             = models.CharField(max_length=100)
    business_unit       = models.CharField(max_length=100)
    job                 = models.CharField(max_length=100)
    gender              = models.CharField(max_length=2)
    area                = models.CharField(max_length=50)
    subarea             = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_user_all'

class PosUserData(models.Model):
    username            = models.CharField(max_length=20, primary_key=True)
    first_name          = models.CharField(max_length=200)
    last_name           = models.CharField(max_length=200)
    organization        = models.CharField(max_length=200)
    organization_name   = models.CharField(max_length=200)
    position            = models.CharField(max_length=200)
    position_name       = models.CharField(max_length=200)
    email               = models.CharField(max_length=200)
    pos_hie             = models.CharField(max_length=100)
    business_unit       = models.CharField(max_length=100)
    groupdept           = models.CharField(max_length=50, null=True)
    job                 = models.CharField(max_length=100)
    gender              = models.CharField(max_length=2)
    area                = models.CharField(max_length=50)
    subarea             = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_user_pos'

class PositionData(models.Model):
    company           = models.CharField(max_length=20)
    position          = models.CharField(max_length=200)
    position_name     = models.CharField(max_length=200)
    pos_hie           = models.CharField(max_length=200)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_position'