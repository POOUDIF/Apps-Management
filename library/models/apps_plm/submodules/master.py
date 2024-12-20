from django.db import models
from django.utils import timezone
import os
from django.contrib.postgres.fields import ArrayField
from library.models.bbicore.submodels.base import BaseModelApps

class TransactionKeyFeature(BaseModelApps):
    article               = models.CharField(max_length=100, null=True)
    brand                 = models.CharField(max_length=100, null=True)
    subbrand              = models.CharField(max_length=200, null=True)
    category_id           = models.TextField(null=True)
    category_en           = models.TextField(null=True)
    color                 = models.CharField(max_length=100, null=True)
    secondary_color       = models.CharField(max_length=100, null=True)
    material_composition  = models.CharField(max_length=100, null=True)
    product_care          = models.TextField(null=True)
    key_feature_id        = models.TextField(null=True)
    key_feature_en        = models.TextField(null=True)
    title_id              = models.TextField(null=True)
    title_en              = models.TextField(null=True)
    product_desc_id       = models.TextField(null=True)
    product_desc_en       = models.TextField(null=True)
    prodev_id             = models.IntegerField(null=True)
    article_id            = models.IntegerField(null=True)
    weight                = models.FloatField(null=True)
    detail_size           = models.TextField(null=True)
    detail_model_size     = models.TextField(null=True)
    is_active             = models.BooleanField(default=True)
    
    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'tr_key_feature'

class MasterWeight(BaseModelApps):
    brand               = models.CharField(max_length=100, null=True)
    subbrand            = models.CharField(max_length=100, null=True)
    category            = models.CharField(max_length=100, null=True)
    weight              = models.IntegerField()
    is_active           = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_weight'

class MasterCost(BaseModelApps):
    brand               = models.CharField(max_length=100, null=True)
    subbrand            = models.CharField(max_length=100, null=True)
    category            = models.CharField(max_length=100, null=True)
    price               = models.IntegerField(max_length=500, null=True)
    is_active           = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_costing'


def get_upload_path_master_label(instance, filename):
    return os.path.join(
        "product-{0}/{1}".format(instance.img_label, filename)
    )

class MasterLabel(BaseModelApps):
    brand               = models.CharField(max_length=100, null=True)
    subbrand            = models.CharField(max_length=100, null=True)
    category            = models.CharField(max_length=100, null=True)
    detail              = models.CharField(max_length=500, null=True)
    img_src             = models.ImageField(upload_to=get_upload_path_master_label,blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)
    img_label           = models.CharField(max_length=500,default='images')
    is_active           = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_label'

class MasterEstimateQty(BaseModelApps):
    brand         = models.CharField(max_length=50)
    sub_brand     = models.CharField(max_length=50)
    category      = models.CharField(max_length=50)
    qty           = models.CharField(max_length=50)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_estimate_qty'

class MasterTolerance(models.Model):
    tolerance           = models.CharField(max_length=50)
    status              = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True)
    created_by          = models.CharField(max_length=50)
    modify_by           = models.CharField(max_length=50)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_tolerance' 


class MasterCheckPoint(models.Model):
    TYPE_CHOICES = [
        ('CMT', 'CMT'),
        ('FOB', 'FOB'),
    ]

    description         = models.TextField()
    brand               = models.CharField(max_length=50)
    sub_brand           = models.TextField()
    category            = models.TextField()
    collection          = models.CharField(max_length=150)
    dept                = models.CharField(max_length=50)
    lead_time           = models.IntegerField()
    lead_time_notif     = models.IntegerField()
    status              = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True)
    created_by          = models.CharField(max_length=50)
    modify_by           = models.CharField(max_length=50)
    step                = models.IntegerField()
    type                = models.CharField(max_length=50,choices=TYPE_CHOICES,null=True,)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_checkpoint'


class MasterSize(BaseModelApps):
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=50)
    sizes               = models.CharField(max_length=50)
    category            = models.CharField(max_length=50)
    status              = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_size'


