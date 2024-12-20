from django.db import models
from django.db.models.base import Model
from django.utils import timezone
import datetime

from rest_framework import status

from .master import *


def get_upload_path(instance, filename):
    return os.path.join(
        "product-{0}/{1}".format(instance.img_label, filename)
    )

class ProductSampleV2(models.Model):
    ref_sample          = models.CharField(max_length=20,null=True)
    old_sample_no       = models.CharField(max_length=20,null=True)
    guidance            = models.CharField(max_length=100,null=True)
    size_spec           = models.IntegerField(null=True)

    class Meta:
        db_table    = 'product_sample_v2'
        app_label   = 'apps_plm'


class ProductDevContentV2(models.Model):
    form_code           = models.CharField(max_length=20)
    creator             = models.CharField(max_length=20)
    creator_name        = models.CharField(max_length=100)
    creator_site        = models.CharField(max_length=50, default='BBI1')
    form_data           = models.TextField(null=True,blank=True)
    created             = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_content_v2'
        indexes     = [
            models.Index(fields=['creator_site']),
        ]


class ProductDevelopmentV2(models.Model):
    product_content     = models.ForeignKey(ProductDevContentV2, on_delete=models.CASCADE)
    code                = models.CharField(max_length=50,null=True)
    status              = models.CharField(max_length=50,null=True)
    date                = models.DateField(null=True)
    duration            = models.CharField(max_length=50,null=True)
    brand               = models.CharField(max_length=50,null=True)
    collection_name     = models.CharField(max_length=100,null=True)
    year                = models.CharField(max_length=4,null=True)
    quartal             = models.CharField(max_length=20,null=True)
    prod_month          = models.CharField(max_length=20,null=True)
    coll_month          = models.CharField(max_length=20,null=True)
    subbrand            = models.CharField(max_length=50,null=True)
    category            = models.CharField(max_length=50,null=True)
    category_detail_id  = models.CharField(max_length=250,null=True)
    category_detail_en  = models.CharField(max_length=250,null=True)
    running_number      = models.IntegerField(null=True)
    no_style            = models.CharField(max_length=100,null=True)
    repeat_sample       = models.CharField(max_length=20,null=True)
    product_sample      = models.ForeignKey(ProductSampleV2, on_delete=models.CASCADE)
    key_feature_english = models.TextField(null=True)
    key_feature_bahasa  = models.TextField(null=True)
    product_description = models.TextField(null=True)
    is_process          = models.CharField(max_length=20,null=True)
    fabric_process      = models.CharField(max_length=5,default='Yes')
    accessories_process = models.CharField(max_length=5,default='TBD')
    thread_process      = models.CharField(max_length=5,default='TBD')
    artwork_process     = models.CharField(max_length=5,default='TBD')
    interlining_process = models.CharField(max_length=5,default='TBD')
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_at         = models.DateTimeField(blank=True, null=True)
    deleted_at          = models.DateTimeField(blank=True, null=True)
    status_garmentdev   = models.CharField(max_length=50,null=True)
    estimate_quantity   = models.CharField(max_length=50,null=True)
    est_qty_article     = models.TextField(blank=True, null=True)
    proto_sample_size   = models.CharField(max_length=50,null=True)
    status_add_cost     = models.BooleanField(default=False)
    workflow            = models.IntegerField(null=True)
    material_composition = models.TextField(null=True)
    weight              = models.FloatField(null=True)
    mkt_id              = models.IntegerField(null=True)
    mkt_sub_brand_id    = models.IntegerField(null=True)
    mkt_category_id     = models.IntegerField(null=True)
    
    class Meta:
        app_label       = 'apps_plm'
        db_table        = 'product_development_v2'


