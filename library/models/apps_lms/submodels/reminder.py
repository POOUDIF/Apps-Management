from django.db import models


from .permit_type import *
from .location import *

class Reminder(models.Model):
    permit          = models.ForeignKey(PermitType, on_delete=models.CASCADE)
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    business_unit   = models.CharField(max_length=50)
    reminder        = models.IntegerField()
    is_status       = models.BooleanField(default=True)
    created_by      = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=50,null=True)
    modified_at     = models.DateTimeField(auto_now_add=True,null=True)
    deleted_by      = models.CharField(max_length=50,null=True)
    deleted_at      = models.DateTimeField(null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'reminder'

class V_Reminder(models.Model):
    permit          = models.ForeignKey(PermitType, on_delete=models.CASCADE)
    permit_type     = models.CharField(max_length=100)
    expired         = models.CharField(max_length=5)
    permit_active   = models.BooleanField()
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_name   = models.CharField(max_length=300)
    location_bu     = models.CharField(max_length=50)
    location_active = models.BooleanField()
    business_unit   = models.CharField(max_length=50)
    reminder        = models.IntegerField()
    is_status       = models.BooleanField()
    created_by      = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=50,null=True)
    modified_at     = models.DateTimeField(null=True)
    deleted_by      = models.CharField(max_length=50,null=True)
    deleted_at      = models.DateTimeField(null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_master_reminder'

