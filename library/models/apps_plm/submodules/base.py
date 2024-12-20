from django.db import models
from django.db.models import fields, indexes
from django.db.models.deletion import CASCADE
from django.utils import timezone

from library.models.apps_plm.submodules.prodev_v2 import ProductDevelopmentV2
from .master import *
from library.models.bbicore.submodels.base import BaseModelApps


# Create your models here.
class todolistActivity(models.Model):
    id_transaction      = models.CharField(max_length=100,null=True)
    prodev              = models.CharField(max_length=100,null=True)
    no_style            = models.CharField(max_length=100,null=True)
    brand               = models.CharField(max_length=100,null=True)
    activity            = models.CharField(max_length=300,null=True)
    link                = models.CharField(max_length=300,null=True)
    position            = models.CharField(max_length=100,null=True)
    modul               = models.CharField(max_length=100,null=True)
    status              = models.CharField(max_length=100,null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        app_label       = 'apps_plm'
        db_table        = 'todolist_activity'

class HistorytodolistActivity(models.Model):
    todo_list           = models.ForeignKey(todolistActivity,on_delete=models.CASCADE)
    created_by          = models.CharField(max_length=100,null=True)
    action              = models.CharField(max_length=100,null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True) 
    modified_at         = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        app_label       = 'apps_plm'
        db_table        = 'history_todolist_activity'

class settingNotification(models.Model):
    profile_name_notif  = models.CharField(max_length=100)
    template_name_notif = models.CharField(max_length=100)
    title_notif         = models.CharField(max_length=100)
    brand               = models.CharField(max_length=100)
    position            = models.CharField(max_length=100)
    modul               = models.CharField(max_length=100)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        app_label       = 'apps_plm'
        db_table        = 'setting_notification'
       
class ProductMasterParam(models.Model):
    category            = models.CharField(max_length=100)
    name                = models.CharField(max_length=100)
    value               = models.CharField(max_length=100)
    description         = models.TextField(null=True,blank=True)
    parent              = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='child')

    class Meta:
        app_label   = 'apps_plm'
        db_table        = 'product_masterparam'

class ProductProcess(models.Model):
    product             = models.ForeignKey(ProductDevelopmentV2,on_delete=models.CASCADE)
    process             = models.CharField(max_length=100)
    task                = models.CharField(max_length=100)
    start_date          = models.DateField(auto_now_add=True)
    end_date            = models.DateField(null=True,default=None,blank=True)
    estimate_date       = models.DateField(null=True,default=None,blank=True)
    status              = models.CharField(max_length=50,default='On Progress')

    class Meta:
        app_label   = 'apps_plm'
        db_table        = 'product_process'
        indexes         = [
            models.Index(fields=['product']),
        ]


