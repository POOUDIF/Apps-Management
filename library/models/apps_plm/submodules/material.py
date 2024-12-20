from datetime import date
from email.policy import default
from re import M
from django.db import models
from django.utils import timezone

from library.models.apps_plm.submodules.prodev_v2 import ProductMaterialV2

from .base import *
from .master import *




# class MaterialDevelopment(models.Model):
#     material_id         = models.IntegerField()
#     date                = models.DateTimeField(auto_now_add=True,null=True)
#     activity            = models.ForeignKey(ProductMasterParam, on_delete=models.CASCADE)
#     user                = models.CharField(max_length=50,null=True)
#     remark              = models.CharField(max_length=50,null=True)
#     comment             = models.TextField(null=True)
#     next_value          = models.IntegerField(default=99)

#     class Meta:
#         db_table    = 'product_material_development'

class MaterialDevelopment(models.Model):
    # material            = models.ForeignKey(MasterMaterial,on_delete=models.CASCADE)
    product_material    = models.ForeignKey(ProductMaterialV2,on_delete=models.CASCADE)
    code                = models.CharField(max_length=20)
    supplier_id         = models.IntegerField()
    supplier_name       = models.CharField(max_length=50)
    supplier_code       = models.CharField(max_length=50)
    status              = models.CharField(max_length=50)
    reference           = models.CharField(max_length=100, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'material_development'

class V_MaterialDevelopment(models.Model):
    material_id = models.IntegerField()
    code        = models.CharField(max_length=50,null=True)
    brand       = models.CharField(max_length=50,null=True)
    type        = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    color       = models.CharField(max_length=50,null=True)
    category    = models.CharField(max_length=50,null=True)
    status      = models.CharField(max_length=50,null=True)
    is_active   = models.BooleanField()
    supplier    = models.CharField(max_length=50,null=True)
    img_id      = models.IntegerField()
    img_src     = models.ImageField()
    img_name    = models.TextField(null=True)
    img_code    = models.TextField(null=True)
    img_label   = models.TextField(null=True)
    detail      = models.CharField(max_length=50,null=True)
    used_as     = models.CharField(max_length=50,null=True)
    product_id  = models.IntegerField()
    product_master_id = models.IntegerField()
    product_material_status =  models.CharField(max_length=50,null=True)
    is_process =  models.CharField(max_length=50,null=True)
    article =  models.CharField(max_length=50,null=True)
    coll_month  = models.CharField(max_length=50,null=True)
    is_status      = models.CharField(max_length=50,null=True)


    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_dev_dashboard'

class V_MaterialDevelopmentDetail(models.Model):
    code            = models.CharField(max_length=50)
    # material_id     = models.IntegerField()
    product_material_id= models.IntegerField()
    status          = models.CharField(max_length=50)
    supplier_id     = models.IntegerField()
    supplier_name   = models.CharField(max_length=50)
    supplier_code   = models.CharField(max_length=50)
    activity        = models.CharField(max_length=50)
    date            = models.DateTimeField()
    reference       = models.CharField(max_length=50)


    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_dev_detail'

class V_MaterialDevelopmentActivity(models.Model):
    activity        = models.CharField(max_length=100,null=True)
    activity_value  = models.CharField(max_length=100,null=True)
    date            = models.DateTimeField(auto_now_add=True,null=True)
    activity_id     = models.IntegerField(null=True)
    user            = models.CharField(max_length=50,null=True)
    remark          = models.CharField(max_length=50,null=True)
    comment         = models.TextField(null=True)
    material_values = models.TextField(null=True)
    material_dev_id = models.IntegerField()
    next_value      = models.IntegerField(null=True)
    product_id      = models.IntegerField()
    code            = models.CharField(max_length=50)
    supplier_name   = models.CharField(max_length=50)
    category        = models.CharField(max_length=50)
    status_comment_designer  = models.TextField(null=True)
    count_sample_comment = models.CharField(max_length=150)
    file_name = models.CharField(max_length=150)
    file_src = models.CharField(max_length=150)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_dev_activity'

class MaterialDevelopmentActivity(models.Model):
    # material_id         = models.IntegerField()
    material_dev        = models.ForeignKey(MaterialDevelopment,on_delete=models.CASCADE)
    date                = models.DateTimeField(auto_now_add=True,null=True)
    activity            = models.ForeignKey(ProductMasterParam, on_delete=models.CASCADE)
    user                = models.CharField(max_length=50,null=True)
    remark              = models.CharField(max_length=50,null=True)
    comment             = models.TextField(null=True)
    material_values     = models.TextField(null=True)
    next_value          = models.IntegerField(default=99)
    status_comment_designer = models.TextField(null=True)
    count_sample_comment = models.CharField(max_length=150,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'material_development_activity'

class MaterialDevelopmentActivityFile(models.Model):
    activity        = models.ForeignKey(MaterialDevelopmentActivity,on_delete=models.CASCADE)
    file_src        = models.FileField(upload_to='material-development',blank=True, null=True)
    file_name       = models.CharField(max_length=100, null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'material_development_activity_file'


class MaterialChatActivity(models.Model):
    material_development     = models.ForeignKey(MaterialDevelopment,on_delete=models.CASCADE)
    username  = models.CharField(max_length=50)
    message   = models.TextField(null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    status    = models.CharField(max_length=50,null=True)
    fullname  = models.CharField(max_length=100,null=True)
    role      = models.CharField(max_length=100,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'material_chat_activity'


#matdev models version 2
class V_MaterialDevelopment_V2(models.Model):
    material_id = models.IntegerField()
    code        = models.CharField(max_length=50,null=True)
    brand       = models.CharField(max_length=50,null=True)
    type        = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    color       = models.CharField(max_length=50,null=True)
    category    = models.CharField(max_length=50,null=True)
    status      = models.CharField(max_length=50,null=True)
    is_active   = models.BooleanField()
    supplier    = models.CharField(max_length=50,null=True)
    img_id      = models.IntegerField()
    img_src     = models.ImageField()
    img_name    = models.TextField(null=True)
    img_code    = models.TextField(null=True)
    img_label   = models.TextField(null=True)
    detail      = models.CharField(max_length=50,null=True)
    used_as     = models.CharField(max_length=50,null=True)
    product_id  = models.IntegerField()
    product_master_id       = models.IntegerField()
    product_material_status =  models.CharField(max_length=50,null=True)
    article =  models.CharField(max_length=50,null=True)
    color_id =  models.CharField(max_length=50,null=True)
    coll_month  = models.CharField(max_length=50,null=True)
    year  = models.CharField(max_length=50,null=True)
    is_process  = models.CharField(max_length=100, null=True, default='New')
    modified_at = models.DateTimeField(blank=True, null=True)
    product_content_id = models.IntegerField()
    no_style  = models.CharField(max_length=100,null=True)
    prodev_id  = models.IntegerField(null=True)
    size_spec  = models.IntegerField(null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_dev_dashboard_v2'



class V_MaterialDevelopmentTechpack_V2(models.Model):
    material_id = models.IntegerField()
    code        = models.CharField(max_length=50,null=True)
    brand       = models.CharField(max_length=50,null=True)
    type        = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    color       = models.CharField(max_length=50,null=True)
    category    = models.CharField(max_length=50,null=True)
    status      = models.CharField(max_length=50,null=True)
    is_active   = models.BooleanField()
    supplier    = models.CharField(max_length=50,null=True)
    img_id      = models.IntegerField()
    img_src     = models.ImageField()
    img_name    = models.TextField(null=True)
    img_code    = models.TextField(null=True)
    img_label   = models.TextField(null=True)
    detail      = models.CharField(max_length=50,null=True)
    used_as     = models.CharField(max_length=50,null=True)
    product_id  = models.IntegerField()
    product_master_id = models.IntegerField()
    product_material_status =  models.CharField(max_length=50,null=True)
    article =  models.CharField(max_length=50,null=True)
    color_id =  models.CharField(max_length=50,null=True)
    coll_month  = models.CharField(max_length=50,null=True)
    is_process  = models.CharField(max_length=100, null=True, default='New')
    modified_at = models.DateTimeField(blank=True, null=True)
    id_material_development   = models.CharField(max_length=300,null=True)
    supplier_name   = models.CharField(max_length=300,null=True)
    prodev_id  = models.IntegerField()

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_activity_detail_v2'



class V_MaterialDevelopmentActivityFile_V2(models.Model):
    activity_id = models.IntegerField()
    file_src    = models.CharField(max_length=150,null=True)
    file_name   = models.CharField(max_length=150,null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_material_activity_file_v2'