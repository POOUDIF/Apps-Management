from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class InspectionMonitoring(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    article                     = models.CharField(null=True, blank=True, max_length=50)
    qty_order                   = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    brand                       = models.CharField(null=True, blank=True, max_length=50)
    category                    = models.CharField(null=True, blank=True, max_length=50)
    delivery                    = models.DateField(null=True, blank=True)
    style_code                  = models.CharField(null=True, blank=True, max_length=50)
    style_desc                  = models.TextField(null=True, blank=True)
    maintainer_nik              = models.CharField(null=True, blank=True, max_length=50)
    maintainer_name             = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_monitoring'
        indexes     = [
            models.Index(fields=['io', 'created', 'created_by_name','updated','updated_by_name'])
        ]

class V_InspDashMonitoring(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    article                     = models.CharField(null=True, blank=True, max_length=50)
    qty_order                   = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    brand                       = models.CharField(null=True, blank=True, max_length=50)
    category                    = models.CharField(null=True, blank=True, max_length=50)
    delivery                    = models.DateField(null=True, blank=True)
    style_code                  = models.CharField(null=True, blank=True, max_length=50)
    style_desc                  = models.TextField(null=True, blank=True)
    maintainer_nik              = models.CharField(null=True, blank=True, max_length=50)
    maintainer_name             = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)
    parent                      = models.BooleanField(blank=True, null=True)
    parent_to                   = models.IntegerField(blank=True, null=True)
    inspection_type             = models.CharField(null=True, blank=True, max_length=200)
    inspector_nik               = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_monitoring'
        managed     = False

class InspectionMonitoringDetail(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    monitoring_id               = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    inspection_type             = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    pic_nik                     = models.CharField(null=True, blank=True, max_length=50)
    pic_name                    = models.CharField(null=True, blank=True, max_length=100)
    plan_date                   = models.DateField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)
    actual_date                 = models.DateTimeField(blank=True, null=True)
    parent                      = models.BooleanField(blank=True, null=True)
    parent_to                   = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_monitoring_detail'
        indexes     = [
            models.Index(fields=['io', 'monitoring_id', 'created', 'created_by_name','updated','updated_by_name'])
        ]

class V_InspectionMonitoringDetail(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    article                     = models.CharField(null=True, blank=True, max_length=20)
    monitoring_id               = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    inspection_type             = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    pic_nik                     = models.CharField(null=True, blank=True, max_length=50)
    pic_name                    = models.CharField(null=True, blank=True, max_length=100)
    plan_date                   = models.DateField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)
    actual_date                 = models.DateTimeField(blank=True, null=True)
    parent                      = models.BooleanField(blank=True, null=True)
    parent_to                   = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_monitoring_detail'
        managed     = False

class V_InspectionReport(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    monitoring_id               = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    inspection_type             = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    pic_nik                     = models.CharField(null=True, blank=True, max_length=50)
    pic_name                    = models.CharField(null=True, blank=True, max_length=100)
    plan_date                   = models.DateField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)
    actual_date                 = models.DateTimeField(blank=True, null=True)
    factory                     = models.CharField(blank=True, null=True, max_length=200)
    article                     = models.CharField(blank=True, null=True, max_length=200)
    qty_order                   = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_report'
        managed     = False

class V_InspActivity(models.Model):
    name                        = models.CharField(null=True, blank=True, max_length=100)
    is_active                   = models.BooleanField()

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_activity'
        managed     = False

class V_InspMasterFactory(models.Model):
    name                        = models.CharField(null=True, blank=True, max_length=100)
    is_active                   = models.BooleanField()

    class Meta:
        app_label   = 'apps_master'
        db_table    = 'v_master_factory'
        managed     = False
