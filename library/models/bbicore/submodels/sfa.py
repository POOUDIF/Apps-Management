from django.db import models
from django.db.models.deletion import CASCADE

class MasterSpg(models.Model):
    nik = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="NO")
    organization_name = models.CharField(max_length=255)
    position = models.CharField(max_length=20)
    position_name = models.CharField(max_length=20)
    job = models.CharField(max_length=100)
    date = models.DateTimeField()
    gender = models.CharField(max_length=2)
    area = models.CharField(max_length=50)
    subarea = models.CharField(max_length=50)

    class Meta:
        managed   = False
        app_label = 'bbicore'
        db_table  = 'v_user_spg'

class LogAssignedSpg(models.Model):
    listLogName = (
        ("CREATED", "CREATED"),
        ("DELETED", "DELETED"),
        ("UPDATED", "UPDATED")
    )
    username = models.CharField(max_length=10)
    log_name = models.CharField(max_length=100,choices=listLogName, default="NO")
    nik_spg = models.CharField(max_length=10)
    is_success = models.BooleanField(default="NO", null=True)
    desc = models.CharField(max_length=255,default="NO", null=True)
    date = models.DateTimeField(editable=False)
    
    class Meta:
        app_label = 'bbicore'
        db_table  = 'log_asgn_spg'

class DepartmentSpg(models.Model):
    department = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'bbicore'
        db_table  = 'v_dept_spg'




    

    