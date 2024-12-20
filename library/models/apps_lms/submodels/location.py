from django.db import models
from django.utils import timezone

class Location(models.Model):
    location_name   = models.CharField(max_length=300)
    business_unit   = models.CharField(max_length=50)
    is_active       = models.BooleanField(default=True)
    created_by      = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=50,null=True)
    modified_at     = models.DateTimeField(auto_now_add=True,null=True)
    deleted_by      = models.CharField(max_length=50,null=True)
    deleted_at      = models.DateTimeField(null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'location'