class V_ProductDevDashboardV2(models.Model):
    id                   = models.CharField(max_length=100, primary_key=True)
    duration             = models.CharField(max_length=100, null=True)
    code                 = models.CharField(max_length=100, null=True)
    status               = models.CharField(max_length=100, null=True)
    date                 = models.DateField()
    brand                = models.CharField(max_length=100, null=True)
    collection_name      = models.CharField(max_length=100, null=True)
    year                 = models.CharField(max_length=100, null=True)
    quartal              = models.CharField(max_length=100, null=True)
    prod_month           = models.CharField(max_length=100, null=True)
    coll_month           = models.CharField(max_length=100, null=True)
    subbrand             = models.CharField(max_length=100, null=True)
    category             = models.CharField(max_length=100, null=True)
    category_detail_id   = models.CharField(max_length=200, null=True)
    category_detail_en   = models.CharField(max_length=200, null=True)
    no_style             = models.CharField(max_length=100, null=True)
    repeat_sample        = models.CharField(max_length=100, null=True)
    key_feature_english  = models.TextField(null=True)
    key_feature_bahasa   = models.TextField(null=True)
    product_description  = models.CharField(max_length=100, null=True)
    is_process           = models.CharField(max_length=100, null=True)
    created_at           = models.DateTimeField(auto_now_add=True,null=True)
    modified_at          = models.DateTimeField(auto_now_add=True,null=True)
    sample_id            = models.IntegerField()
    ref_sample           = models.CharField(max_length=50,null=True)
    old_sample_no        = models.CharField(max_length=50,null=True)
    guidance             = models.CharField(max_length=50,null=True)
    size_spec            = models.IntegerField(null=True)
    size_description     = models.CharField(max_length=50,null=True)
    running_number       = models.CharField(max_length=50,null=True)
    fabric_process       = models.CharField(max_length=5)
    accessories_process  = models.CharField(max_length=5)
    thread_process       = models.CharField(max_length=5)
    artwork_process      = models.CharField(max_length=5)
    interlining_process  = models.CharField(max_length=5)
    estimate_quantity    = models.CharField(max_length=50)
    creator_name         = models.CharField(max_length=10)
    proto_sample_size    = models.CharField(max_length=10)
    product_content_id   = models.CharField(max_length=10)
    status_garmentdev    = models.CharField(max_length=10)
    material_composition = models.CharField(max_length=10)
    weight               = models.FloatField()

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_product_dev_dashboard_v2'


class ColorProductDesignV2(models.Model):
    YES = 'yes'
    NO  = 'no'

    CHOICES_STATUS = (
        (YES, 'Yes'),
        (NO, 'No')
    )
    product_dev         = models.ForeignKey(ProductDevelopmentV2, on_delete=models.CASCADE)
    color               = models.CharField(max_length=50,null=True)
    secondary_color     = models.CharField(max_length=150,null=True)
    intensity           = models.CharField(max_length=100,null=True)
    code_intensity      = models.CharField(max_length=100,null=True)
    article             = models.CharField(max_length=100,null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_at         = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted             = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NO)
    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_color_v2'


class ProductMaterialV2(models.Model):
    YES = 'yes'
    NO  = 'no'

    CHOICES_STATUS = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    NEW = 'New'
    IN_PROGRESS = 'In Progress'

    CHOICES_STATUS_MATDEV = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress')
    )

    material            = models.ForeignKey(MasterMaterial, on_delete=models.CASCADE)
    color_product       = models.ForeignKey(ColorProductDesignV2, on_delete=models.CASCADE)
    product_dev         = models.ForeignKey(ProductDevelopmentV2, on_delete=models.CASCADE)
    detail              = models.TextField(null=True)
    parameter           = models.CharField(max_length=100,null=True)
    used_as             = models.CharField(max_length=100, null=True)
    status              = models.CharField(max_length=50, choices=CHOICES_STATUS_MATDEV, default=NEW, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_at         = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted             = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NO)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_material_v2'


class V_ProductMaterialV2(models.Model):
    id                  = models.IntegerField(primary_key=True)
    product_dev_id      = models.IntegerField()
    product_color_id    = models.IntegerField()
    material_id         = models.IntegerField()
    product_material_id = models.IntegerField()
    color               = models.CharField(max_length=100)
    brand               = models.CharField(max_length=100)
    code_intensity      = models.CharField(max_length=100)
    article             = models.CharField(max_length=100)
    material_category   = models.CharField(max_length=100)
    code_material       = models.CharField(max_length=100)
    type                = models.CharField(max_length=100)
    description         = models.CharField(max_length=100)
    detail              = models.TextField()
    used_as             = models.CharField(max_length=100)
    product_material_status = models.CharField(max_length=100)
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
    weaving_type        = models.CharField(max_length=50)
    weight              = models.CharField(max_length=50)
    type_attribute      = models.CharField(max_length=50)
    atribute1           = models.CharField(max_length=50)
    atribute1_value     = models.CharField(max_length=10)
    atribute2           = models.CharField(max_length=50)
    atribute2_value     = models.CharField(max_length=10)
    code_handloom       = models.CharField(max_length=100)
    img_id              = models.IntegerField()
    img_src             = models.ImageField()
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)
    img_label           = models.TextField(null=True)
    modified_at         = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted             = models.CharField(max_length=100)
    parameter           = models.CharField(max_length=100)
    master_material_id  = models.IntegerField()

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_product_material_v2'


