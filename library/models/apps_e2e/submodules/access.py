from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class E2EApplicationPages(models.Model):
    OPT_ICON        = (('ri-archive-line', 'ri-archive-line'),('ri-archive-stack-line', 'ri-archive-stack-line'),('ri-terminal-window-line','ri-terminal-window-line'),('ri-article-line', 'ri-article-line'),('ri-archive-drawer-line', 'ri-archive-drawer-line'))
    app_code        = models.CharField(max_length=50)
    page_code       = models.CharField(max_length=50)
    name            = models.CharField(max_length=200)
    route           = models.CharField(max_length=200, help_text='# for parent page')
    parent_page     = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, help_text='null for single page and parent page')
    icon            = models.CharField(max_length=250, choices=OPT_ICON, default = 'flaticon-home')
    page_order      = models.IntegerField(blank=True, null=True)
    is_menu         = models.BooleanField(default=False)
    description     = models.TextField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'pages_app'
        ordering    = ['page_order','app_code', 'page_code']
        verbose_name        = 'E2E - Application page'
        verbose_name_plural = 'E2E - Application pages'
    def __str__(self):
        return '(%s) %s -- %s'%(self.app_code, self.page_code, self.name)

class E2EApplicationPageConfig(models.Model):
    access_name     = models.CharField(max_length=200)
    page            = models.ForeignKey(E2EApplicationPages, on_delete=models.CASCADE)
    description     = models.TextField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'page_config'
        ordering    = ['page', 'access_name']
        verbose_name        = 'E2E - Application page config'
        verbose_name_plural = 'E2E - Application pages config'
    def __str__(self):
        return '(%s) %s -- %s'%(self.page, self.access_name, self.description)

class E2EAccessRightConfig(models.Model):
    access_name     = models.CharField(max_length=50)
    page            = models.ForeignKey(E2EApplicationPages, on_delete=models.CASCADE)
    access_right    = models.CharField(max_length=500)

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'access_right'
        ordering    = ['page', 'access_name','access_right']
        verbose_name        = 'E2E - Access right'
        verbose_name_plural = 'E2E - Access right'
    def __str__(self):
        return '(%s) %s -- %s'%(self.page, self.access_name, self.access_right)

class V_AccessRight(models.Model):
    access_name     = models.CharField(max_length=50, blank=True, null=True)
    page_code       = models.CharField(max_length=100, blank=True, null=True)
    access_right    = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'v_access_right'
        managed     = False

class V_ApplicationPages(models.Model):
    access_name     = models.CharField(max_length=50)
    app_code        = models.CharField(max_length=50)
    page_code       = models.CharField(max_length=50)
    name            = models.CharField(max_length=200)
    route           = models.CharField(max_length=200)
    parent_page     = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    icon            = models.CharField(max_length=250)
    page_order      = models.IntegerField(blank=True, null=True)
    is_menu         = models.BooleanField(default=False)
    description     = models.TextField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'v_application_list'
        managed     = False