from django.db import models

class VendorQdd(models.Model):
    subcont          = models.CharField(null=True, blank=True, max_length=30)
    io               = models.CharField(null=True, blank=True, max_length=30)
    artikel          = models.CharField(null=True, blank=True, max_length=30)
    kerjasama        = models.CharField(null=True, blank=True, max_length=30) 
    prod_due_date    = models.DateTimeField(default=None, null=True, blank=True)
    final_inspection = models.DateTimeField(default=None, null=True, blank=True)
    garansi          = models.DateTimeField(default=None, null=True, blank=True)
    period           = models.DateTimeField(default=None, null=True, blank=True)
    status_job       = models.BooleanField(default=True)
    #quality
    qual_qty_defect = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_sampling = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_grade_a  = models.BigIntegerField(null=True, blank=True)
    qual_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #quantity
    quan_qty_complete = models.BigIntegerField(null=True, blank=True)
    quan_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #delivery
    delv_qty_ontime = models.BigIntegerField(null=True, blank=True)
    delv_qty_order  = models.BigIntegerField(null=True, blank=True)
    case            = models.CharField(null=True, blank=True, max_length=100)
    note            = models.CharField(null=True, blank=True, max_length=100)
    retur_toko      = models.IntegerField(null=True, blank=True, default=0)
    created_by      = models.CharField(max_length=50, null=True)
    created_at      = models.DateTimeField(default=None, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by      = models.CharField(max_length=50, null=True, default=None)
    deleted_by      = models.CharField(max_length=50,null=True, default=None)
    deleted_at      = models.DateTimeField(null=True,  default=None )
    

    class Meta:
        app_label = 'apps_vendor_management'
        db_table = 'vendor_qdd'

class V_VendorQdd(models.Model):
    subcont          = models.CharField(null=True, blank=True, max_length=30)
    io               = models.CharField(null=True, blank=True, max_length=30)
    artikel          = models.CharField(null=True, blank=True, max_length=30)
    kerjasama        = models.CharField(null=True, blank=True, max_length=30) 
    prod_due_date    = models.DateTimeField(default=None, null=True, blank=True)
    final_inspection = models.DateTimeField(default=None, null=True, blank=True)
    garansi          = models.DateTimeField(default=None, null=True, blank=True)
    period           = models.DateTimeField(default=None, null=True, blank=True)
    status_job       = models.BooleanField(default=True)
    #quality
    qual_qty_defect = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_sampling = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_grade_a = models.BigIntegerField(null=True, blank=True)
    qual_qty_iocut   = models.BigIntegerField(null=True, blank=True)
    #quantity
    quan_qty_complete = models.BigIntegerField(null=True, blank=True)
    quan_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #delivery
    delv_qty_ontime = models.BigIntegerField(null=True, blank=True)
    delv_qty_order  = models.BigIntegerField(null=True, blank=True)
    case = models.CharField(null=True, blank=True, max_length=100)
    note = models.CharField(null=True, blank=True, max_length=100)
    retur_toko = models.IntegerField(null=True, blank=True, default=0)
    created_by      = models.CharField(max_length=50, null=True)
    created_at      = models.DateTimeField(default=None, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by      = models.CharField(max_length=50, null=True, default=None)
    deleted_by      = models.CharField(max_length=50,null=True, default=None)
    deleted_at      = models.DateTimeField(null=True,  default=None )

    class Meta:
        managed = False
        app_label = 'apps_vendor_management'
        db_table = 'v_vendor_qdd'

class VendorQqdHistory(models.Model):
    subcont          = models.CharField(null=True, blank=True, max_length=30)
    io               = models.CharField(null=True, blank=True, max_length=30)
    artikel          = models.CharField(null=True, blank=True, max_length=30)
    kerjasama        = models.CharField(null=True, blank=True, max_length=30) 
    prod_due_date    = models.DateTimeField(default=None, null=True, blank=True)
    final_inspection = models.DateTimeField(default=None, null=True, blank=True)
    garansi          = models.DateTimeField(default=None, null=True, blank=True)
    period           = models.DateTimeField(default=None, null=True, blank=True)
    status_job       = models.BooleanField(default=True)
    #quality
    qual_qty_defect = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_sampling = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_grade_a  = models.BigIntegerField(null=True, blank=True)
    qual_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #quantity
    quan_qty_complete = models.BigIntegerField(null=True, blank=True)
    quan_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #delivery
    delv_qty_ontime = models.BigIntegerField(null=True, blank=True)
    delv_qty_order  = models.BigIntegerField(null=True, blank=True)
    case            = models.CharField(null=True, blank=True, max_length=100)
    note            = models.CharField(null=True, blank=True, max_length=100)
    retur_toko      = models.IntegerField(null=True, blank=True, default=0)
    created_by      = models.CharField(max_length=50, null=True)
    created_at      = models.DateTimeField(default=None, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by      = models.CharField(max_length=50, null=True, default=None)
    deleted_by      = models.CharField(max_length=50,null=True, default=None)
    deleted_at      = models.DateTimeField(null=True,  default=None )
    

    class Meta:
        app_label = 'apps_vendor_management'
        db_table = 'vendor_qqd_history'

class V_VendorQqdHistory(models.Model):
    subcont          = models.CharField(null=True, blank=True, max_length=30)
    io               = models.CharField(null=True, blank=True, max_length=30)
    artikel          = models.CharField(null=True, blank=True, max_length=30)
    kerjasama        = models.CharField(null=True, blank=True, max_length=30) 
    prod_due_date    = models.DateTimeField(default=None, null=True, blank=True)
    final_inspection = models.DateTimeField(default=None, null=True, blank=True)
    garansi          = models.DateTimeField(default=None, null=True, blank=True)
    period           = models.DateTimeField(default=None, null=True, blank=True)
    status_job       = models.BooleanField(default=True)
    #quality
    qual_qty_defect = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_sampling = models.BigIntegerField(null=True, blank=True, default=0)
    qual_qty_grade_a = models.BigIntegerField(null=True, blank=True)
    qual_qty_iocut   = models.BigIntegerField(null=True, blank=True)
    #quantity
    quan_qty_complete = models.BigIntegerField(null=True, blank=True)
    quan_qty_iocut    = models.BigIntegerField(null=True, blank=True)
    #delivery
    delv_qty_ontime = models.BigIntegerField(null=True, blank=True)
    delv_qty_order  = models.BigIntegerField(null=True, blank=True)
    case = models.CharField(null=True, blank=True, max_length=100)
    note = models.CharField(null=True, blank=True, max_length=100)
    retur_toko = models.IntegerField(null=True, blank=True, default=0)
    created_by      = models.CharField(max_length=50, null=True)
    created_at      = models.DateTimeField(default=None, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by      = models.CharField(max_length=50, null=True, default=None)
    deleted_by      = models.CharField(max_length=50,null=True, default=None)
    deleted_at      = models.DateTimeField(null=True,  default=None )

    class Meta:
        managed = False
        app_label = 'apps_vendor_management'
        db_table = 'v_vendor_qqd_history'