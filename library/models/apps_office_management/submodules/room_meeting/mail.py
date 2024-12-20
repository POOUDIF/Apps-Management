from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid

class RoomBookMail(models.Model):
    name = models.CharField(max_length=100, default=None, null=True)
    code = models.CharField(max_length=50, default=None, null=True)
    to = models.CharField(max_length=300, default=None, null=True)
    cc = models.CharField(max_length=300, default=None, null=True)
    status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label  = 'apps_office_management'
        db_table   = 'room_mail'