from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

from library.models.bbicore import BaseModel


class CustomConfig(BaseModel):
    OPT_CONDITION = [('BYPASS HEALTH_HISTORY_V2', 'BYPASS_LIMIT HEALTH_HISTORY_V2')]
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    module_code = models.CharField(max_length=100, null=True, blank=True)
    name        = models.CharField(max_length=100, choices=OPT_CONDITION)
    date_start  = models.DateField(default=timezone.now)
    date_end    = models.DateField(default=timezone.now, blank=True, null=True)
    
    class Meta:
        app_label   = 'bbicore'
        db_table    = 'custom_config'
        verbose_name        = 'Form Config - Custom Config'
        verbose_name_plural = 'Form Config - Custom Config'