class MasterMaterial(models.Model):
    YES = 'yes'
    NO  = 'no'

    CHOICES_REPEAT = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    id_type             = models.CharField(max_length=100, null=True)
    description         = models.TextField(null=True,default=None)
    color               = models.CharField(max_length=20,null=True,default=None)
    category            = models.CharField(max_length=20)
    supplier            = models.CharField(max_length=40,null=True,default=None)
    status              = models.CharField(max_length=20)
    is_active           = models.BooleanField(default=True)
    running_number      = models.IntegerField(null=True)
    detail_type         = models.CharField(max_length=100, null=True)
    detail_size         = models.CharField(max_length=100, null=True)
    detail_weight       = models.CharField(max_length=100, null=True)
    repeat              = models.CharField(max_length=10, choices=CHOICES_REPEAT, default=NO)
    id_referensi        = models.IntegerField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_material'

class V_MasterMaterial(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    id_type             = models.CharField(max_length=100)
    description         = models.TextField(null=True)
    color               = models.CharField(max_length=20)
    supplier            = models.CharField(max_length=40)
    category            = models.CharField(max_length=20)
    status              = models.CharField(max_length=20)
    is_active           = models.BooleanField(default=True)
    fabric_id           = models.IntegerField()
    composition         = models.CharField(max_length=100)
    composition_value   = models.CharField(max_length=100)
    yarn_size           = models.CharField(max_length=50)
    width               = models.CharField(max_length=50)
    construction        = models.CharField(max_length=100)
    texture             = models.CharField(max_length=50)
    chemical_finishing  = models.CharField(max_length=50)
    year                = models.CharField(max_length=4)
    month               = models.CharField(max_length=50)
    running_number      = models.IntegerField()
    weaving_type        = models.CharField(max_length=50)
    weight              = models.CharField(max_length=50)
    type_attribute      = models.CharField(max_length=50)
    img_id              = models.IntegerField()
    img_src             = models.ImageField()
    img_name            = models.TextField()
    img_code            = models.TextField()
    material_id         = models.IntegerField()
    atribute1           = models.CharField(max_length=50)
    atribute1_value     = models.CharField(max_length=10)
    atribute2           = models.CharField(max_length=50)
    atribute2_value     = models.CharField(max_length=10)
    code_handloom       = models.CharField(max_length=100)
    detail_size         = models.CharField(max_length=100)
    detail_type         = models.CharField(max_length=100)
    detail_weight       = models.CharField(max_length=100)
    repeat              = models.CharField(max_length=50)
    id_referensi        = models.IntegerField()

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_master_material'


class V_MasterMaterialFabric(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    description         = models.TextField(null=True)
    color               = models.CharField(max_length=20)
    supplier            = models.CharField(max_length=40)
    category            = models.CharField(max_length=20)
    status              = models.CharField(max_length=20)
    is_active           = models.BooleanField(default=True)
    fabric_id           = models.IntegerField()
    composition         = models.CharField(max_length=100)
    composition_value   = models.CharField(max_length=100)
    yarn_size           = models.CharField(max_length=50)
    width               = models.CharField(max_length=50)
    construction        = models.CharField(max_length=100)
    texture             = models.CharField(max_length=50)
    chemical_finishing  = models.CharField(max_length=50)
    year                = models.CharField(max_length=4)
    month               = models.CharField(max_length=50)
    running_number      = models.IntegerField()
    weaving_type        = models.CharField(max_length=50)
    weight              = models.CharField(max_length=50)
    type_attribute      = models.CharField(max_length=50)
    img_id              = models.IntegerField()
    img_src             = models.ImageField()
    img_name            = models.TextField()
    img_code            = models.TextField()
    img_label           = models.TextField()
    # additional_id       = models.IntegerField()
    # additional_src      = models.ImageField()
    # additional_name     = models.CharField(max_length=100, null=True)
    # additional_label    = models.CharField(max_length=100, null=True)
    material_id         = models.IntegerField()
    atribute1           = models.CharField(max_length=50)
    atribute1_value     = models.CharField(max_length=10)
    atribute2           = models.CharField(max_length=50)
    atribute2_value     = models.CharField(max_length=10)
    code_handloom       = models.CharField(max_length=100)
    repeat              = models.CharField(max_length=50)
    id_referensi        = models.IntegerField()

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_master_material_fabric'


def get_upload_path(instance, filename):
    return os.path.join(
        "master-{0}/{1}".format(instance.material.category, filename)
    )

class MasterMaterialImages(models.Model):
    material            = models.ForeignKey(MasterMaterial, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to=get_upload_path,blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)
    img_label           = models.TextField(max_length=500,default='images')

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_material'

class MasterMaterialComponent(models.Model):
    code                = models.CharField(max_length=50)
    category            = models.CharField(max_length=20)
    label_name          = models.CharField(max_length=50)
    label_value         = models.CharField(max_length=100)
    description         = models.TextField()

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_material_component'

class MasterMaterialFabric(models.Model):
    material            = models.ForeignKey(MasterMaterial, on_delete=models.CASCADE)
    composition         = models.CharField(max_length=100,null=True,default=None)
    composition_value   = models.CharField(max_length=50,null=True,default=None)
    yarn_size           = models.CharField(max_length=50,null=True,default=None)
    width               = models.CharField(max_length=50,null=True,default=None)
    construction        = models.CharField(max_length=100,null=True,default=None)
    texture             = models.CharField(max_length=50,null=True,default=None)
    chemical_finishing  = models.CharField(max_length=50,null=True,default=None)
    year                = models.CharField(max_length=4)
    month               = models.CharField(max_length=50)
    running_number      = models.IntegerField(null=True)
    weaving_type        = models.CharField(max_length=50,null=True,default=None)
    weight              = models.CharField(max_length=50)
    atribute1           = models.CharField(max_length=50,null=True,default=None)
    atribute1_value     = models.CharField(max_length=10,null=True,default=None)
    atribute2           = models.CharField(max_length=50,null=True,default=None)
    atribute2_value     = models.CharField(max_length=10,null=True,default=None)
    code_handloom       = models.CharField(max_length=100,null=True,default=None)
    type_attribute      = models.CharField(max_length=50,null=True,default=None)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'master_material_fabric'


class MasterFabric(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    composition         = models.CharField(max_length=100)
    yarn_size           = models.CharField(max_length=50)
    width               = models.CharField(max_length=10)
    construction        = models.CharField(max_length=100)
    texture             = models.CharField(max_length=50)
    chemical_finishing  = models.CharField(max_length=50)
    year                = models.CharField(max_length=4)
    month               = models.CharField(max_length=10)
    running_number      = models.IntegerField()
    weaving_type        = models.CharField(max_length=50)
    description         = models.TextField(null=True)
    weight              = models.CharField(max_length=10)



    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_master_fabric'

class ImagesMasterFabric(models.Model):
    master_fabric       = models.ForeignKey(MasterFabric, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to="product-fabric/",blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_fabric'

class MasterThread(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    description         = models.TextField(null=True)
    color               = models.CharField(max_length=10)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_master_thread'

class ImagesMasterThread(models.Model):
    master_thread       = models.ForeignKey(MasterThread, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to="product-thread/",blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_thread'

class MasterAccessories(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    description         = models.TextField(null=True)
    color               = models.CharField(max_length=10)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_master_accessories'

class ImagesMasterAccessories(models.Model):
    master_accessories      = models.ForeignKey(MasterAccessories, on_delete=models.CASCADE)
    img_src                 = models.ImageField(upload_to="product-accessories/",blank=True, null=True)
    img_name                = models.TextField(null=True)
    img_code                = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_accessories'

class MasterArtwork(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    description         = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_master_artwork'

class ImagesMasterArtwork(models.Model):
    master_artwork       = models.ForeignKey(MasterArtwork, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to="product-artwork/",blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_artwork'

class MasterInterlining(models.Model):
    code                = models.CharField(max_length=50)
    brand               = models.CharField(max_length=50)
    type                = models.CharField(max_length=100)
    description         = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_master_interlining'

class ImagesMasterInterlining(models.Model):
    master_interlining  = models.ForeignKey(MasterInterlining, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to="product-interlining/",blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'images_master_interlining'


class V_MasterSize(models.Model):
    brand                = models.CharField(max_length=50)
    category             = models.CharField(max_length=50)
    sizes                 = models.CharField(max_length=50)
    name                 = models.CharField(max_length=50)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_master_size'
