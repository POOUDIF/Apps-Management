from django.db import models
from django.db.models.base import Model

from .prodev_v2 import *

class SupplierSelection(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    article             = models.ForeignKey(ColorProductDesignV2,on_delete=models.CASCADE)
    supplier_id         = models.IntegerField()
    supplier_name       = models.CharField(max_length=500)
    supplier_code       = models.CharField(max_length=50)
    type_subcon         = models.CharField(max_length=50)
    created_by          = models.CharField(max_length=50, null=True, default=None)
    created_date        = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table    = 'product_supplier'
        app_label   = 'apps_plm'

class SupplierMaster(models.Model):
    supplier_name       = models.CharField(max_length=500)
    supplier_code       = models.CharField(max_length=50)
    supplier_type       = models.CharField(max_length=50,null=True)
    is_active           = models.BooleanField(default=True)

    class Meta:
        db_table    = 'master_supplier'
        app_label   = 'apps_plm'



#supploer models version 2
class V_SupplierDashboard_V2(models.Model):
    duration            = models.CharField(max_length=100, null=True)
    code                = models.CharField(max_length=100, null=True)
    status              = models.CharField(max_length=100, null=True)
    date                = models.DateField()
    brand               = models.CharField(max_length=100, null=True)
    collection_name     = models.CharField(max_length=100, null=True)
    year                = models.CharField(max_length=100, null=True)
    quartal             = models.CharField(max_length=100, null=True)
    prod_month          = models.CharField(max_length=100, null=True)
    coll_month          = models.CharField(max_length=100, null=True)
    subbrand            = models.CharField(max_length=100, null=True)
    category            = models.CharField(max_length=100, null=True)
    article             = models.CharField(max_length=100, null=True)
    repeat_sample       = models.CharField(max_length=100, null=True)
    note                = models.CharField(max_length=100, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True)
    sample_id           = models.IntegerField()
    ref_sample          = models.CharField(max_length=50,null=True)
    old_sample_no       = models.CharField(max_length=50,null=True)
    guidance            = models.CharField(max_length=50,null=True)
    size_spec           = models.IntegerField(null=True)
    size_description    = models.CharField(max_length=50,null=True)
    running_number      = models.CharField(max_length=50,null=True)
    fabric_process      = models.CharField(max_length=5)
    accessories_process = models.CharField(max_length=5)
    thread_process      = models.CharField(max_length=5)
    artwork_process     = models.CharField(max_length=5)
    interlining_process = models.CharField(max_length=5)
    creator_name = models.CharField(max_length=10)
    no_style  = models.CharField(max_length=50,null=True)
    color_id  = models.CharField(max_length=50,null=True)


    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_supplier_dev_dashboard_v2'