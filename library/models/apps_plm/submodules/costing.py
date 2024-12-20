from django.db import models
from django.db.models.deletion import CASCADE
from library.models.bbicore.submodels.base import BaseModelApps
from .prodev_v2 import *

class ProductCosting(models.Model):
    product         = models.ForeignKey(ProductDevelopmentV2,on_delete=CASCADE)
    supplier        = models.CharField(max_length=50)
    est_cost        = models.DecimalField(decimal_places=0,max_digits=9)
    sample_number   = models.CharField(max_length=50)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_costing'

class Costing(BaseModelApps):
    prodev          = models.IntegerField(max_length=100,blank=True,null=True)
    gardev          = models.IntegerField(max_length=100,blank=True,null=True)
    article_ref     = models.CharField(max_length=500,blank=True,null=True)
    price_ref       = models.CharField(max_length=500,blank=True,null=True)
    exp_delivery    = models.DateTimeField(blank=True,null=True)
    opex            = models.IntegerField(max_length=200,blank=True,null=True)
    total           = models.IntegerField(max_length=200,blank=True,null=True)
    barcode_cost    = models.IntegerField(max_length=200,blank=True,null=True)
    total_est_cogm  = models.IntegerField(max_length=200,blank=True,null=True)
    production_unit = models.CharField(max_length=500,blank=True,null=True)
    price_index     = models.IntegerField(max_length=200,blank=True,null=True)
    delivery_date   = models.DateTimeField(blank=True,null=True)
    sample          = models.CharField(max_length=500,blank=True,null=True)
    

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'costing' 

class detailCosting(BaseModelApps):
    costing           = models.ForeignKey(Costing,on_delete=CASCADE)
    type              = models.CharField(max_length=500,blank=True,null=True)
    placement         = models.TextField(blank=True,null=True)
    material_category = models.CharField(max_length=500,blank=True,null=True)
    material_type     = models.CharField(max_length=500,blank=True,null=True)
    description       = models.TextField(blank=True,null=True)
    composition       = models.CharField(max_length=500,blank=True,null=True)
    construction      = models.CharField(max_length=500,blank=True,null=True)
    width             = models.CharField(max_length=500,blank=True,null=True)
    weight            = models.CharField(max_length=500,blank=True,null=True)
    material_price    = models.IntegerField(max_length=200,blank=True,null=True)
    consumption       = models.IntegerField(max_length=200,blank=True,null=True)
    offered_cost      = models.IntegerField(max_length=200,blank=True,null=True)
    supplier          = models.CharField(max_length=500,blank=True,null=True)
    name_article      = models.TextField(blank=True,null=True)
    comments          = models.TextField(blank=True,null=True)
    size              = models.IntegerField(max_length=200,blank=True,null=True)
    position          = models.CharField(max_length=500,blank=True,null=True)
    ref               = models.TextField(blank=True,null=True)
    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'detail_costing'


