from datetime import date
from email import message
from django.db import models
from django.utils import timezone

from  .base import *
from .prodev_v2 import *
from library.models.bbicore.submodels.base import BaseModelApps

class EstimateCost(BaseModelApps):

    garment_dev_id      = models.IntegerField()
    prodev_dev_id       = models.IntegerField()
    item                = models.CharField(max_length=150, null=True)
    cost_value          = models.CharField(max_length=50, null=True)
    is_exclude          = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'estimate_cost'

class V_GarmentDevelopmentActivity(models.Model):
    activity        = models.CharField(max_length=100,null=True)
    activity_value  = models.CharField(max_length=100,null=True)    
    date            = models.DateTimeField(auto_now_add=True,null=True)
    activity_id     = models.IntegerField(null=True)
    user            = models.CharField(max_length=50,null=True)
    remark          = models.CharField(max_length=50,null=True)
    comment         = models.TextField(null=True)
    garment_values  = models.TextField(null=True)
    garment_dev_id  = models.IntegerField()
    next_value      = models.IntegerField(null=True)
    product_id      = models.IntegerField()
    supplier_name   = models.CharField(max_length=50)
    file_src        = models.ImageField()
    file_name       = models.CharField(max_length=50)
    status_comment_designer  = models.TextField(null=True)
    count_sample_comment = models.CharField(max_length=150)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_garment_dev_activity'


class V_GarmentDevDashboard(models.Model):
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
    no_style            = models.CharField(max_length=100, null=True)
    repeat_sample       = models.CharField(max_length=100, null=True)
    proto_sample_size   = models.CharField(max_length=100, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True)
    sample_id           = models.IntegerField()
    ref_sample          = models.CharField(max_length=50,null=True)
    old_sample_no       = models.CharField(max_length=50,null=True)
    guidance            = models.CharField(max_length=50,null=True)
    size_spec           = models.IntegerField(null=True)
    running_number      = models.CharField(max_length=50,null=True)
    fabric_process      = models.CharField(max_length=5)
    accessories_process = models.CharField(max_length=5)
    thread_process      = models.CharField(max_length=5)
    artwork_process     = models.CharField(max_length=5)
    interlining_process = models.CharField(max_length=5)
    img_src             = models.TextField()
    img_code            = models.TextField()
    img_label           = models.TextField()
    status_garment_selection = models.CharField(max_length=100)
    supplier_selection   = models.CharField(max_length=100)
    estimate_quantity    = models.CharField(max_length=100)
    est_qty_article      = models.TextField()
    product_content_id   = models.IntegerField(null=True)
    status_garmentdev    = models.CharField(max_length=100)
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_garment_dev_dashboard'


class V_GarmentDevelopmentDetail(models.Model):
    code            = models.CharField(max_length=50)
    # material_id     = models.IntegerField()
    product_garment_id = models.IntegerField()
    status          = models.CharField(max_length=50)
    supplier_id     = models.IntegerField()
    supplier_name   = models.CharField(max_length=50)
    supplier_code   = models.CharField(max_length=50)
    supplier_type   = models.CharField(max_length=50)
    activity        = models.CharField(max_length=50)
    date            = models.DateTimeField()
    status_approver = models.CharField(max_length=50)
    available_capacity  = models.IntegerField(null=True, blank=True)
    history_price       = models.IntegerField(null=True, blank=True)
    workflow_id         = models.IntegerField(null=True, blank=True)

    
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_garment_dev_detail'

class V_GarmentCostingDetail(models.Model):
    code            = models.CharField(max_length=50)
    # material_id     = models.IntegerField()
    product_garment_id= models.IntegerField()
    status          = models.CharField(max_length=50)
    supplier_id     = models.IntegerField()
    supplier_name   = models.CharField(max_length=50)
    supplier_code   = models.CharField(max_length=50)
    activity        = models.CharField(max_length=50)
    date            = models.DateTimeField()
    cost            = models.CharField(max_length=50)
    status_costing  = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_costing_detail'