class ParameterApprover(models.Model):
    brand               = models.CharField(max_length=50, null=True)
    name                = models.CharField(max_length=50, null=True)
    position            = models.CharField(max_length=50, null=True)
    nik                 = models.CharField(max_length=50,null=True)
    pos_level           = models.IntegerField(null=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table        = 'parameter_approver'


class ParameterPIC(models.Model):
    DESIGNER_HEAD = 'Designer Head'
    MD = 'MD'
    DESIGNER  = 'Designer'
    MD_DEPT_HEAD = 'MD Dept Head'
    BRAND_MANAGER = 'Brand Manager'
    SUB_DIVISION_HEAD = 'Sub Division Head'
    DIVISION_HEAD_MARKETING = 'Division Head Marketing'
    SUPER_USER = 'Super User'
    TECHNICAL = 'Technical'
    NONE = '--'
    CHOICES_STATUS = (
        (DESIGNER_HEAD, DESIGNER_HEAD),
        (MD, 'MD'),
        (DESIGNER, 'Designer'),
        (MD_DEPT_HEAD, 'MD Dept Head'),
        (BRAND_MANAGER, 'Brand Manager'),
        (SUB_DIVISION_HEAD, 'Sub Division Head'),
        (DIVISION_HEAD_MARKETING, 'Division Head Marketing'),
        (TECHNICAL, 'Technical'),
        (NONE, '--')
    )

    brand               = models.CharField(max_length=50, null=True)
    name                = models.CharField(max_length=50, null=True)
    position            = models.CharField(max_length=50, null=True, choices=CHOICES_STATUS, default=NONE)
    nik                 = models.CharField(max_length=50,null=True)
    isActive            = models.BooleanField(default=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table        = 'parameter_pic'
        ordering    = ['brand', 'position']
        verbose_name        = 'Plm - Parameter PIC'
        verbose_name_plural = 'Plm - Parameter PIC'
    def __str__(self):
        return '(%s) %s -- %s'%(self.brand, self.name, self.position)
    

class Report(models.Model):
    id_article               = models.IntegerField()
    style                    = models.CharField(max_length=100)
    article                  = models.CharField(max_length=100)
    input_prodev             = models.DateField(null=True,default=None,blank=True)
    approve_prodev           = models.DateField(null=True,default=None,blank=True)
    receive_sample_material  = models.DateField(null=True,default=None,blank=True)
    estimate_costing         = models.DateField(null=True,default=None,blank=True)
    receive_sample_garment   = models.DateField(null=True,default=None,blank=True)
    upload_size_spec         = models.DateField(null=True,default=None,blank=True)
    final_costing            = models.DateField(null=True,default=None,blank=True)
    buying                   = models.DateField(null=True,default=None,blank=True)
    create_date              = models.DateField(auto_now_add=True, blank=True)
    update_date              = models.DateField(null=True,default=None,blank=True)

    class Meta:
        app_label   = 'apps_plm'
        db_table        = 'report'


class V_user_activity(models.Model):
    prodev              = models.CharField(max_length=100, null=True)
    no_style            = models.CharField(max_length=100, null=True)
    brand               = models.CharField(max_length=100, null=True)
    activity            = models.CharField(max_length=100, null=True)
    position            = models.CharField(max_length=100, null=True)
    modul               = models.CharField(max_length=100, null=True)
    created_by          = models.CharField(max_length=100, null=True)
    created_at          = models.CharField(max_length=100, null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_user_activity'


class V_todo_list_activity(models.Model):
    id_transaction      = models.CharField(max_length=100,null=True)
    prodev              = models.CharField(max_length=100,null=True)
    no_style            = models.CharField(max_length=100,null=True)
    brand               = models.CharField(max_length=100,null=True)
    activity            = models.CharField(max_length=300,null=True)
    link                = models.CharField(max_length=300,null=True)
    position            = models.CharField(max_length=100,null=True)
    modul               = models.CharField(max_length=100,null=True)
    status              = models.CharField(max_length=100,null=True)
    created_at          = models.CharField(max_length=100, null=True)
    modified_at         = models.CharField(max_length=100, null=True)
    status_action       = models.CharField(max_length=100, null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_todo_list_activity'


class V_dashboard_monitoring(models.Model):
    id                  = models.CharField(max_length=100, primary_key=True)
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
    key_feature_english = models.TextField(null=True)
    key_feature_bahasa  = models.TextField(null=True)
    product_description = models.CharField(max_length=100, null=True)
    is_process          = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True)
    modified_at         = models.DateTimeField(auto_now_add=True,null=True)
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
    estimate_quantity   = models.CharField(max_length=50)
    creator_name = models.CharField(max_length=10)
    proto_sample_size = models.CharField(max_length=10)
    product_content_id = models.CharField(max_length=10)
    status_garmentdev = models.CharField(max_length=10)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_dashboard_monitoring'


class FilterManagement(BaseModelApps):
    modul                       = models.CharField(null=True, max_length=100)
    name                        = models.CharField(null=True, max_length=200)
    isActive                    = models.BooleanField(default=True)
    rule                        = models.TextField(null=True)
    id_transaction              = models.IntegerField(null=True)

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'filter_management' 
