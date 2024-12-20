from django.db import models
import os
# import django_filters
from django.db.models import Q

from django.contrib.auth.models import User
from django.db.models.base import Model
# from bbi.base.models import BaseAPIModel2
from django.core.validators import FileExtensionValidator

from .storage import OverwriteStorage
# from bbi_backend import settings
import filecmp

class DeptMapping(models.Model):
    bu = models.CharField(max_length=100, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    nik = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    jabatan = models.CharField(max_length=100, null=True)
    parent_id = models.IntegerField( null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'm_dept_mapping'
class HeadDeptMapping(models.Model):
    bu = models.CharField(max_length=100, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'h_dept_mapping'
class PositionMapping(models.Model):
    position_group = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'position_mapping'
class PositionMappingSpc(models.Model):
    company           = models.CharField(max_length=20)
    position          = models.CharField(max_length=200)
    position_name     = models.CharField(max_length=200)
    pos_hie           = models.CharField(max_length=200)
    parent_id         = models.IntegerField(blank=True, null=True)
    source_id         = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'position_mapping_spc'
class V_User_Groupdept(models.Model):
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    organization = models.CharField(max_length=50, null=True)
    business_unit = models.CharField(max_length=50, null=True)
    groupdept = models.CharField(max_length=50, null=True)
    class Meta:
        managed     = False
        app_label   = 'bbicore'
        db_table    = 'v_user_pos'