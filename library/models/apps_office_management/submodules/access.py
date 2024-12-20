from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid

    
class OfcMgtApplicationPages(models.Model):
    OPT_ICON        = (('ri-archive-line', 'ri-archive-line'),('ri-archive-stack-line', 'ri-archive-stack-line'),('ri-terminal-window-line','ri-terminal-window-line'),('ri-article-line', 'ri-article-line'),('ri-archive-drawer-line', 'ri-archive-drawer-line'),('flaticon-add','flaticon-add '), ('flaticon-agenda','flaticon-agenda '),('flaticon-app','flaticon-app '),('flaticon-archive','flaticon-archive '),('flaticon-attachment','flaticon-attachment '),('flaticon-bookmark','flaticon-bookmark '),('flaticon-briefcase','flaticon-briefcase '),('flaticon-calendar','flaticon-calendar '),('flaticon-database','flaticon-database '),('flaticon-document','flaticon-document '),('flaticon-download','flaticon-download '),('flaticon-file','flaticon-file '),('flaticon-folder','flaticon-folder '),('flaticon-id-card','flaticon-id-card '),('flaticon-layers','flaticon-layers '),('flaticon-login','flaticon-login '),('flaticon-menu','flaticon-menu '),('flaticon-navigation','flaticon-navigation '),('flaticon-network','flaticon-network '),('flaticon-photo-camera','flaticon-photo-camera '),('flaticon-picture','flaticon-picture '),('flaticon-print','flaticon-print '),('flaticon-reading','flaticon-reading '),('flaticon-save','flaticon-save '),('flaticon-search','flaticon-search '),('flaticon-send','flaticon-send '),('flaticon-server','flaticon-server '),('flaticon-settings','flaticon-settings '),('flaticon-share','flaticon-share '),('flaticon-sign','flaticon-sign '),('flaticon-time','flaticon-time '),('flaticon-upload','flaticon-upload '),('flaticon-user','flaticon-user '),('flaticon-view','flaticon-view '),('flaticon-wifi','flaticon-wifi '),('flaticon-windows','flaticon-windows '),('flaticon-worldwide','flaticon-worldwide '),('flaticon-zoom-in','flaticon-zoom-in '),('flaticon-zoom-out','flaticon-zoom-out '))
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
        app_label   = 'apps_office_management'
        db_table    = 'pages_app'
        ordering    = ['page_order','app_code', 'page_code']
        verbose_name        = 'Book Room - Application page'
        verbose_name_plural = 'Book Room - Application pages'
    def __str__(self):
        return '(%s) %s -- %s'%(self.app_code, self.page_code, self.name)

class OfcMgtApplicationPageConfig(models.Model):
    access_name     = models.CharField(max_length=200)
    page            = models.ForeignKey(OfcMgtApplicationPages, on_delete=models.CASCADE)
    description     = models.TextField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_office_management'
        db_table    = 'page_config'
        ordering    = ['page', 'access_name']
        verbose_name        = 'Book Room - Application page config'
        verbose_name_plural = 'Book Room - Application pages config'
    def __str__(self):
        return '(%s) %s -- %s'%(self.page, self.access_name, self.description)

class OfcMgtAccessRightConfig(models.Model):
    access_name     = models.CharField(max_length=50)
    page            = models.ForeignKey(OfcMgtApplicationPages, on_delete=models.CASCADE)
    access_right    = models.CharField(max_length=500)

    class Meta:
        app_label   = 'apps_office_management'
        db_table    = 'access_right'
        ordering    = ['page', 'access_name','access_right']
        verbose_name        = 'Book Room - Access right'
        verbose_name_plural = 'Book Room - Access right'
    def __str__(self):
        return '(%s) %s -- %s'%(self.page, self.access_name, self.access_right)

class V_OfcMgtAccessRight(models.Model):
    access_name     = models.CharField(max_length=50, blank=True, null=True)
    page_code       = models.CharField(max_length=100, blank=True, null=True)
    access_right    = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        app_label   = 'apps_office_management'
        db_table    = 'v_access_right'
        managed     = False

class V_OfcMgtApplicationPages(models.Model):
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
        app_label   = 'apps_office_management'
        db_table    = 'v_pages_app'
        managed     = False