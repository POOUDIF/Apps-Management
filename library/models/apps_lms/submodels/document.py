from unicodedata import category
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

import os
from .institution import *
from .level import *
from .location import *
from .permit_type import *
from .department import *

def get_upload_path(instance, filename):
    return os.path.join(
        "dms/legal/{0}/{1}".format(instance.file_label, filename)
        # "dms/legal/document-legal/{1}".format(instance.file_label, filename)
    )

class DocumentLegal(models.Model):
    business_unit       = models.CharField(max_length=50)
    permit_type         = models.ForeignKey(PermitType,on_delete=models.CASCADE)
    location            = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,default=None)
    reminder            = models.IntegerField(null=True,default=None)
    # reminder            = models.ForeignKey(Reminder,on_delete=models.CASCADE,null=True,default=None)
    institution         = models.ForeignKey(Institution,on_delete=models.CASCADE)
    start_date          = models.DateField()
    end_date            = models.DateField(null=True)
    durations           = models.IntegerField(null=True)
    remind_date         = models.DateField(null=True)
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField(null=True)
    level               = models.ForeignKey(Level,on_delete=models.CASCADE)
    province            = models.CharField(max_length=100,null=True)
    city                = models.CharField(max_length=100,null=True)
    district            = models.CharField(max_length=100,null=True)
    ward                = models.CharField(max_length=100,null=True)
    file_location       = models.CharField(max_length=50)
    pic_dept            = models.ForeignKey(LegalDepartmentMapping,on_delete=models.CASCADE,null=True,default=None)
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(auto_now_add=True,null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    is_active           = models.BooleanField(default=True)
    type_dms            = models.CharField(max_length=200,null=True)
    id_notif            = models.IntegerField(null=True, blank=True)
    status              = models.CharField(max_length=200,null=True)
    workflow_id         = models.IntegerField(null=True, blank=True)
    notif_count         = models.IntegerField(default=0, blank=True, null=True)
    all_access         = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'document_legal'

class DocumentLegalFile(models.Model):
    document_legal  = models.ForeignKey(DocumentLegal,on_delete=models.CASCADE)
    file_src        = models.FileField(upload_to=get_upload_path, null=True)
    file_name       = models.CharField(max_length=300)
    file_label      = models.CharField(max_length=300)
    deleted_by      = models.CharField(max_length=50,null=True,default=None)
    deleted_at      = models.DateTimeField(null=True)
    is_active       = models.BooleanField(default=True)

    class Meta:
        app_label = 'apps_lms'
        db_table  = 'document_legal_file'

class V_DocumentLegalDashboard(models.Model):
    business_unit       = models.CharField(max_length=50)
    start_date          = models.DateField()
    end_date            = models.DateField()
    end_year            = models.IntegerField()
    remind_date         = models.DateField()
    durations           = models.IntegerField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    dept_name           = models.CharField(max_length=50)
    file_location       = models.CharField(max_length=300)
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    institution         = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    expired             = models.CharField(max_length=300)
    location_id         = models.IntegerField()
    location            = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    reminder_id         = models.IntegerField()
    reminder            = models.IntegerField()
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    category_id         = models.IntegerField()
    category_name       = models.CharField(max_length=300)
    transaction         = models.CharField(max_length=300)
    type_dms            = models.CharField(max_length=200)
    status              = models.CharField(max_length=200,null=True)
    workflow_id         = models.IntegerField(null=True, blank=True)
    category_transaction= models.CharField(max_length=200,null=True)
    notif_count         = models.IntegerField() 
    all_access         = models.BooleanField(default=False)
    # file_id             = models.IntegerField()
    # file_src            = models.FileField(upload_to=get_upload_path, null=True)
    # file_name           = models.CharField(max_length=300)
    # file_label          = models.CharField(max_length=300)


    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_documentlegal_dashboard'

class HistoryDownloadDocLegal(models.Model):
    document_legal  = models.ForeignKey(DocumentLegal,on_delete=models.CASCADE)
    file_id         = models.IntegerField(null=True, blank=True)
    customer_id     = models.IntegerField(null=True, blank=True)
    customer_name   = models.CharField(max_length=300, null=True, blank=True)
    customer_code   = models.CharField(max_length=300, null=True, blank=True)
    reason          = models.CharField(max_length=300, null=True, blank=True)
    created_by      = models.CharField(max_length=50, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by      = models.CharField(max_length=50, null=True, blank=True)
    updated_at      = models.DateTimeField(null=True, blank=True)
    deleted_by      = models.CharField(max_length=50, null=True, blank=True)
    deleted_at      = models.DateTimeField(null=True, blank=True)
    class Meta:
        app_label = 'apps_lms'
        db_table  = 'history_dowload_doc_legal'
        
class V_DocumentLegalDetail(models.Model):

    business_unit       = models.CharField(max_length=300)
    start_date          = models.DateField()
    end_date            = models.DateField()
    end_year            = models.CharField(max_length=5)
    durations           = models.IntegerField()
    remind_date         = models.DateField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=300)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    file_location       = models.CharField(max_length=300)
    created_by          = models.CharField(max_length=300)
    created_at          = models.DateField()
    modified_by         = models.CharField(max_length=300)
    modified_at         = models.DateField()
    deleted_by          = models.CharField(max_length=300)
    deleted_at          = models.DateField()
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    name                = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    level_name          = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    expired             = models.CharField(max_length=300)
    # reminder            = models.IntegerField()
    file_id             = models.IntegerField()
    file_src            = models.CharField(max_length=300)
    file_name           = models.CharField(max_length=300)
    file_label          = models.CharField(max_length=300)
    document_legal_id   = models.IntegerField()
    status              = models.CharField(max_length=200,null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_documentlegal_detail'


class V_DocumentLegalReminder(models.Model):
    # business_unit       = models.CharField(max_length=50)
    # start_date          = models.DateField()
    # end_date            = models.DateField()
    # remind_date         = models.DateField()
    # permit_no           = models.CharField(max_length=300)
    # is_active           = models.BooleanField()
    # institution         = models.CharField(max_length=300)
    # permit_type         = models.CharField(max_length=300)
    # location            = models.CharField(max_length=300)
    # reminder            = models.IntegerField()
    # created_by          = models.CharField(max_length=50)
    # created_at          = models.DateTimeField(auto_now_add=True)
    # modified_by         = models.CharField(max_length=50)
    # modified_at         = models.DateTimeField(null=True)
    # deleted_by          = models.CharField(max_length=50)
    # deleted_at          = models.DateTimeField(null=True)

    business_unit       = models.CharField(max_length=50)
    start_date          = models.DateField()
    start_year            = models.IntegerField()
    end_date            = models.DateField()
    end_year            = models.IntegerField()
    remind_date         = models.DateField()
    durations           = models.IntegerField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    file_location       = models.CharField(max_length=300)
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    institution         = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    location_id         = models.IntegerField()
    location            = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    reminder_id         = models.IntegerField()
    reminder            = models.IntegerField()
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    pic_dept_id         = models.IntegerField()
    type_dms            = models.CharField(max_length=200)
    dept_name           = models.CharField(max_length=50)
    status              = models.CharField(max_length=200,null=True)
    # file_id             = models.IntegerField()
    # file_src            = models.FileField(upload_to=get_upload_path, null=True)
    # file_name           = models.CharField(max_length=300)
    # file_label          = models.CharField(max_length=300)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_documentlegal_reminder'


class V_CreateLegalEmail(models.Model):

    business_unit       = models.CharField(max_length=300)
    start_date          = models.DateField()
    end_date            = models.DateField()
    # end_year            = models.CharField(max_length=5)
    durations           = models.IntegerField()
    remind_date         = models.DateField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=300)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    file_location       = models.CharField(max_length=300)
    created_by          = models.CharField(max_length=300)
    created_at          = models.DateField()
    modified_by         = models.CharField(max_length=300)
    modified_at         = models.DateField()
    deleted_by          = models.CharField(max_length=300)
    deleted_at          = models.DateField()
    is_active           = models.BooleanField()
    institution         = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    permit_type         = models.CharField(max_length=300)
    expired             = models.CharField(max_length=300)
    reminder            = models.IntegerField()
    file_id             = models.IntegerField()
    file_src            = models.CharField(max_length=300)
    file_name           = models.CharField(max_length=300)
    file_label          = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    status              = models.CharField(max_length=200,null=True)


    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_create_legal_mail'


class V_LegalFileDoc(models.Model):
    file_src            = models.CharField(max_length=300)
    file_name           = models.CharField(max_length=300)
    permit_no           = models.CharField(max_length=300)
    file_label          = models.CharField(max_length=300)
    deleted_by          = models.CharField(max_length=300)
    deleted_at          = models.DateTimeField(null=True)
    is_active           = models.BooleanField(default=True)
    document_legal_id   = models.IntegerField()


    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_legal_file_doc'

class LMSMasterMailer(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    cc = models.CharField(max_length=255, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'lms_master_mailer'

class LMSMasterType(models.Model):
    code_type = models.CharField(max_length=255, null=True, blank=True)
    type_doc = models.CharField(max_length=255, null=True, blank=True)
    type_label = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'lms_master_type'

class LMSMasterCity(models.Model):
    provinsi    = models.CharField(max_length=200)
    kota        = models.CharField(max_length=200)
    kecamatan   = models.CharField(max_length=200)
    kelurahan   = models.CharField(max_length=200)
    kodepos     = models.CharField(max_length=10)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'lms_master_city'


class V_DocumentLegalApproval(models.Model):
    business_unit       = models.CharField(max_length=50)
    start_date          = models.DateField()
    end_date            = models.DateField()
    end_year            = models.IntegerField()
    remind_date         = models.DateField()
    durations           = models.IntegerField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    file_location       = models.CharField(max_length=300)
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    institution         = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    location_id         = models.IntegerField()
    location            = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    reminder_id         = models.IntegerField()
    reminder            = models.IntegerField()
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    pic_dept_id         = models.IntegerField()
    type_dms            = models.CharField(max_length=200)
    dept_name           = models.CharField(max_length=50)
    status              = models.CharField(max_length=200,null=True)
    status_request      = models.CharField(max_length=200,null=True)
    requester           = models.CharField(max_length=200,null=True)
    header_id       = models.IntegerField(null=True, blank=True)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_document_legal_approval'


class LMSRequestDocument(models.Model):
    document_legal  = models.ForeignKey(DocumentLegal,on_delete=models.CASCADE)
    mail_requester  = models.TextField(null=True, blank=True)
    status          = models.CharField(max_length=255, null=True, blank=True)
    reason          = models.TextField(null=True, blank=True)
    workflow_id     = models.IntegerField(null=True, blank=True)
    header_id       = models.IntegerField(null=True, blank=True)
    created_by      = models.CharField(max_length=255, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by      = models.CharField(max_length=255, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'lms_document_request'

class V_LMSRequestDocument(models.Model):
    document_legal  = models.ForeignKey(DocumentLegal,on_delete=models.CASCADE)
    mail_requester  = models.TextField(null=True, blank=True)
    status          = models.CharField(max_length=255, null=True, blank=True)
    reason          = models.TextField(null=True, blank=True)
    workflow_id     = models.IntegerField(null=True, blank=True)
    header_id       = models.IntegerField(null=True, blank=True)
    created_by      = models.CharField(max_length=255, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by      = models.CharField(max_length=255, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        managed     = False
        app_label = 'apps_lms'
        db_table = 'v_lms_document_request'

class LMSRequestDocumentHeader(models.Model):
    # document_legal  = models.ForeignKey(DocumentLegal,on_delete=models.CASCADE)
    requester_name  = models.TextField(null=True, blank=True)
    requester_nik   = models.TextField(null=True, blank=True)
    mail_requester  = models.TextField(null=True, blank=True)
    status          = models.CharField(max_length=255, null=True, blank=True)
    reason          = models.TextField(null=True, blank=True)
    workflow_id     = models.IntegerField(null=True, blank=True)
    created_by      = models.CharField(max_length=255, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by      = models.CharField(max_length=255, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        app_label = 'apps_lms'
        db_table = 'lms_document_request_header'

class V_DocumentLegalReminderV2(models.Model):
    business_unit       = models.CharField(max_length=50)
    start_date          = models.DateField()
    start_year            = models.IntegerField()
    end_date            = models.DateField()
    end_year            = models.IntegerField()
    remind_date         = models.DateField()
    durations           = models.IntegerField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    file_location       = models.CharField(max_length=300)
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    institution         = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    location_id         = models.IntegerField()
    location            = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    reminder_id         = models.IntegerField()
    reminder            = models.IntegerField()
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    pic_dept_id         = models.IntegerField()
    type_dms            = models.CharField(max_length=200)
    dept_name           = models.CharField(max_length=50)
    status              = models.CharField(max_length=200,null=True)
    notif_count         = models.IntegerField()
    # file_id             = models.IntegerField()
    # file_src            = models.FileField(upload_to=get_upload_path, null=True)
    # file_name           = models.CharField(max_length=300)
    # file_label          = models.CharField(max_length=300)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_documentlegal_reminder_v2'
class V_DocumentLegalReminderNotif(models.Model):
    business_unit       = models.CharField(max_length=50)
    start_date          = models.DateField()
    start_year            = models.IntegerField()
    end_date            = models.DateField()
    end_year            = models.IntegerField()
    remind_date         = models.DateField()
    durations           = models.IntegerField()
    permit_no           = models.CharField(max_length=300)
    extend              = models.CharField(max_length=5)
    extend_no           = models.IntegerField()
    province            = models.CharField(max_length=300)
    city                = models.CharField(max_length=300)
    district            = models.CharField(max_length=300)
    ward                = models.CharField(max_length=300)
    pic_dept_id         = models.IntegerField()
    file_location       = models.CharField(max_length=300)
    is_active           = models.BooleanField()
    institution_id      = models.IntegerField()
    institution         = models.CharField(max_length=300)
    permit_type_id      = models.IntegerField()
    permit_type         = models.CharField(max_length=300)
    location_id         = models.IntegerField()
    location            = models.CharField(max_length=300)
    level_name          = models.CharField(max_length=300)
    level_id            = models.IntegerField()
    reminder_id         = models.IntegerField()
    reminder            = models.IntegerField()
    created_by          = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_by         = models.CharField(max_length=50)
    modified_at         = models.DateTimeField(null=True)
    deleted_by          = models.CharField(max_length=50)
    deleted_at          = models.DateTimeField(null=True)
    pic_dept_id         = models.IntegerField()
    type_dms            = models.CharField(max_length=200)
    dept_name           = models.CharField(max_length=50)
    status              = models.CharField(max_length=200,null=True)
    notif_count         = models.IntegerField()
    notif_plan    = models.IntegerField()
    # file_id             = models.IntegerField()
    # file_src            = models.FileField(upload_to=get_upload_path, null=True)
    # file_name           = models.CharField(max_length=300)
    # file_label          = models.CharField(max_length=300)

    class Meta:
        managed     = False
        app_label   = 'apps_lms'
        db_table    = 'v_documentlegal_notif'