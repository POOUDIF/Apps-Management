from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from ..room_meeting.room import RoomMasterRoom
import os
import uuid


class RoomBook(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    user_nik = models.CharField(max_length=10, null=True, blank=True)
    user_data = models.CharField(max_length=100, null=True, blank=True)
    user_mail = models.CharField(max_length=100, null=True, blank=True)
    dept_name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    room = models.ForeignKey(RoomMasterRoom, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.CharField(max_length=50, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    deleted_by = models.CharField(max_length=50, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, editable=True)
    class Meta:
        app_label = 'apps_office_management'
        db_table = 'room_book'

class RoomSwitchBook(models.Model):
    code = models.CharField(max_length=10, unique=True)
    requester_nik = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    requester_data = models.CharField(max_length=100, null=True, blank=True)
    requester_mail = models.CharField(max_length=100, null=True, blank=True)
    requester_nik_to = models.CharField(max_length=10, null=True, blank=True)
    requester_data_to = models.CharField(max_length=100, null=True, blank=True)
    to = models.CharField(max_length=300, null=True, blank=True)
    cc = models.CharField(max_length=300, null=True, blank=True)
    dept_name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=10, null=True, blank=True)
    book_id = models.IntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.CharField(max_length=50, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)
    deleted_by = models.CharField(max_length=50, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, editable=True)
    class Meta:
        app_label = 'apps_office_management'
        db_table = 'room_switch_book'