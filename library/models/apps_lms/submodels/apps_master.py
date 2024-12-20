from django.db import models

class AppsMasterCustomer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_code = models.CharField(max_length=30)
    class Meta:
        app_label   = 'apps_master'
        db_table    = 'm_customer'
        managed     = False