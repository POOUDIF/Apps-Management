from django.db import models

class Direksi(models.Model):
    direksi_name        = models.CharField(max_length=300)
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_by          = models.CharField(max_length=50,null=True,default=None)
    updated_at          = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_by          = models.CharField(max_length=50,null=True,default=None)
    deleted_at          = models.DateTimeField(null=True,default=None)
    is_active           = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'direksi'

class LegalDireksiPIC(models.Model):
    nik             = models.CharField(max_length=20, blank=True, null=True)
    cc              = models.BooleanField(blank=True, null=True)
    direksi_id        = models.IntegerField(blank=True, null=True)
    email           = models.CharField(max_length=150, blank=True, null=True)
    jabatan         = models.CharField(max_length=100, blank=True, null=True)
    jabatan_detail  = models.CharField(max_length=100, blank=True, null=True)
    created_by      = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_by      = models.CharField(max_length=100, blank=True, null=True)
    updated_at      = models.DateTimeField(blank=True, null=True)
    deleted_by      = models.CharField(max_length=100, blank=True, null=True)
    deleted_at      = models.DateTimeField(blank=True, null=True)
    is_active       = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'legal_direksi_pic'