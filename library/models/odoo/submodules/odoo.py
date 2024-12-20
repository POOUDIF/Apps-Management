from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver


class V_DistributionPlan(models.Model):
    id          = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=500, blank=True, null=True)
    brand       = models.CharField(max_length=500, blank=True, null=True)
    category    = models.CharField(max_length=500, blank=True, null=True)
    state    = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        app_label   = 'apps_odoo_addons'
        db_table    = 'v_distribution_plan'
        managed     = False

class V_DistributionPlanDetail(models.Model):
    id          = models.IntegerField(blank=True,null=True)
    picking_id = models.IntegerField(primary_key=True)
    reference = models.CharField(max_length=500,blank=True,null=True)
    schedule_date = models.DateField(blank=True,null=True)
    source_document = models.TextField(blank=True,null=True)
    source_warehouse = models.TextField(blank=True,null=True)
    destination_warehouse = models.IntegerField(blank=True,null=True)
    bound = models.CharField(max_length=500,blank=True,null=True)
    state = models.CharField(max_length=500,blank=True,null=True)
    area = models.CharField(max_length=500,blank=True,null=True)
    batch_name = models.CharField(max_length=500,blank=True,null=True)

    class Meta:
        app_label   = 'apps_odoo_addons'
        db_table    = 'v_distribution_plan_detail'
        managed     = False

class V_StrickerBox(models.Model):
    id          = models.IntegerField(primary_key=True)
    spid = models.IntegerField(blank=True,null=True)
    warehouse_name = models.CharField(max_length=500,blank=True,null=True)
    picking_date = models.DateField(blank=True,null=True)
    brand_name = models.CharField(max_length=500,blank=True,null=True)
    picking_name = models.CharField(max_length=500,blank=True,null=True)
    sku = models.CharField(max_length=500,blank=True,null=True)
    qty = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    class Meta:
        app_label   = 'apps_odoo_addons'
        db_table    = 'v_sticker_box'
        managed     = False
