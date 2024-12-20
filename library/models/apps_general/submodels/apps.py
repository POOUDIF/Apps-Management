from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class ErrorLog(models.Model):
    app_name            = models.CharField(max_length=200,blank=True, null=True)
    error_log           = models.TextField(blank=True, null=True)
    data_log            = models.TextField(blank=True, null=True)
    url_log             = models.CharField(max_length=200, blank=True, null=True)
    created             = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        app_label   = 'bbicore'
        db_table    = 'error_log'
        indexes = [
            models.Index(fields=['app_name','url_log','created'],),
        ]
