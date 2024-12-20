from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class MasterPointOfFocus(models.Model):
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    brand                       = models.CharField(null=True, blank=True, max_length=200)
    style_category              = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_master_point_of_focus'
        indexes     = [
            models.Index(fields=['value', 'style_category'])
        ]

class V_MasterPointOfFocus(models.Model):
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    brand                       = models.CharField(null=True, blank=True, max_length=200)
    style_category              = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_master_point_of_focus'
        managed     = False

class MasterAQL(models.Model):
    quality_level               = models.CharField(null=True, blank=True, max_length=200)
    size_min                    = models.IntegerField(null=True, blank=True)
    size_max                    = models.IntegerField(null=True, blank=True)
    sample_size                 = models.IntegerField(null=True, blank=True)
    accept_major                = models.IntegerField(null=True, blank=True)
    accept_minor                = models.IntegerField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_master_aql'
        indexes     = [
            models.Index(fields=['quality_level','sample_size','accept_major','accept_minor'])
        ]

class V_MasterAQL(models.Model):
    quality_level               = models.CharField(null=True, blank=True, max_length=200)
    size_min                    = models.IntegerField(null=True, blank=True)
    size_max                    = models.IntegerField(null=True, blank=True)
    sample_size                 = models.IntegerField(null=True, blank=True)
    accept_major                = models.IntegerField(null=True, blank=True)
    accept_minor                = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_master_aql'
        managed     = False

class InspectionMasterApprover(models.Model):
    name   = models.CharField(null=True, blank=True, max_length=200)
    pos    = models.CharField(null=True, blank=True, max_length=200)
    email  = models.CharField(null=True, blank=True, max_length=200)
    nik    = models.CharField(null=True, blank=True, max_length=200)
    title  = models.CharField(null=True, blank=True, max_length=200)
    cc     = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_master_approver'
        indexes     = [
            models.Index(fields=['nik','pos','name'])
        ]

class V_InspectionMasterApprover(models.Model):
    nik   = models.CharField(null=True, blank=True, max_length=200)
    name  = models.CharField(null=True, blank=True, max_length=200)
    pos   = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    title = models.CharField(null=True, blank=True, max_length=200)
    cc    = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_master_approver'
        managed     = False

class MasterDefect(models.Model):
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)


    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_master_defect'
        indexes     = [
            models.Index(fields=['zone','defect','classification'])
        ]

class V_MasterDefect(models.Model):
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_master_defect'
        managed     = False


class MasterChecklist(models.Model):
    category                    = models.CharField(null=True, blank=True, max_length=200)
    label                       = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_master_checklist'
        indexes     = [
            models.Index(fields=['category','label'])
        ]

class V_MasterChecklist(models.Model):
    category                    = models.CharField(null=True, blank=True, max_length=200)
    label                       = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_master_checklist'
        managed     = False

class V_VendorList(models.Model):
    supplier_code               = models.CharField(null=True, blank=True, max_length=200)
    supplier_name               = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_vendor_list'
        managed     = False