from django.db import models
from django.utils import timezone
from library.models.bbicore import BaseModelApps

class SizeSpec(models.Model):
    YES = 'yes'
    NO  = 'no'

    CHOICES_REPEAT = (
        (YES, 'Yes'),
        (NO, 'No')
    )

    brand           = models.CharField(max_length=50)
    sub_brand       = models.CharField(max_length=50,null=True)
    category        = models.CharField(max_length=50)
    description     = models.TextField(null=True,default=None)
    size            = models.TextField(null=True,default=None)
    size_detail     = models.TextField(null=True,default=None)
    is_active       = models.BooleanField(default=True)
    status          = models.BooleanField(default=False)
    repeat          = models.CharField(max_length=10, choices=CHOICES_REPEAT, default=NO)
    id_referensi    = models.IntegerField(null=True)
    created_date    = models.DateTimeField(auto_now_add=True,null=True)
    modified_date   = models.DateTimeField(auto_now=True,null=True)
    created_by      = models.CharField(max_length=50,null=True)
    modify_by       = models.CharField(max_length=50,null=True)
    is_size_detail  = models.BooleanField(default=False)
    remark          = models.TextField(null=True,default=None)

    class Meta:
        db_table    = 'size_spec'
        app_label   = 'apps_plm'

class SizeSet(BaseModelApps):
    size_spec         = models.ForeignKey(SizeSpec, on_delete=models.CASCADE)
    prodev_id         = models.CharField(max_length=50)
    description       = models.TextField(null=True,default=None)
    size_code         = models.CharField(max_length=50)
    size_value        = models.CharField(max_length=50)
    tol_plus          = models.FloatField(max_length=50,null=True)
    tol_min           = models.FloatField(max_length=50,null=True)
    actual            = models.FloatField(max_length=50,null=True)
    tol_actual        = models.FloatField(max_length=50,null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table    = 'size_set'

class SizeDetail(models.Model):
    size_spec         = models.ForeignKey(SizeSpec, on_delete=models.CASCADE)
    description       = models.TextField(null=True,default=None)
    size_code         = models.CharField(max_length=50)
    size_value        = models.CharField(max_length=50)
    tol_min_old       = models.CharField(max_length=50,null=True)
    tol_plus_old      = models.CharField(max_length=50,null=True)
    tol_plus          = models.FloatField(max_length=50,null=True)
    tol_min           = models.FloatField(max_length=50,null=True)
    is_sample         = models.BooleanField(default=False)
    created_date      = models.DateTimeField(auto_now_add=True,null=True)
    modified_date     = models.DateTimeField(auto_now=True,null=True)
    created_by        = models.CharField(max_length=50,null=True)
    modify_by         = models.CharField(max_length=50,null=True)

    class Meta:
        db_table    = 'size_detail'
        app_label   = 'apps_plm'

class SizeSample(models.Model):
    size_detail     = models.ForeignKey(SizeDetail, on_delete=models.CASCADE)
    supplier        = models.CharField(max_length=50)
    garment_id      = models.CharField(max_length=50)
    prodev_id       = models.CharField(max_length=50)
    sample          = models.CharField(max_length=50)
    actual          = models.CharField(max_length=50)
    tol_actual      = models.CharField(max_length=50)
    created_date    = models.DateTimeField(auto_now_add=True,null=True)
    modified_date   = models.DateTimeField(auto_now=True,null=True)
    created_by      = models.CharField(max_length=50,null=True)
    modify_by       = models.CharField(max_length=50,null=True)

    class Meta:
        db_table    = 'size_sample'
        app_label   = 'apps_plm'

class SizeRatio(models.Model):
    brand           = models.CharField(max_length=50)
    sub_brand       = models.CharField(max_length=50)
    category        = models.CharField(max_length=50)
    size            = models.TextField(null=True,default=None)
    ratio           = models.FloatField(null=True)
    valid_from      = models.DateTimeField(null=True)
    valid_to        = models.DateTimeField(null=True)

    class Meta:
        db_table    = 'master_size_ratio'
        app_label   = 'apps_plm'


class V_MasterRatioSize(models.Model):
    brand                = models.CharField(max_length=50)
    sub_brand            = models.CharField(max_length=50)
    category             = models.CharField(max_length=50)
    size                 = models.CharField(max_length=50)
    ratio                = models.CharField(max_length=50)
    valid_from           = models.DateTimeField()
    valid_to             =  models.DateTimeField()
    name                 = models.CharField(max_length=50)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_master_size_ratio'

class V_SizeSetDetail(models.Model):
    description         = models.TextField(null=True, blank=True, max_length=100)
    size_code           = models.CharField(null=True, blank=True, max_length=100)
    size_value          = models.CharField(null=True, blank=True, max_length=100)
    tol_min_old         = models.CharField(null=True, blank=True, max_length=100)
    tol_plus_old        = models.CharField(null=True, blank=True, max_length=100)
    tol_plus            = models.CharField(null=True, blank=True, max_length=100)
    tol_min             = models.CharField(null=True, blank=True, max_length=100)
    is_sample           = models.BooleanField(null=True, blank=True)
    created_date        = models.DateTimeField(null=True, blank=True)
    modified_date       = models.DateTimeField(null=True, blank=True)
    created_by          = models.CharField(null=True, blank=True, max_length=100)
    modify_by           = models.CharField(null=True, blank=True, max_length=100)
    size_spec_id        = models.IntegerField(null=True, blank=True)
    no_style            = models.CharField(null=True, blank=True, max_length=100)
    status              = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_size_set_detail'


class V_SizeSetDetailFull(models.Model):
    description         = models.CharField(null=True, blank=True, max_length=200)
    size_code           = models.CharField(null=True, blank=True, max_length=100)
    size_value          = models.CharField(null=True, blank=True, max_length=100)
    tol_plus            = models.CharField(null=True, blank=True, max_length=100)
    tol_min             = models.CharField(null=True, blank=True, max_length=100)
    size_spec_id        = models.IntegerField(null=True, blank=True)
    no_style            = models.CharField(null=True, blank=True, max_length=100)
    status              = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_size_set_full'

