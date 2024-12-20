from django.db import models

class VendorBusinessCategory(models.Model):
    business_category_code = models.CharField(max_length=300, null=True)
    business_name = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label  = 'apps_vendor_management'
        db_table   = 'vendor_business_category'


class V_VendorBusinessCategory(models.Model):
    business_category_code = models.CharField(max_length=300, null=True)
    business_name = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_business_category'
        managed     = False

# class V_BusinessOracle(models.Model):
#     brand = models.CharField(max_length=100, null=True)
#     created = models.CharField(max_length=30, null=True)
#     artikel = models.CharField(max_length=30, null=True)
#     io = models.IntegerField(primary_key=True)
#     kode_category = models.CharField(max_length=300, null=True)
#     kategory_name = models.CharField(max_length=300, null=True)
#     brand = models.CharField(max_length=30, null=True)
#     brand_name = models.CharField(max_length=30, null=True)
#     production_due_date = models.DateField(null=True)
#     size_qty = models.IntegerField(null=True)
#     vendor_code = models.CharField(max_length=300, null=True)
#     vendor_name = models.CharField(max_length=300, null=True)
#     harga = models.IntegerField(null=True)
#     cogm = models.IntegerField(null=True)
    

#     class Meta:
#         app_label   = 'apps_vendor_management'
#         db_table    = 'v_business_v2'
#         managed     = False
class V_BusinessOracle(models.Model):
    brand = models.CharField(max_length=100, null=True)
    artikel = models.CharField(max_length=30, null=True)
    IO_HEADER_NUMBER = models.IntegerField(primary_key=True)
    kode_category = models.CharField(max_length=300, null=True)
    kategory_name = models.CharField(max_length=300, null=True)
    BRAND_NAME = models.CharField(max_length=30, null=True)
    PRODUCTION_DUE_DATE = models.DateField(null=True)
    IO_SIZE_QUANTITY = models.IntegerField(null=True)
    VENDOR_NAME = models.CharField(max_length=300, null=True)
    VENDOR_ID = models.CharField(max_length=300, null=True)
    harga = models.IntegerField(null=True)
    cogm = models.IntegerField(null=True)
    

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_business_v3'
        managed     = False
