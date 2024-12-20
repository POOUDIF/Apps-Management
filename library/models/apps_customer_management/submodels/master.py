from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class MasterCompany(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    sop                         = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_company'
        indexes     = [
            models.Index(fields=['code', 'name','sop'])
        ]

class V_MasterCompany(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    sop                         = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_company'
        managed     = False

class MasterTypeofBusiness(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_type_business'
        indexes     = [
            models.Index(fields=['code', 'name'])
        ]

class V_MasterTypeofBusiness(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_type_business'
        managed     = False

class MasterCustomerCategory(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_customer_category'
        indexes     = [
            models.Index(fields=['code', 'name'])
        ]

class V_MasterCustomerCategory(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name                        = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_customer_category'
        managed     = False

class MasterReportingPeriod(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    period                      = models.CharField(null=True, blank=True, max_length=200)
    day                         = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_reporting_period'
        indexes     = [
            models.Index(fields=['code', 'period','day'])
        ]

class V_MasterReportingPeriod(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    period                      = models.CharField(null=True, blank=True, max_length=200)
    day                         = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_reporting_period'
        managed     = False

class MasterGPSK(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    start                       = models.IntegerField(null=True, blank=True)
    end                         = models.IntegerField(null=True, blank=True)
    percent                     = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_gp_sk'
        indexes     = [
            models.Index(fields=['code', 'percent'])
        ]

class V_MasterGPSK(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    start                       = models.IntegerField(null=True, blank=True)
    end                         = models.IntegerField(null=True, blank=True)
    percent                     = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_gp_sk'
        managed     = False

class MasterParameter(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=250)
    name                        = models.CharField(null=True, blank=True, max_length=250)
    category                    = models.CharField(null=True, blank=True, max_length=250)
    text_value                  = models.TextField(null=True, blank=True, max_length=250)
    condition                   = models.CharField(null=True, blank=True, max_length=250)
    type_data_criteria          = models.CharField(null=True, blank=True, max_length=250)
    criteria                    = models.CharField(null=True, blank=True, max_length=250)
    score                       = models.IntegerField(null=True, blank=True)
    type_data_criteria_2        = models.CharField(null=True, blank=True, max_length=250)
    criteria_2                  = models.CharField(null=True, blank=True, max_length=250)
    score_2                     = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=250)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=250)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)
    order                       = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_master_parameter'
        indexes     = [
            models.Index(fields=['category', 'name','criteria','condition'])
        ]

class V_MasterParameter(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=250)
    name                        = models.CharField(null=True, blank=True, max_length=250)
    category                    = models.CharField(null=True, blank=True, max_length=250)
    text_value                  = models.TextField(null=True, blank=True, max_length=250)
    condition                   = models.CharField(null=True, blank=True, max_length=250)
    type_data_criteria          = models.CharField(null=True, blank=True, max_length=250)
    criteria                    = models.CharField(null=True, blank=True, max_length=250)
    score                       = models.IntegerField(null=True, blank=True)
    type_data_criteria_2        = models.CharField(null=True, blank=True, max_length=250)
    criteria_2                  = models.CharField(null=True, blank=True, max_length=250)
    score_2                     = models.IntegerField(null=True, blank=True)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=250)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=250)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)
    order_by                    = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_master_parameter'
        managed     = False



class V_MasterGroupCustomer(models.Model):
    name                        = models.CharField(null=True, blank=True, max_length=250)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_group_customer'
        managed     = False