class GarmentDevelopment(models.Model):
    CMT = "CMT"
    FOB = "FOB"
    TYPE_CHOICES = [
        (CMT, 'CMT'),
        (FOB, 'FOB'),
    ]

    product_garment     = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    code                = models.CharField(max_length=200)
    supplier_id         = models.IntegerField()
    supplier_name       = models.CharField(max_length=500)
    supplier_code       = models.CharField(max_length=500)
    status              = models.CharField(max_length=50,null=True)
    status_approver     = models.CharField(max_length=50,null=True)
    supplier_type       = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)
    available_capacity  = models.IntegerField(null=True, blank=True)
    history_price       = models.IntegerField(null=True, blank=True)
    workflow_id         = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_development'

class GarmentCosting(models.Model):
    garment_development = models.ForeignKey(GarmentDevelopment,on_delete=models.CASCADE)
    cost = models.CharField(max_length=50, null=True)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    modify_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    state = models.BooleanField(default=False)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_costing'

class GarmentSelection(models.Model):
    product_development = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE,null=True)
    supplier_name = models.CharField(max_length=50,null=True)
    content = models.CharField(max_length=100,null=True)
    comment = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=50,null=True)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    estimate_cost = models.CharField(max_length=50,null=True) 

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_selection'

class GarmentMarketing(models.Model):
    product_development = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE,null=True)
    supplier_name = models.CharField(max_length=50,null=True)
    content = models.TextField(null=True)
    het = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    approver = models.CharField(max_length=50,null=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)
    workflow_id = models.CharField(max_length=50,null=True)
    workflow_id_other = models.CharField(max_length=50,null=True)
    date_approver_cogm = models.DateTimeField(null=True)
    date_approver_het_qty = models.DateTimeField(null=True)
    submit_io =  models.BooleanField(default=False)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_marketing'

