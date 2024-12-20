from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

from library.models.bbicore import BaseModel


""" WorkflowProfile : WF Profile used on workflow routing
    profile_no  : Document number, ex : WF2L, WF3L etc
    profile_name: Document name, ex : "WORKFLOW 2 LAYERS", etc
    profile     : relate to WorkflowProfile(profile_id)
    origin      : (used on copy document) doc_no of copied document
    reference   : (used on related doc / breakout document) doc_no of related / parent document
"""
class WorkflowProfile(models.Model):
    OPT_MODE = (('OPR', 'OPR'), ('GW', 'GW'), ('SSH', 'SSH'), ('SPV', 'SPV'), ('SSSH', 'SSSH'), ('SH', 'SH'), ('SDH', 'SDH'), ('DH', 'DH'), ('SDIV', 'SDIV'), ('DVH', 'DVH'), ('CSCO', 'CSCO'), ('BOC', 'BOC'), ('COO', 'COO'), ('DIR', 'DIR'), ('CEO', 'CEO'), ('CFO', 'CFO'), ('CMO', 'CMO'))
    profile_no      = models.CharField(max_length=50, unique=True)
    profile_name    = models.CharField(max_length=200)
    is_custom_route = models.BooleanField(default=False)
    wf_steps        = models.IntegerField(default=1)
    level_min       = models.CharField(max_length=50, choices=OPT_MODE, default = 'DH', null=True, blank=True)
    level_max       = models.CharField(max_length=50, choices=OPT_MODE, null=True, blank=True)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'wf_profile'
        # managed     = False
    def __str__(self):
        return '(%s) %s -- %s'%(self.profile_no, self.profile_name, self.wf_steps)


class CustomRoute(models.Model):
    OPT_MODE = (('GW', 'GW'), ('SSH', 'SSH'), ('SPV', 'SPV'), ('SSSH', 'SSSH'), ('SH', 'SH'), ('SDH', 'SDH'), ('DH', 'DH'), ('SDIV', 'SDIV'), ('DVH', 'DVH'), ('CSCO', 'CSCO'), ('BOC', 'BOC'), ('COO', 'COO'), ('DIR', 'DIR'), ('CEO', 'CEO'), ('CFO', 'CFO'), ('CMO', 'CMO'))
    profile         = models.ForeignKey(WorkflowProfile, on_delete=models.CASCADE)
    step_no         = models.IntegerField(default=1)
    position        = models.CharField(max_length=50, choices=OPT_MODE, default = 'DH', null=True, blank=True)
    nik             = models.CharField(max_length=50, null=True, blank=True)
    organization    = models.CharField(max_length=50, null=True, blank=True)
    job             = models.CharField(max_length=50, null=True, blank=True)
    bu              = models.CharField(max_length=50, null=True, blank=True, default = 'BBI1')

    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'custom_route'
        unique_together = ('profile', 'step_no',)
        # managed     = False
    def __str__(self):
        return '(%s) -- %s'%(self.profile,  self.step_no)


class DocumentProfile(models.Model):
    doc_profile_no  = models.CharField(max_length=50, unique=True)
    doc_prefix      = models.CharField(max_length=50, unique=True)
    doc_name        = models.CharField(max_length=200)
    callback_url    = models.CharField(max_length=250)
    wf_profile      = models.ForeignKey(WorkflowProfile, on_delete=models.CASCADE)
    last_sequence   = models.IntegerField(default=0)
    doc_length      = models.IntegerField(default=4)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'doc_profile'
        # managed     = False
    def __str__(self):
        return '(%s) %s -- %s'%(self.doc_profile_no, self.doc_prefix, self.doc_name)


class WorkflowCustomRoute(models.Model):
    wf_profile      = models.ForeignKey(WorkflowProfile, on_delete=models.CASCADE)
    profile_name    = models.CharField(max_length=200)
    is_custom_route = models.BooleanField(default=False)
    wf_steps        = models.IntegerField()
    unit_level_min  = models.CharField(max_length=50, null=True, blank=True)
    unit_level_max  = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'wf_custom_route'
        # managed     = False


""" Workflow : Represent Document on workflow
    doc_no      : Document number, ex : PLM010101 or PLM-BP/22/09/..... etc
    doc_name    : Document name, ex : "Product Development Form", etc
    profile     : relate to WorkflowProfile(profile_id)
    origin      : (used on copy document) doc_no of copied document
    reference   : (used on related doc / breakout document) doc_no of related / parent document
"""
class Workflow(models.Model):
    doc_no              = models.CharField(max_length=50)
    doc_name            = models.CharField(max_length=200)
    apps_name           = models.CharField(max_length=200, null=True)
    profile_no          = models.CharField(max_length=50)
    origin              = models.CharField(max_length=50, null=True, blank=True)
    reference           = models.CharField(max_length=50, null=True, blank=True)
    wf_state            = models.CharField(max_length=50)
    cur_step            = models.IntegerField(null=True, blank=True)
    create_date         = models.DateTimeField(auto_now_add=True)
    update_date         = models.DateTimeField(null=True)
    update_by           = models.CharField(max_length=50, null=True)
    creator             = models.CharField(max_length=50)
    creator_name        = models.CharField(max_length=50)
    creator_org         = models.CharField(max_length=50)
    creator_pos         = models.CharField(max_length=50)
    creator_org_name    = models.CharField(max_length=500)
    creator_pos_name    = models.CharField(max_length=500)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'workflow'
        # managed     = False


