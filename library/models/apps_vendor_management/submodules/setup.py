from django.db import models

class VendorSetup(models.Model):#migrasi vendor code, vendor_code_sap, vendor_name
    vendor_code = models.CharField(max_length=300, null=True)
    business_category = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.BigIntegerField(default=0, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    article = models.CharField(max_length = 20, null=True)
    category_product = models.CharField(max_length=300, null=True)
    service_type = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    vendor_qdd = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)
    history_cost = models.BigIntegerField(default=0, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    qty_delivery = models.BigIntegerField(default=0, null=True)
    io = models.BigIntegerField(default=0, null=True)
    source_id = models.BigIntegerField(default=0, null=True)
    source_last_updated = models.DateTimeField(default=None, null=True, blank=True)
    period = models.DateTimeField(default=None, null=True, blank=True)
    vendor_flexibility = models.CharField(max_length=10, null=True)
    status      = models.BooleanField(default=True)
    promised_date = models.DateField(null=True, blank=True)
    transaction_date = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'vendor_setup'

class VendorSetupPlm(models.Model):#migrasi vendor code, vendor_code_sap, vendor_name
    vendor_code = models.CharField(max_length=300, null=True)
    business_category = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.BigIntegerField(default=0, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    article = models.CharField(max_length = 20, null=True)
    category_product = models.CharField(max_length=300, null=True)
    service_type = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    vendor_qdd = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)
    history_cost = models.BigIntegerField(default=0, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    qty_delivery = models.BigIntegerField(default=0, null=True)
    io = models.BigIntegerField(default=0, null=True)
    source_id = models.BigIntegerField(default=0, null=True)
    source_last_updated = models.DateTimeField(default=None, null=True, blank=True)
    period = models.DateTimeField(default=None, null=True, blank=True)
    vendor_flexibility = models.CharField(max_length=10, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'vendor_setup_plm'

class V_VendorSetup(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    business_category = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.BigIntegerField(default=0, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    article = models.CharField(max_length = 20, null=True)
    category_product = models.CharField(max_length=300, null=True)
    service_type = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    vendor_qdd = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)
    history_cost = models.BigIntegerField(default=0, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    qty_delivery = models.BigIntegerField(default=0, null=True)
    io = models.BigIntegerField(default=0, null=True)
    source_id = models.BigIntegerField(default=0, null=True)
    source_last_updated = models.DateTimeField(default=None, null=True, blank=True)
    period = models.DateTimeField(default=None, null=True, blank=True)
    vendor_flexibility = models.CharField(max_length=10, null=True)
    status      = models.BooleanField(default=True)
    promised_date = models.DateField(null=True, blank=True)
    transaction_date = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_setup'
        managed = False

class V_VendorSetupV2(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    business_category = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.BigIntegerField(default=0, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    article = models.CharField(max_length = 20, null=True)
    category_product = models.CharField(max_length=300, null=True)
    service_type = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    vendor_qdd = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)
    history_cost = models.BigIntegerField(default=0, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    qty_delivery = models.BigIntegerField(default=0, null=True)
    io = models.BigIntegerField(default=0, null=True)
    source_id = models.BigIntegerField(default=0, null=True)
    source_last_updated = models.DateTimeField(default=None, null=True, blank=True)
    period_date = models.DateField(default=None, null=True, blank=True)
    period = models.DateTimeField(default=None, null=True, blank=True)
    vendor_flexibility = models.CharField(max_length=10, null=True)
    # status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_setup_capacity'
        managed = False

class V_VendorSetupRank(models.Model):
    vendor_code = models.CharField(max_length=300, null=True)
    business_category = models.CharField(max_length=300, null=True)
    vendor_code_sap = models.BigIntegerField(default=0, null=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    article = models.CharField(max_length = 20, null=True)
    category_product = models.CharField(max_length=300, null=True)
    service_type = models.CharField(max_length=300, null=True)
    vendor_capacity = models.BigIntegerField(default=0, null=True)
    vendor_qdd = models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)
    history_cost = models.BigIntegerField(default=0, null=True)
    qty = models.BigIntegerField(default=0, null=True)
    qty_delivery = models.BigIntegerField(default=0, null=True)
    io = models.BigIntegerField(default=0, null=True)
    source_id = models.BigIntegerField(default=0, null=True)
    source_last_updated = models.DateTimeField(default=None, null=True, blank=True)
    period = models.DateTimeField(default=None, null=True, blank=True)
    vendor_flexibility = models.CharField(max_length=10, null=True)
    selisih_cost = models.BigIntegerField(default=0, null=True)
    status      = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_vendor_setup'
        managed = False

# class V_OracleSetup(models.Model):
#     created = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
#     io = models.BigIntegerField(default=0, null=True)
#     brand = models.CharField(max_length=300, null=True)
#     artikel = models.CharField(primary_key=True, max_length=300)
#     size_qty = models.BigIntegerField(default=0, null=True)
#     production_due_date = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
#     vendor_name = models.CharField(max_length=300, null=True)
#     vendor_code = models.CharField(max_length=300, null=True)
#     kode_category = models.CharField(max_length=300, null=True)
#     kategory_name = models.CharField(max_length=300, null=True)
#     harga = models.BigIntegerField(default=0, null=True)
#     cogm = models.BigIntegerField(default=0, null=True)
#     class Meta:
#         app_label   = 'apps_vendor_management'
#         db_table    = 'v_data_oracle_io'
#         managed = False
class V_OracleSetup(models.Model):
    IO_HEADER_NUMBER = models.BigIntegerField(default=0, null=True)
    brand_name = models.CharField(max_length=300, null=True)
    artikel = models.CharField(primary_key=True, max_length=300)
    io_size_quantity = models.BigIntegerField(default=0, null=True)
    production_due_date = models.DateField(auto_now_add=True, editable=False, null=True, blank=True)
    vendor_name = models.CharField(max_length=300, null=True)
    vendor_site_code = models.CharField(max_length=300, null=True)
    kode_category = models.CharField(max_length=300, null=True)
    kategory_name = models.CharField(max_length=300, null=True)
    harga = models.BigIntegerField(default=0, null=True)
    cogm = models.BigIntegerField(default=0, null=True)
    vendor_id = models.CharField(max_length=300, null=True)
    last_update_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    quantity_delivery = models.BigIntegerField(default=0, null=True) 
    promised_date = models.DateField(null=True, blank=True)
    transaction_date = models.DateField(null=True, blank=True)   
    class Meta:
        app_label   = 'apps_vendor_management'
        db_table    = 'v_data_io_oracle'
        managed = False

class V_PlmSetup(models.Model):
    supplier_id  = models.IntegerField(default=0, null=True, blank=True)
    supplier_name = models.CharField(max_length=300, null=True, blank=True)
    supplier_code = models.CharField(max_length=300, null=True, blank=True)
    supplier_type = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    modify_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    het = models.CharField( max_length=50, null=True, blank=True)
    qty = models.CharField( max_length=50, null=True, blank=True)
    cogm = models.CharField( max_length=50, null=True, blank=True)
    article= models.CharField( max_length=50, null=True, blank=True)
    category = models.CharField( max_length=50, null=True, blank=True)
    prod_year = models.CharField( max_length=50, null=True, blank=True)
    prod_month = models.CharField( max_length=50, null=True, blank=True)
    created_date_gmdetail = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    product_development_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'v_garment_mkt_vendor_mgt'
        managed = False