from django.db import models
from django.utils import timezone


# model master level
class Institution(models.Model):
    name            = models.CharField(max_length=100)
    created_by      = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=50,null=True)
    modified_at     = models.DateTimeField(auto_now_add=True,null=True)
    deleted_by      = models.CharField(max_length=50,null=True)
    deleted_at      = models.DateTimeField(null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'institution'