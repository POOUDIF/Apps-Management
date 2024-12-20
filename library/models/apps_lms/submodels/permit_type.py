from django.db import models
from django.utils import timezone

from .category import Category
from .institution import Institution
from .level import Level


# model master permit_type
class PermitType(models.Model):
    permit_type         = models.CharField(max_length=100)
    expired             = models.CharField(max_length=5)
    category            = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    is_active           = models.BooleanField(default=True)
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    modified_by         = models.CharField(max_length=50,null=True)
    modified_at         = models.DateTimeField(auto_now_add=True,null=True)
    deleted_by          = models.CharField(max_length=50,null=True)
    deleted_at          = models.DateTimeField(null=True)
    end_date            = models.DateField(null=True)
    levels              = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    institution         = models.ForeignKey(Institution,on_delete=models.CASCADE,null=True)
    duration            = models.CharField(max_length=100,null=True)
    reminders           = models.CharField(max_length=100,null=True)
    category_transaction= models.CharField(max_length=100,null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'permit_type'

class V_PermitType(models.Model):
    permit_type         = models.CharField(max_length=100)
    expired             = models.CharField(max_length=5)
    category            = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    institution         = models.ForeignKey(Institution,on_delete=models.CASCADE,null=True)
    levels              = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    is_active           = models.BooleanField(default=True)
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    modified_by         = models.CharField(max_length=50,null=True)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50,null=True)
    deleted_at          = models.DateTimeField(null=True)
    code                = models.CharField(max_length=5)
    # name                = models.CharField(max_length=300)
    name                = models.CharField(max_length=300)
    institution_name    = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    end_date            = models.DateField(null=True)
    duration            = models.IntegerField(null=True,default=None)
    reminders           = models.IntegerField(null=True,default=None)
    pic_dept_id         = models.IntegerField(null=True,default=None)
    department          = models.CharField(max_length=200)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'v_master_permittype'
        managed     = False

class V_PermitType_V2(models.Model):
    permit_type         = models.CharField(max_length=100)
    expired             = models.CharField(max_length=5)
    category            = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    institution         = models.ForeignKey(Institution,on_delete=models.CASCADE,null=True)
    levels              = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    is_active           = models.BooleanField(default=True)
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    modified_by         = models.CharField(max_length=50,null=True)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50,null=True)
    deleted_at          = models.DateTimeField(null=True)
    code                = models.CharField(max_length=5)
    # name                = models.CharField(max_length=300)
    name                = models.CharField(max_length=300)
    institution_name    = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    end_date            = models.DateField(null=True)
    duration            = models.IntegerField(null=True,default=None)
    reminders           = models.IntegerField(null=True,default=None)
    pic_dept_id         = models.IntegerField(null=True,default=None)
    department          = models.CharField(max_length=300)
    category_transaction= models.CharField(max_length=100,null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'v_master_permittype_v2'
        managed     = False


class LMSMasterActivity(models.Model):
    permittype          = models.ForeignKey(PermitType,on_delete=models.CASCADE,null=True)
    activity_name       = models.CharField(max_length=200,null=True, blank=True)
    created_by          = models.CharField(max_length=200,null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    updated_by          = models.CharField(max_length=200,null=True, blank=True)
    updated_at          = models.DateTimeField(auto_now_add=True,editable=True)
    is_active           = models.BooleanField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'lms_master_activity'


class V_LMSMasterActivity(models.Model):
    permittype          = models.ForeignKey(PermitType,on_delete=models.CASCADE,null=True)
    permit_type_name    = models.CharField(max_length=200,null=True, blank=True)
    category_transaction= models.CharField(max_length=200,null=True, blank=True)
    activity_name       = models.CharField(max_length=200,null=True, blank=True)
    created_by          = models.CharField(max_length=200,null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    updated_by          = models.CharField(max_length=200,null=True, blank=True)
    updated_at          = models.DateTimeField(auto_now_add=True,editable=True)
    is_active           = models.BooleanField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'v_lms_master_activity'
        managed     = False


class LMSMasterCategoryTransaction(models.Model):
    category_transaction= models.CharField(max_length=200,null=True, blank=True)
    created_by          = models.CharField(max_length=200,null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    updated_by          = models.CharField(max_length=200,null=True, blank=True)
    updated_at          = models.DateTimeField(auto_now_add=True,editable=True)
    is_active           = models.BooleanField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'lms_master_category_transaction'

class V_LMSMasterCategoryTransaction(models.Model):
    category_transaction= models.CharField(max_length=200,null=True, blank=True)
    created_by          = models.CharField(max_length=200,null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,editable=False)
    updated_by          = models.CharField(max_length=200,null=True, blank=True)
    updated_at          = models.DateTimeField(auto_now_add=True,editable=True)
    is_active           = models.BooleanField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'v_lms_master_category_transaction'
        managed     = False