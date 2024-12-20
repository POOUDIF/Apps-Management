from django.db import models, connection

class AppsMaster(models.Model):
    vendor_id = models.BigIntegerField(primary_key=True)
    last_update_date = models.DateTimeField(auto_now_add=True, blank=True) 
    last_updated_by = models.BigIntegerField(blank=True) 
    vendor_name = models.CharField(max_length=300, null=True)
    summary_flag = models.CharField(max_length=300, null=True)
    vendor_type_disp= models.CharField(max_length=300, null=True)
    attribute2 = models.CharField(max_length=300, null=True)
    class Meta:
        app_label   = 'apps_master'
        db_table    = 'm_supplier'
        managed     = False

class AppsMasterCategory(models.Model):
    name = models.CharField(max_length=300, null=True)
    brand_id = models.BigIntegerField(null=True, blank=True, default=0)
    code = models.CharField(max_length=300, null=True)
    create_uid = models.BigIntegerField(null=True, blank=True, default=0)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    write_uid = models.DateTimeField(auto_now_add=True, blank=True)
    length = models.DateTimeField(auto_now_add=True, blank=True)
    width = models.DateTimeField(auto_now_add=True, blank=True)
    height = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        app_label   = 'apps_master'
        db_table    = 'm_category'
        managed     = False

class AppsMasterBrand(models.Model):
    name = models.CharField(max_length=300, null=True)
    code = models.CharField(max_length=300, null=True)
    responsible_id = models.BigIntegerField(null=True, blank=True, default=0)
    create_uid = models.BigIntegerField(null=True, blank=True, default=0)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    write_uid = models.DateTimeField(auto_now_add=True, blank=True)
    split_voucer = models.BooleanField(default=True)
    class Meta:
        app_label   = 'apps_master'
        db_table    = 'm_brand'
        managed     = False

class AppsMasterRetur(models.Model):
    ware_source = models.CharField(max_length=300, null=True)
    ware_destination = models.CharField(max_length=300, null=True)
    code_ws = models.CharField(max_length=300, null=True)
    date_done = models.DateTimeField(auto_now_add=True, blank=True)
    qty = models.BigIntegerField(null=True, blank=True, default=0)

    class Meta:
        app_label   = 'apps_master'
        db_table    = 'v_m_retur_qty'
        managed     = False
        # unique_together = (('ware_source', 'ware_destination', 'code_ws', 'date_done'),)
    # def get_data_since(last_update):
    #     with connection.cursor() as cursor:
    #         cursor.execute("""SELECT ware_source, ware_destination, code_ws, date_done, qty FROM m_retur_qty WHERE date_done > %s """, [last_update])
    #         return cursor.fetchall()
        