class ImagesProductDesignV2(models.Model):
    YES = 'yes'
    NO  = 'no'

    CHOICES_STATUS = (
        (YES, 'Yes'),
        (NO, 'No')
    )
    product_design      = models.ForeignKey(ProductDevelopmentV2, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)
    img_label           = models.TextField(null=True)
    img_detail          = models.TextField(null=True)
    deleted             = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NO)

    class Meta:
        db_table    = 'product_design_images_v2'
        app_label   = 'apps_plm'


class ProductProcessV2(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    process             = models.CharField(max_length=100)
    task                = models.CharField(max_length=100)
    start_date          = models.DateField(auto_now_add=True)
    end_date            = models.DateField(null=True,default=None,blank=True)
    estimate_date       = models.DateField(null=True,default=None,blank=True)
    status              = models.CharField(max_length=50,default='On Progress')

    class Meta:
        app_label       = 'apps_plm'
        db_table        = 'product_process_v2'
        indexes         = [
            models.Index(fields=['product']),
        ]


class V_ProductSampleV2(models.Model):
    sample_id           = models.IntegerField()
    ref_sample          = models.CharField(max_length=50,null=True)
    old_sample_no       = models.CharField(max_length=50,null=True)
    guidance            = models.CharField(max_length=50,null=True)
    size_spec           = models.IntegerField()
    img_id              = models.IntegerField()
    img_src             = models.ImageField(upload_to="product-technical/", blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        managed     = False
        db_table    = 'v_product_sample_v2'
        app_label   = 'apps_plm'


class ProductApprovalV2(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    status              = models.CharField(max_length=50)
    comment             = models.TextField(null=True)
    date                = models.DateTimeField(auto_now_add=True)
    created_by          = models.CharField(max_length=50)

    class Meta:
        db_table        = 'product_approval_v2'
        app_label   = 'apps_plm'


class ProductMaterialApprovalV2(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    product_material    = models.ForeignKey(ProductMaterialV2,on_delete=models.CASCADE)
    status              = models.CharField(max_length=50)
    article             = models.CharField(max_length=50, null=True)
    code                = models.CharField(max_length=50, null=True)
    comment             = models.TextField(null=True)
    date                = models.DateTimeField(auto_now_add=True)
    created_by          = models.CharField(max_length=50)

    class Meta:
        db_table        = 'product_material_approval_v2'
        app_label   = 'apps_plm'


class V_MaterialHistoryV2(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    product_material    = models.ForeignKey(ProductMaterialV2,on_delete=models.CASCADE)
    code                = models.CharField(max_length=50)
    article             = models.CharField(max_length=50)
    category            = models.CharField(max_length=50)
    status              = models.CharField(max_length=50)
    comment             = models.TextField(null=True)
    date                = models.DateTimeField(auto_now_add=True)
    created_by          = models.CharField(max_length=50)

    class Meta:
        managed     = False
        db_table    = 'v_material_history_v2'
        app_label   = 'apps_plm'


class V_Techpack_V2(models.Model):
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
    key_feature_english = models.TextField(null=True)
    key_feature_bahasa  = models.TextField(null=True)
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
    color  = models.CharField(max_length=100,null=True)
    code_intensity  = models.CharField(max_length=100,null=True)
    created_at_color  = models.CharField(max_length=100,null=True)
    modified_at_color  = models.CharField(max_length=100,null=True)
    product_description  = models.CharField(max_length=100,null=True)
    proto_sample_size = models.CharField(max_length=10)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_techpack_v2'


class ImagesProductSampleV2(models.Model):
    product_sample      = models.ForeignKey(ProductSampleV2, on_delete=models.CASCADE)
    img_src             = models.ImageField(upload_to="product-technical/", blank=True, null=True)
    img_name            = models.TextField(null=True)
    img_code            = models.TextField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'product_sample_images_v2'


class ExportProduct(models.Model):
    # id                  = models.IntegerField(null=True)
    style_id            = models.IntegerField(null=True)
    variant_sku         = models.CharField(max_length=100,null=True)
    item_name           = models.TextField(null=True)
    master_brand        = models.CharField(max_length=100,null=True)
    master_category     = models.CharField(max_length=100,null=True)
    option_type         = models.CharField(max_length=100,null=True)
    option_value_1      = models.CharField(max_length=100,null=True)
    weight              = models.IntegerField(null=True)
    dimension_length    = models.IntegerField(null=True)
    dimension_width     = models.IntegerField(null=True)
    dimension_height    = models.IntegerField(null=True)
    size_type           = models.CharField(max_length=100,null=True) 
    regular             = models.CharField(max_length=100,null=True)
    size_type           = models.CharField(max_length=100,null=True)
    description         = models.TextField(null=True)
    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_export_product_forstock'
