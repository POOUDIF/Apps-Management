from django.db import models
from .bussiness_category import *

class VendorCategoryProduct(models.Model):
    category_product_code = models.CharField(max_length=300, null=True)
    category_product_name = models.CharField(max_length=300, null=True)
    source_code = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    business_category = models.ForeignKey(VendorBusinessCategory, on_delete=models.CASCADE)
    parent_category = models.IntegerField(null=True, blank=True)
    # business_name = models.CharField(max_length=300, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    
    class Meta:
        app_label  = 'apps_vendor_management'
        db_table   = 'vendor_category_product'

class V_VendorCategoryProduct(models.Model):
    category_product_code =models.CharField(max_length=300, null=True)
    category_product_name = models.CharField(max_length=300, null=True)
    source_code = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    business_category = models.ForeignKey(VendorBusinessCategory, on_delete=models.CASCADE)
    parent_category = models.IntegerField(null=True, blank=True)
    # business_name = models.CharField(max_length=300, null=True)
    # business_category_code = models.CharField(max_length=300, null=True)


    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_category_product'
        managed     = False

class V_getVendorCategoryProduct(models.Model):
    category_product_code =models.CharField(max_length=300, null=True)
    category_product_name = models.CharField(max_length=300, null=True)
    source_code = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    business_category = models.ForeignKey(VendorBusinessCategory, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=300, null=True)
    business_category_code = models.CharField(max_length=300, null=True)
    parent_category = models.IntegerField(null=True, blank=True)
    # deleted_by = models.CharField(max_length=50, null=True, default=None)
    # deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_get_vendor_category_product'
        managed     = False

class VendorGroupCategory(models.Model):
    group_category_code = models.CharField(max_length=300, null=True)
    group_category_name = models.CharField(max_length=300, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    
    class Meta:
        app_label  = 'apps_vendor_management'
        db_table   = 'vendor_group_category'
