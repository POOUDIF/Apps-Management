from django.db import models

class VendorServiceType(models.Model):
    service_type_code = models.CharField(max_length=300, null=True)
    service_name      = models.CharField(max_length=300, null=True)
    status            = models.BooleanField(default=True)
    created_by        = models.CharField(max_length=50, null=True)
    created_at        = models.DateTimeField(default=None, null=True, blank=True)
    updated_by        = models.CharField(max_length=50, null=True, default=None)
    updated_at        = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by        = models.CharField(max_length=50, null=True, default=None)
    deleted_at        = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label  = 'apps_vendor_management'
        db_table   = 'vendor_service_type'

class V_VendorServiceType(models.Model):
    service_type_code = models.CharField(max_length=300, null=True)
    service_name      = models.CharField(max_length=300, null=True)
    status            = models.BooleanField(default=True)
    created_by        = models.CharField(max_length=50, null=True)
    created_at        = models.DateTimeField(default=None, null=True, blank=True)
    updated_by        = models.CharField(max_length=50, null=True, default=None)
    updated_at        = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by        = models.CharField(max_length=50, null=True, default=None)
    deleted_at        = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_service_type'
        managed     = False
