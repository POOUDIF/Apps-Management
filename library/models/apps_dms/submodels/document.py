from django.db import models
import os
# import django_filters
from django.db.models import Q

from django.contrib.auth.models import User
from django.db.models.base import Model
# from bbi.base.models import BaseAPIModel2
from django.core.validators import FileExtensionValidator

from .storage import OverwriteStorage
# from bbi_backend import settings
import filecmp
class FormContentDMS(models.Model):
    form_code           = models.CharField(max_length=20)
    parent_form         = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    creator             = models.CharField(max_length=20)
    creator_name        = models.CharField(max_length=100)
    creator_site        = models.CharField(max_length=50, default='BBI1')
    form_data           = models.TextField(null=True,blank=True)
    created             = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'form_content_dms'
        indexes     = [
            models.Index(fields=['creator_site']),
        ]


def get_file_path(instance, filename):
    if instance.ver_doc is None:
        ver = 0
    else:
        ver = instance.ver_doc
    if instance.rev_doc is None:
        rev = 0 
    else:
        rev = instance.rev_doc
        
    docsName = instance.no_document + "V"+str(ver) +"R"+ str(rev)
    ext = '.' + filename.split('.')[-1]
    remove_char = ["/"]

    for char in remove_char:
        docsName = docsName.replace(char, "-")

    filename    = docsName + ext

    return os.path.join(
        "dms/document-{0}/{1}".format(instance.type_doc, filename)
    )

