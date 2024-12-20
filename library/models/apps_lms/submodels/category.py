from django.db import models
from datetime import date,datetime, timedelta


class Category(models.Model):
    code        = models.CharField(max_length=5,null=True,default=None)
    name        = models.CharField(max_length=300)
    created_by  = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=50,null=True,default=None)
    modified_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_by  = models.CharField(max_length=50,null=True,default=None)
    deleted_at  = models.DateTimeField(null=True,default=None)
    pic_dept_id = models.IntegerField(max_length=300,null=True,default=None)
    pic_dept = models.CharField(max_length=300,null=True,default=None)
    transaction = models.CharField(max_length=300,null=True,default=None)

    class Meta:
        app_label  = 'apps_lms'
        db_table   = 'category'

