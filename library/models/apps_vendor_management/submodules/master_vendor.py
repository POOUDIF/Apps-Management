from django.db import models

class Mastervendor(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.CharField(max_length=300, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    source_last_updated = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'vendor_master_vendor'

class V_MasterVendor(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.CharField(max_length=300, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    source_last_updated = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'vendor_master_vendor'
        managed = False

class CapacityVendor(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    group_code = models.IntegerField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'vendor_capacity'

class V_GetCapacityVendor(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    group_code = models.IntegerField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    group_category_code = models.CharField(max_length=300, null=True)
    group_category_name = models.CharField(max_length=300, null=True)
    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_get_capacity_vendor'
        managed = False

class V_MasterForPLM(models.Model):
    vendor_code = models.CharField( primary_key=True, max_length=300)
    vendor_id = models.CharField(max_length=300, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_qdd = models.IntegerField(default=0, null=True)
    history_cost = models.IntegerField(default=0, null=True)
    selisih_cost = models.IntegerField(default=0, null=True)
    count = models.IntegerField(default=0, null=True)
    capacity = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    ranking = models.IntegerField(default=0, null=True)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_api_plm'
        managed = False