class FormDMSDocument(models.Model):
    form_content        = models.ForeignKey(FormContentDMS, on_delete=models.CASCADE, null=True, blank=True)
    no_document         = models.CharField(max_length=20)
    title_doc           = models.CharField(max_length=100)
    type_doc            = models.CharField(max_length=20)
    decs_doc            = models.TextField(null=True, blank=True)
    start_date_apply    = models.DateField(null=True, blank=True)
    is_public_doc       = models.BooleanField()
    bu_access           = models.CharField(max_length=20)
    dept_access         = models.CharField(max_length=500)
    posisi_access       = models.CharField(null=True,max_length=500)
    upload_doc          = models.FileField(upload_to=get_file_path, validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpg', 'jpeg', 'png', 'vsd', 'vsdx', 'xls', 'xlsx', 'txt', 'odt', 'vsdm', 'vstx', 'vstm'])])
    status_active       = models.BooleanField()
    parent_document     = models.IntegerField(null=True, blank=True)
    ver_doc             = models.IntegerField(null=True, blank=True)
    parent_rev          = models.IntegerField(null=True, blank=True)
    rev_doc             = models.IntegerField(null=True, blank=True)
    overview_rev        = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'dms_document'
        indexes     = [
            models.Index(fields=['no_document', 'is_public_doc', 'status_active']),
            models.Index(fields=['bu_access', 'dept_access'])
        ]

class FormDocumentLog(models.Model):
    no_document         = models.ForeignKey(FormDMSDocument, on_delete=models.CASCADE, null=True, blank=True)
    doc_id              = models.IntegerField(null=True, blank=True)
    modify_reason       = models.TextField(null=True, blank=True)
    modified_at         = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_by         = models.CharField(max_length=100)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'document_log'
        indexes     = [
            models.Index(fields=['no_document', 'modify_reason', 'modified_at', 'modified_by'])
        ]

class DMSRole(models.Model):
    dms_role_id         = models.IntegerField()
    all_dept            = models.BooleanField(default=False)
    role_name           = models.CharField(max_length=100)
    dept                = models.CharField(max_length=20)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'dms_role'
        indexes     = [
            models.Index(fields=['dms_role_id']),
            models.Index(fields=['all_dept']),
            models.Index(fields=['role_name']),
            models.Index(fields=['dept']),
        ]

class DMSRoleMapping(models.Model):
    nik               = models.CharField(max_length=20)
    dms_role          = models.ForeignKey(DMSRole, on_delete=models.CASCADE)

    def __str__(self):
        return '%s -- %s'%(self.nik, self.dms_role)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'dms_role_mapping'
        indexes     = [
            models.Index(fields=['nik']),
            models.Index(fields=['dms_role_id']),
        ]


class DeptList(models.Model):
    business_unit   = models.CharField(max_length=20)
    dept_code       = models.CharField(max_length=20)
    dept_name       = models.CharField(max_length=20)

    def __str__(self):
        return '%s -- %s'%(self.business_unit, self.dept_name)

    class Meta:
        app_label   = 'apps_dms'
        db_table    = 'dept_list'
        indexes     = [
            models.Index(fields=['business_unit']),
            models.Index(fields=['dept_code']),
            models.Index(fields=['dept_name']),
        ]


class V_DMSRole(models.Model):
    nik               = models.CharField(max_length=20)
    dms_role_id       = models.IntegerField()
    role_name         = models.CharField(max_length=100)
    all_dept          = models.BooleanField(default=False)
    dept              = models.CharField(max_length=20)

    class Meta:
        app_label   = 'apps_dms'
        managed = False
        db_table = 'v_dmsrole'


class V_DMSDocuments(models.Model):
    no_document         = models.CharField(max_length=20)
    title_doc           = models.CharField(max_length=100)
    type_doc            = models.CharField(max_length=20)
    decs_doc            = models.TextField(null=True, blank=True)
    start_date_apply    = models.DateField(null=True, blank=True)
    is_public_doc       = models.BooleanField()
    bu_access           = models.CharField(max_length=20)
    dept_access         = models.CharField(max_length=500)
    posisi_access       = models.CharField(null=True,max_length=500)
    upload_doc          = models.FileField()
    status_active       = models.BooleanField()
    parent_document     = models.IntegerField()
    ver_doc             = models.IntegerField()
    parent_rev          = models.IntegerField()
    rev_doc             = models.IntegerField()
    overview_rev        = models.TextField(null=True, blank=True)
    
    class Meta:
        app_label   = 'apps_dms'
        managed = False
        db_table = 'v_dmsdocuments'
class V_DMSDocumentsSpc(models.Model):
    no_document         = models.CharField(max_length=20)
    title_doc           = models.CharField(max_length=100)
    type_doc            = models.CharField(max_length=20)
    decs_doc            = models.TextField(null=True, blank=True)
    start_date_apply    = models.DateField(null=True, blank=True)
    is_public_doc       = models.BooleanField()
    bu_access           = models.CharField(max_length=20)
    dept_access         = models.CharField(max_length=500)
    posisi_access       = models.CharField(null=True,max_length=500)
    upload_doc          = models.FileField()
    status_active       = models.BooleanField()
    parent_document     = models.IntegerField()
    ver_doc             = models.IntegerField()
    parent_rev          = models.IntegerField()
    rev_doc             = models.IntegerField()
    overview_rev        = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_dms'
        managed = False
        db_table = 'v_dmsdocspc'

class V_Org_PathDMS(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    parent_unit = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type_of_unit= models.CharField(max_length=100, blank=True, null=True)
    groupdept= models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label   = 'apps_core'
        managed = False
        db_table = 'v_orgpath'

class V_Org_Groupdept(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    groupdept = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label   = 'apps_core'
        managed = False
        db_table = 'v_org_groupdept'


class V_Multi_Department(models.Model):
    nik = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    bu = models.CharField(max_length=100, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label   = 'apps_core'
        managed = False
        db_table = 'v_multi_department'

class V_TypeMimeDMS(models.Model):
    code_mime           = models.CharField(max_length=200, null=True)
    mime_type           = models.CharField(max_length=200, null=True)
    mime_doc            = models.CharField(max_length=200, null=True)

    class Meta:
        app_label   = 'bbi_api'
        managed     = False
        db_table    = 'v_mimetypedoc'

class V_TypeDocDMS(models.Model):
    code_type           = models.CharField(max_length=200, null=True)
    type_doc            = models.CharField(max_length=200, null=True)
    type_label          = models.CharField(max_length=200, null=True)

    class Meta:
        app_label   = 'bbi_api'
        managed     = False
        db_table    = 'v_mastertypedocdms'

class NotifTemplate(models.Model):
    name            = models.CharField(max_length=50, null=True)
    template        = models.TextField( null=True)
    description    = models.TextField(max_length=50, null=True)
    params_template    = models.TextField(max_length=50, null=True)

    class Meta:
        app_label   = 'apps_notification'
        db_table    = 'notif_template'
        managed     = False