from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from library.models.bbicore.submodels.base import BaseModelApps


class MonitoringOperation(models.Model):
    id                          = models.IntegerField(null=True,blank=True)
    no_style                    = models.CharField(null=True,blank=True)
    article                     = models.CharField(null=True,blank=True)
    brand                       = models.CharField(null=True,blank=True)
    year                        = models.IntegerField(null=True,blank=True)
    coll_month                  = models.CharField(null=True,blank=True)
    type                        = models.CharField(null=True,blank=True)
    plan_coll_prstn_formatted   = models.DateField(null=True,blank=True)
    move_coll_prstn_formatted   = models.DateField(null=True,blank=True)
    actual_coll_prstn_formatted = models.DateField(null=True,blank=True)
    difference_coll_prstn       = models.IntegerField(null=True,blank=True)   
    move_difference_coll_prstn  = models.IntegerField(null=True,blank=True)
    leadtime_coll_prstn         = models.CharField(null=True,blank=True)
    plan_input_plm_formatted    = models.DateField(null=True,blank=True)
    move_input_plm_formatted    = models.DateField(null=True,blank=True)
    actual_input_plm_formatted  = models.DateField(null=True,blank=True)
    difference_input_plm        = models.IntegerField(null=True,blank=True)
    move_difference_input_plm   = models.IntegerField(null=True,blank=True)
    leadtime_input_plm          = models.CharField(null=True,blank=True)
    plan_placing_subcont_formatted         = models.DateField(null=True,blank=True)
    move_placing_subcont_formatted         = models.DateField(null=True,blank=True)
    actual_placing_subcont_formatted       = models.DateField(null=True,blank=True)
    difference_placing_subcont             = models.IntegerField(null=True,blank=True)
    move_difference_placing_subcont        = models.IntegerField(null=True,blank=True)
    leadtime_placing_subcont               = models.CharField(null=True,blank=True)
    plan_designer_mtr_subcont_formatted    = models.DateField(null=True,blank=True)
    move_designer_mtr_subcont_formatted    = models.DateField(null=True,blank=True)
    actual_designer_mtr_subcont_formatted  = models.DateField(null=True,blank=True)
    difference_designer_mtr_subcont        = models.IntegerField(null=True,blank=True)
    move_difference_designer_mtr_subcont   = models.IntegerField(null=True,blank=True)
    leadtime_designer_mtr_subcont          = models.CharField(null=True,blank=True)
    plan_proto_rec_1_formatted             = models.DateField(null=True,blank=True)
    move_proto_rec_1_formatted             = models.DateField(null=True,blank=True)
    actual_proto_rec_1_formatted           = models.DateField(null=True,blank=True)
    difference_proto_rec_1                 = models.IntegerField(null=True,blank=True)
    move_difference_proto_rec_1            = models.IntegerField(null=True,blank=True)
    leadtime_proto_rec_1                   = models.CharField(null=True,blank=True)
    plan_proto_comment_1_formatted         = models.DateField(null=True,blank=True)
    move_proto_comment_1_formatted         = models.DateField(null=True,blank=True)
    actual_proto_comment_1_formatted       = models.DateField(null=True,blank=True)
    difference_proto_comment_1             = models.IntegerField(null=True,blank=True)
    move_difference_proto_comment_1        = models.IntegerField(null=True,blank=True)
    leadtime_proto_comment_1               = models.CharField(null=True,blank=True)
    plan_proto_rec_2_formatted             = models.DateField(null=True,blank=True)
    move_proto_rec_2_formatted             = models.DateField(null=True,blank=True)
    actual_proto_rec_2_formatted           = models.DateField(null=True,blank=True)
    difference_proto_rec_2                 = models.IntegerField(null=True,blank=True)
    move_difference_proto_rec_2            = models.IntegerField(null=True,blank=True)
    leadtime_proto_rec_2                   = models.CharField(null=True,blank=True)
    plan_proto_approved_formatted          = models.DateField(null=True,blank=True)
    move_proto_approved_formatted          = models.DateField(null=True,blank=True)
    actual_proto_approved_formatted        = models.DateField(null=True,blank=True)
    difference_proto_approved              = models.IntegerField(null=True,blank=True)
    move_difference_proto_approved         = models.IntegerField(null=True,blank=True)
    leadtime_proto_approved                = models.CharField(null=True,blank=True)
    summary_plan_lead_time_prodev          = models.IntegerField(null=True,blank=True)
    summary_difference_lead_time_prodev    = models.IntegerField(null=True,blank=True)
    summary_actual_lead_time_prodev        = models.IntegerField(null=True,blank=True)
    summary_result_lead_time_prodev        = models.CharField(null=True,blank=True)
    plan_po_fabric_release_formatted       = models.DateField(null=True,blank=True)
    move_po_fabric_release_formatted       = models.DateField(null=True,blank=True)
    actual_po_fabric_release_formatted     = models.DateField(null=True,blank=True)
    difference_po_fabric_release           = models.IntegerField(null=True,blank=True)
    move_difference_po_fabric_release      = models.IntegerField(null=True,blank=True)
    leadtime_po_fabric_release             = models.CharField(null=True,blank=True)
    plan_release_io_formatted              = models.DateField(null=True,blank=True)
    move_release_io_formatted              = models.DateField(null=True,blank=True)
    actual_release_io_formatted            = models.DateField(null=True,blank=True)
    difference_release_io                  = models.IntegerField(null=True,blank=True)
    move_difference_release_io             = models.IntegerField(null=True,blank=True)
    leadtime_release_io                    = models.CharField(null=True,blank=True)
    plan_approval_pps_formatted            = models.DateField(null=True,blank=True)
    move_approval_pps_formatted            = models.DateField(null=True,blank=True)
    actual_approval_pps_formatted          = models.DateField(null=True,blank=True)
    difference_approval_pps                = models.IntegerField(null=True,blank=True)
    move_difference_approval_pps           = models.IntegerField(null=True,blank=True)
    leadtime_approval_pps                  = models.CharField(null=True,blank=True)
    plan_final_insp_formatted              = models.DateField(null=True,blank=True)
    move_final_insp_formatted              = models.DateField(null=True,blank=True)
    actual_final_insp_formatted            = models.DateField(null=True,blank=True)
    difference_final_insp                  = models.IntegerField(null=True,blank=True)
    move_difference_final_insp             = models.IntegerField(null=True,blank=True)
    leadtime_final_insp                    = models.CharField(null=True,blank=True)
    plan_fabric_insp_formatted             = models.DateField(null=True,blank=True)
    move_fabric_insp_formatted             = models.DateField(null=True,blank=True)
    actual_fabric_insp_formatted           = models.DateField(null=True,blank=True)
    difference_fabric_insp                 = models.IntegerField(null=True,blank=True)
    move_difference_fabric_insp            = models.IntegerField(null=True,blank=True)
    leadtime_fabric_insp                   = models.CharField(null=True,blank=True)
    plan_fabric_bkb_formatted              = models.DateField(null=True,blank=True)
    move_fabric_bkb_formatted              = models.DateField(null=True,blank=True)
    actual_fabric_bkb_formatted            = models.DateField(null=True,blank=True)
    difference_fabric_bkb                  = models.IntegerField(null=True,blank=True)
    move_difference_fabric_bkb             = models.IntegerField(null=True,blank=True)
    leadtime_fabric_bkb                    = models.CharField(null=True,blank=True)
    plan_fabric_btfg_formatted             = models.DateField(null=True,blank=True)
    move_fabric_btfg_formatted             = models.DateField(null=True,blank=True)
    actual_fabric_btfg_formatted           = models.DateField(null=True,blank=True)
    difference_fabric_btfg                 = models.IntegerField(null=True,blank=True)
    move_difference_fabric_btfg            = models.IntegerField(null=True,blank=True)
    leadtime_fabric_btfg                   = models.CharField(null=True,blank=True)
    plan_supply_chain                      = models.CharField(null=True,blank=True)
    actual_supply_chain                    = models.IntegerField(null=True,blank=True)
    difference_supply_chain                = models.IntegerField(null=True,blank=True)
    result_supply_chain                    = models.CharField(null=True,blank=True)
    plan_total                             = models.CharField(null=True,blank=True)
    actual_total                           = models.IntegerField(null=True,blank=True)
    difference_total                       = models.IntegerField(null=True,blank=True) 
    result_total                           = models.CharField(null=True,blank=True)
    status                                 = models.CharField(null=True,blank=True)
    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'end_to_end_monitoring'
        managed     = False


class Parameter(BaseModelApps):
    name          = models.CharField(max_length=100, null=True)
    modul         = models.CharField(max_length=100, null=True)
    param_1       = models.TextField()
    param_2       = models.TextField()
    param_3       = models.TextField()
    param_4       = models.TextField()
    param_5       = models.TextField()
    param_6       = models.TextField()

    class Meta:
        app_label   = 'apps_e2e'
        db_table    = 'parameter'