class GarmentMarketingDetail(models.Model):
    garment_marketing = models.ForeignKey(GarmentMarketing,on_delete=models.CASCADE,null=True)
    prodev = models.CharField(max_length=50,null=True)
    het = models.CharField(max_length=50,null=True)
    qty = models.CharField(max_length=50,null=True)
    cogm = models.CharField(max_length=50,null=True)
    article = models.CharField(max_length=50,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
  
    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_marketing_detail'

class GarmentMarketingDetailSize(models.Model):
    garment_marketing_detail = models.ForeignKey(GarmentMarketingDetail,on_delete=models.CASCADE,null=True)
    size = models.CharField(max_length=50,null=True)
    ratio = models.CharField(max_length=50,null=True)
    qty = models.CharField(max_length=50,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_marketing_detail_size'
    
class GarmentChatActivity(models.Model):
    garment_development     = models.ForeignKey(GarmentDevelopment,on_delete=models.CASCADE)
    username  = models.CharField(max_length=50)
    message   = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    status    = models.CharField(max_length=50,null=True)
    fullname  = models.CharField(max_length=100,null=True)
    role      = models.CharField(max_length=100,null=True) 

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_chat_activity'

class GarmentDevelopmentActivity(models.Model):

    garment_dev         = models.ForeignKey(GarmentDevelopment,on_delete=models.CASCADE, null=True)
    date                = models.DateTimeField(auto_now_add=True,null=True)
    activity            = models.ForeignKey(ProductMasterParam, on_delete=models.CASCADE,null=True)
    user                = models.CharField(max_length=50,null=True)
    remark              = models.TextField(null=True)
    comment             = models.TextField(null=True)
    garment_values      = models.TextField(null=True)
    next_value          = models.IntegerField(default=99,null=True)
    status_comment_designer = models.TextField(null=True)
    count_sample_comment = models.CharField(max_length=150,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_development_activity'


class GarmentDevelopmentActivityFile(models.Model):
    activity        = models.ForeignKey(GarmentDevelopmentActivity,on_delete=models.CASCADE)
    file_src        = models.FileField(upload_to='garment-development',blank=True, null=True)
    file_name       = models.CharField(max_length=100, null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_development_activity_file'

class GarmentSizeSpec(models.Model):
    product_development = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE,null=True)
    brand           = models.CharField(max_length=50)
    description     = models.TextField(null=True)
    file_src        = models.FileField(upload_to='garment-sizespec-file',blank=True, null=True)
    file_name       = models.CharField(max_length=100, null=True)
    create_date     = models.DateTimeField(auto_now_add=True,null=True)
    modify_date     = models.DateTimeField(auto_now=False, auto_now_add=False)
    no_style        = models.TextField(null=True)

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'garment_size_spec'

class V_GarmentSelection(models.Model):
    no_style            = models.CharField(max_length=100, null=True)
    code                = models.CharField(max_length=100, null=True)
    duration            = models.CharField(max_length=100, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    note                = models.CharField(max_length=100, null=True)
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
    repeat_sample       = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True)
    running_number      = models.CharField(max_length=50,null=True)
    fabric_process      = models.CharField(max_length=5)
    accessories_process = models.CharField(max_length=5)
    thread_process      = models.CharField(max_length=5)
    artwork_process     = models.CharField(max_length=5)
    interlining_process = models.CharField(max_length=5)
    sample_id           = models.IntegerField()
    ref_sample          = models.CharField(max_length=50,null=True)
    old_sample_no       = models.CharField(max_length=50,null=True)
    guidance            = models.CharField(max_length=50,null=True)
    size_spec           = models.IntegerField(null=True)
    supplier_selection  = models.CharField(max_length=100)
    content_garment_selection           = models.CharField(max_length=100)
    status_garment_selection            = models.CharField(max_length=100)
    create_date_garment_selection       = models.CharField(max_length=100)
    comment_garment_selection           = models.CharField(max_length=100)
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_garment_selection'


class V_GarmentMarketing(models.Model):
    no_style            = models.CharField(max_length=100, null=True)
    code                = models.CharField(max_length=100, null=True)
    duration            = models.CharField(max_length=100, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    note                = models.CharField(max_length=100, null=True)
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
    repeat_sample       = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True)
    running_number      = models.CharField(max_length=50,null=True)
    fabric_process      = models.CharField(max_length=5)
    accessories_process = models.CharField(max_length=5)
    thread_process      = models.CharField(max_length=5)
    artwork_process     = models.CharField(max_length=5)
    interlining_process = models.CharField(max_length=5)
    sample_id           = models.IntegerField()
    ref_sample          = models.CharField(max_length=50,null=True)
    old_sample_no       = models.CharField(max_length=50,null=True)
    guidance            = models.CharField(max_length=50,null=True)
    size_spec           = models.IntegerField(null=True)
    supplier_selection  = models.CharField(max_length=100)
    content_garment_selection           = models.CharField(max_length=100)
    status_garment_selection            = models.CharField(max_length=100)
    create_date_garment_selection       = models.CharField(max_length=100)
    comment_garment_selection           = models.CharField(max_length=100)
    het                                 = models.CharField(max_length=100)
    workflow_id                         = models.CharField(max_length=100)
    workflow_id_other                   = models.CharField(max_length=100)
    create_date_garment_marketing       = models.CharField(max_length=100)
    modify_date_garment_marketing       = models.CharField(max_length=100)
    id_garment_marketing                = models.CharField(max_length=100)
    approver_garment_marketing          = models.CharField(max_length=100)
    status_garment_marketing            = models.CharField(max_length=100)
    technical_src                       = models.CharField(max_length=100)
    technical_name                      = models.CharField(max_length=100)
    technical_code                      = models.CharField(max_length=100)
    estimate_quantity                   = models.CharField(max_length=100)
    est_qty_article                     = models.TextField()
    estimate_cost                       = models.CharField(max_length=100)
    proto_sample_size                   = models.CharField(max_length=100)
    submit_io                           = models.CharField(max_length=100)
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_garment_marketing'


class GarmentMarketingRef(BaseModelApps):
    garment_marketing = models.ForeignKey(GarmentMarketing,on_delete=models.CASCADE,null=True)
    reference = models.TextField(null=True)
    index = models.CharField(max_length=100,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'garment_marketing_ref'


class V_ArticleRefPrice(models.Model):
    prodev_id = models.IntegerField()
    no_style = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=500,null=True)
    year = models.CharField(max_length=100,null=True)
    supplier_name = models.CharField(max_length=500,null=True)
    article = models.CharField(max_length=200,null=True)
    cogm = models.CharField(max_length=100,null=True)
    qty = models.CharField(max_length=100,null=True)
    het = models.CharField(max_length=100,null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_article_ref_price'
