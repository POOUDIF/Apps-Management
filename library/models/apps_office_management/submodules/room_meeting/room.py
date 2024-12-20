from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid

class RoomMasterRoom(models.Model):
    code = models.CharField(max_length=100, blank=False, null=True)
    room_name      = models.CharField(max_length=100, blank=False, null=False, unique=True)
    room_desc      = models.TextField(blank=True, null=True)
    status         = models.BooleanField(default=True)
    created_by     = models.CharField(max_length=50, null=True)
    created_at     = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by     = models.CharField(max_length=50, null=True)
    updated_at     = models.DateTimeField(auto_now_add=True, editable=True)
    deleted_by     = models.CharField(max_length=50, null=True)
    deleted_at     = models.DateTimeField(auto_now_add=True, editable=True)
     
    class Meta:
        app_label = 'apps_office_management'
        db_table = 'room_master_room' 
    