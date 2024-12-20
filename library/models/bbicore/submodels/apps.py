from django.db import models

from .base import BaseModel


class Applications(models.Model):
    code            = models.CharField(unique=True, max_length=20)
    group           = models.CharField(max_length=20)
    name            = models.CharField(max_length=50)
    class Meta:
        app_label   = 'bbicore'
        db_table    = 'applications'
        ordering    = ['group', 'code']
        verbose_name        = 'Menu Config - Application'
        verbose_name_plural = 'Menu Config - Applications'
    def __str__(self):
        return '(%s) %s -- %s'%(self.group, self.code, self.name)


'''
ApplicationConfig & ReportConfig
================================
code        : application code / unique ID
group       : grouping of application (PPC / Design / HR / Sales / FA / etc)
image       : icon
route       : URL path to application
mode        : REDIRECT / NEW_TAB / NEW_WINDOW. Default = REDIRECT
custom_param    : json / pre-loaded parameters for future implementation. Value will be stored as json
'''
class ApplicationConfig(BaseModel):
    OPT_MODE = (('REDIRECT', 'REDIRECT'), ('NEW_TAB', 'NEW_TAB'), ('NEW_WINDOW', 'NEW_WINDOW'))
    code            = models.CharField(unique=True, max_length=20)
    group           = models.CharField(max_length=20)
    mode            = models.CharField(max_length=10, choices=OPT_MODE, default = 'REDIRECT')
    route           = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='app/images/', max_length=255, null=True, blank=True)
    custom_param    = models.TextField(null=True)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'app_config'
        ordering    = ['group', 'code']
        verbose_name        = 'Menu Config - Application'
        verbose_name_plural = 'Menu Config - Applications'
    def __str__(self):
        return '(%s) %s -- %s'%(self.group, self.code, self.name)


class ReportConfig(BaseModel):
    OPT_MODE = (('REDIRECT', 'REDIRECT'), ('NEW_TAB', 'NEW_TAB'), ('NEW_WINDOW', 'NEW_WINDOW'))
    code            = models.CharField(unique=True, max_length=20)
    group           = models.CharField(max_length=20)
    mode            = models.CharField(max_length=10, choices=OPT_MODE, default = 'REDIRECT')
    route           = models.CharField(max_length=100)
    image           = models.ImageField(upload_to='rpt/images/', max_length=255, null=True, blank=True)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'rpt_config'
        ordering    = ['group', 'code']
        verbose_name        = 'Menu Config - Report'
        verbose_name_plural = 'Menu Config - Reports'
    custom_param    = models.TextField(null=True)
    def __str__(self):
        return '(%s) %s -- %s'%(self.group, self.code, self.name)


class AppAccess(BaseModel):
    user_group      = models.CharField(max_length=20, blank=True, null=True)
    app_access      = models.ManyToManyField(ApplicationConfig, verbose_name=('Application Access'), blank=True,)


    class Meta:
        app_label   = 'bbicore'
        db_table    = 'user_appaccess'
        ordering            = ['user_group']
        verbose_name        = 'User Role - Applications'

    def __str__(self):
        return '%s -- %s'%(self.user_group, self.name)


class RptAccess(BaseModel):
    user_group      = models.CharField(max_length=20, blank=True, null=True)
    rpt_access      = models.ManyToManyField(ReportConfig, verbose_name=('Report Access'), blank=True,)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'user_rptaccess'
        ordering            = ['user_group']
        verbose_name        = 'User Role - Reports'

    def __str__(self):
        return '%s -- %s'%(self.user_group, self.name)


class BbiSmgAccess(BaseModel):
    business_unit   = models.CharField(max_length=50)
    app_access      = models.ManyToManyField(AppAccess, verbose_name=('Application Access - BBI Semarang'), blank=True,)
    rpt_access      = models.ManyToManyField(RptAccess, verbose_name=('Report Setting Mapping - BBI Semarang'), blank=True,)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'usersmg_access'
        ordering    = ['business_unit', 'name']
        verbose_name        = "User Access (Semarang) - Apps & Reports"


class V_BBIAppAccess(models.Model):
    rolename        = models.CharField(max_length=100)
    rolegroup       = models.CharField(max_length=20)
    acc_id          = models.IntegerField()
    acc_code        = models.CharField(max_length=50)
    is_active       = models.BooleanField()

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_bbi_appaccess'
        unique_together = (('rolename', 'acc_id'))

class V_BBIRptAccess(models.Model):
    rolename_rpt    = models.CharField(max_length=100)
    rolegroup_rpt   = models.CharField(max_length=20)
    rpt_id          = models.IntegerField()
    rpt_code        = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_bbi_rptaccess'
        unique_together = (('rolename_rpt', 'rpt_id'))



class V_UserSmgAppAccess(models.Model):
    rolename        = models.CharField(max_length=100)
    business_unit   = models.CharField(max_length=50)
    department      = models.CharField(max_length=100)
    subdepartment   = models.CharField(max_length=100)
    app_id          = models.IntegerField()
    app_code        = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_usersmg_appaccess'
        unique_together = (('rolename', 'business_unit', 'app_id'),)



class V_UserSmgRptAccess(models.Model):
    rolename        = models.CharField(max_length=100)
    business_unit   = models.CharField(max_length=50)
    rpt_id          = models.IntegerField()
    rpt_code        = models.CharField(max_length=50)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_usersmg_rptaccess'
        unique_together = (('rolename', 'business_unit', 'rpt_id'),)