class WorkflowLine(models.Model):
    workflow                = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    step_no                 = models.IntegerField()
    state                   = models.CharField(max_length=50)
    processor               = models.CharField(max_length=50)
    processor_name          = models.CharField(max_length=200)
    actual_processor        = models.CharField(max_length=50)
    actual_processor_name   = models.CharField(max_length=200)
    processed_date          = models.DateTimeField(null=True)
    next_step_no            = models.IntegerField(null=True, blank=True)
    next_processor          = models.CharField(max_length=50, null=True, blank=True)
    next_processor_name     = models.CharField(max_length=200, null=True, blank=True)
    processor_comment       = models.TextField(null=True)
    workflow_data           = models.TextField(null=True)
    callback_url            = models.CharField(max_length=250, null=True, blank=True)
    callback_param          = models.CharField(max_length=250, null=True, blank=True)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'wf_line'
        # managed     = False


class V_InboxWorkflowLine(models.Model):
    id              = models.CharField(max_length=50,primary_key=True)
    workflow_id     = models.CharField(max_length=50)
    doc_no          = models.CharField(max_length=50)
    doc_name        = models.CharField(max_length=200)
    state           = models.CharField(max_length=50)
    processor       = models.CharField(max_length=50)
    processor_name  = models.CharField(max_length=200)
    next_processor_name = models.CharField(max_length=200)
    create_date     = models.DateTimeField(auto_now_add=True)
    callback_url    = models.CharField(max_length=200)
    callback_param  = models.CharField(max_length=200)
    apps_name       = models.CharField(max_length=200)
    update_date     = models.DateTimeField(null=True)
    creator_name    = models.CharField(max_length=200)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'v_inbox_wf'
        managed     = False


class V_OutboxWorkflowLine(models.Model):
    id              = models.CharField(max_length=50, primary_key=True)
    workflow_id     = models.CharField(max_length=50)
    doc_no          = models.CharField(max_length=50)
    doc_name        = models.CharField(max_length=200)
    state           = models.CharField(max_length=50)
    wf_state        = models.CharField(max_length=50)
    create_date     = models.DateTimeField(auto_now_add=True)
    callback_url    = models.CharField(max_length=200)
    callback_param  = models.CharField(max_length=200)
    creator         = models.CharField(max_length=200)
    creator_name    = models.CharField(max_length=200)
    apps_name       = models.CharField(max_length=200)
    update_date     = models.DateTimeField(null=True)
    next_processor_name    = models.CharField(max_length=200)

    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'v_outbox_wf'
        managed     = False


class V_ClosedWorkflowLine(models.Model):
    id              = models.CharField(max_length=50, primary_key=True)
    workflow_id     = models.CharField(max_length=50)
    doc_no          = models.CharField(max_length=50)
    doc_name        = models.CharField(max_length=200)
    state           = models.CharField(max_length=50)
    wf_state        = models.CharField(max_length=50)
    create_date     = models.DateTimeField(auto_now_add=True)
    callback_url    = models.CharField(max_length=200)
    callback_param  = models.CharField(max_length=200)
    creator         = models.CharField(max_length=200)
    creator_name    = models.CharField(max_length=200)
    processor       = models.CharField(max_length=200)
    apps_name       = models.CharField(max_length=200)
    update_date     = models.DateTimeField(null=True)
    class Meta:
        app_label   = 'apps_workflow'
        db_table    = 'v_closed_wf'
        managed     = False

# From Model Notification

class ContactGroup(models.Model):
    group_name            = models.CharField(max_length=50, null=True)
    description           = models.TextField(max_length=50, null=True)
    is_active             = models.BooleanField(default=False)

    class Meta:
        app_label   = 'apps_notification'
        db_table    = 'contact_group'
        managed     = False

    def __str__(self):
        return '%s'%(self.group_name)
        # return '%s -- %s'%(self.group_name, self.description)

class Contact(models.Model):
    nik             = models.CharField(max_length=50, null=True)
    name            = models.CharField(max_length=50, null=True)
    phone_no        = models.TextField(max_length=50, null=True)
    email_office    = models.TextField(max_length=50, null=True)
    email_public    = models.TextField(max_length=50, null=True)
    contact_group   = models.ManyToManyField(ContactGroup)

    class Meta:
        app_label   = 'apps_notification'
        db_table    = 'contact'
        managed     = False

