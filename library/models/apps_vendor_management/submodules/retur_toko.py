from django.db import models

class VendorReturToko(models.Model):
    artikel = models.CharField(max_length=300, null=True)
    period      = models.DateTimeField(max_length=300, null=True)
    jml_retur      = models.IntegerField( null=True)
    created_by        = models.CharField(max_length=50, null=True)
    created_at        = models.DateTimeField(default=None, null=True, blank=True)
    updated_by        = models.CharField(max_length=50, null=True, default=None)
    updated_at        = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by        = models.CharField(max_length=50, null=True, default=None)
    deleted_at        = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label  = 'apps_vendor_management'
        db_table   = 'vendor_retur_toko'