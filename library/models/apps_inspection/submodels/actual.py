from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid
from .planning import *

class InspectionActualPPS(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_date                = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_date                = models.DateTimeField(editable=True, blank=True, null=True)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    approval                    = models.CharField(null=True, blank=True, max_length=200)
    note                        = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_pps'
        indexes     = [
            models.Index(fields=['io', 'id_transaction'])
        ]

class V_InspectionActualPPS(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_date                = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_date                = models.DateTimeField(editable=True, blank=True, null=True)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    article                     = models.CharField(null=True, blank=True, max_length=50)
    qty_order                   = models.IntegerField(null=True, blank=True)
    brand                       = models.CharField(null=True, blank=True, max_length=50)
    category                    = models.CharField(null=True, blank=True, max_length=50)
    delivery                    = models.DateField(null=True, blank=True)
    style_code                  = models.CharField(null=True, blank=True, max_length=50)
    style_desc                  = models.TextField(null=True, blank=True)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    approval                    = models.CharField(null=True, blank=True, max_length=200)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    note                        = models.TextField(null=True, blank=True)
    monitoring_id               = models.IntegerField(null=True,blank=True)
    parent_to                   = models.IntegerField(blank=True, null=True)
    article_group               = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_pps'
        managed     = False


class PPSPointOfFocus(models.Model):
    pps                         = models.ForeignKey(InspectionActualPPS, on_delete=models.CASCADE)
    style_category              = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    brand                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    checklist                   = models.CharField(null=True, blank=True, max_length=10)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_pps_point_of_focus'
        indexes     = [
            models.Index(fields=['value', 'focus_type','remark'])
        ]

class V_PPSPointOfFocus(models.Model):
    pps                         = models.ForeignKey(InspectionActualPPS, on_delete=models.CASCADE)
    style_category              = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    brand                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    checklist                   = models.CharField(null=True, blank=True, max_length=10)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_pps_point_of_focus'
        managed     = False

class PPSSizeSpec(models.Model):
    pps                         = models.ForeignKey(InspectionActualPPS, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val                  = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation                   = models.CharField(null=True, blank=True, max_length=200)
    pic                         = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_pps_size_spec'
        indexes     = [
            models.Index(fields=['description', 'size_code','actual_val','deviation','tolerance_min','tolerance_max'])
        ]

class V_PPSSizeSpec(models.Model):
    pps                         = models.ForeignKey(InspectionActualPPS, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val                  = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation                   = models.CharField(null=True, blank=True, max_length=200)
    pic                         = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_pps_size_spec'
        managed     = False

# class FileSizeSpec(models.Model):
#     name_file                   = models.CharField(null=True, blank=True, max_length=200)
#     url_file                    = models.CharField(null=True, blank=True, max_length=200)
#     created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
#     created_by                  = models.CharField(null=True, blank=True, max_length=200)
#     updated                     = models.DateTimeField(auto_now_add=True, editable=True, null=True, blank=True)
#     updated_by                  = models.CharField(null=True, blank=True, max_length=200)

#     class Meta:
#         app_label   = 'apps_inspection'
#         db_table    = 'inspection_file_size_spec'

class InspectionActualPPM(models.Model):
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    io                          = models.IntegerField(null=True, blank=True)
    attendees                   = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(null=True, blank=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    approval                    = models.CharField(null=True, blank=True, max_length=200)
    plan_cutting                = models.DateField(null=True, blank=True)
    plan_sewing                 = models.DateField(null=True, blank=True)
    output_per_day              = models.CharField(null=True, blank=True, max_length=20)
    image_fabric                = models.BooleanField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_ppm'
        indexes     = [
            models.Index(fields=['io', 'attendees','created','id_transaction','created_by'])
        ]

class InspectionPPMAttachment(models.Model):
    ppm                         = models.ForeignKey(InspectionActualPPM, on_delete=models.CASCADE)
    category                    = models.CharField(null=True, blank=True, max_length=200)
    img                         = models.ImageField(upload_to="insp/ppm/", blank=True, null=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_ppm_attachment'

class V_InspectionPPMAttachment(models.Model):
    ppm                         = models.ForeignKey(InspectionActualPPM, on_delete=models.CASCADE)
    category                    = models.CharField(null=True, blank=True, max_length=200)
    img                         = models.ImageField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_ppm_attachment'
        managed     = False

class V_InspectionActualPPM(models.Model):
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    io                          = models.IntegerField(null=True, blank=True)
    attendees                   = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(null=True, blank=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    article                     = models.CharField(null=True, blank=True, max_length=50)
    qty_order                   = models.IntegerField(null=True, blank=True)
    brand                       = models.CharField(null=True, blank=True, max_length=50)
    category                    = models.CharField(null=True, blank=True, max_length=50)
    delivery                    = models.DateField(null=True, blank=True)
    style_code                  = models.CharField(null=True, blank=True, max_length=50)
    style_desc                  = models.TextField(null=True, blank=True)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=50)
    plan_cutting                = models.DateField(null=True, blank=True)
    plan_sewing                 = models.DateField(null=True, blank=True)
    output_per_day              = models.CharField(null=True, blank=True, max_length=20)
    pic_nik                     = models.CharField(null=True, blank=True, max_length=200)
    parent_to                   = models.IntegerField(blank=True, null=True)
    image_fabric                = models.BooleanField(null=True, blank=True)
    article_group               = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_ppm'
        managed     = False


class InspectionActualPPMDetail(models.Model):
    ppm                         = models.ForeignKey(InspectionActualPPM, on_delete=models.CASCADE)
    pic                         = models.CharField(null=True, blank=True, max_length=200)
    note                        = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_ppm_detail'
        indexes     = [
            models.Index(fields=['pic'])
        ]

class V_InspectionActualPPMDetail(models.Model):
    ppm                         = models.ForeignKey(InspectionActualPPM, on_delete=models.CASCADE)
    pic                         = models.CharField(null=True, blank=True, max_length=200)
    note                        = models.TextField(null=True, blank=True)


    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_ppm_detail'
        managed     = False

class V_InspectionListSchedule(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    monitoring_id               = models.IntegerField(null=True, blank=True)
    state                       = models.CharField(null=True, blank=True, max_length=20)
    inspection_type             = models.CharField(null=True, blank=True, max_length=20)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    pic_nik                     = models.CharField(null=True, blank=True, max_length=50)
    pic_name                    = models.CharField(null=True, blank=True, max_length=100)
    plan_date                   = models.DateField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=20)
    created_by_name             = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=20)
    updated_by_name             = models.CharField(null=True, blank=True, max_length=200)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    article                     = models.CharField(null=True, blank=True, max_length=200)
    style_desc                  = models.CharField(null=True, blank=True, max_length=200)
    qty_order                   = models.IntegerField(null=True, blank=True)
    parent_to                   = models.IntegerField(blank=True, null=True)


    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_list_schedule'
        managed     = False

class InspectionInline(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    sample_ref_no               = models.CharField(null=True, blank=True, max_length=200)
    qty_output                  = models.IntegerField(null=True, blank=True)
    qty_sample                  = models.IntegerField(null=True, blank=True)
    cutting_report              = models.IntegerField(null=True, blank=True)
    result                      = models.CharField(null=True, blank=True, max_length=200)
    qty_critical                = models.IntegerField(null=True, blank=True)
    qty_minor                   = models.IntegerField(null=True, blank=True)
    qty_major                   = models.IntegerField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    qc_name                     = models.CharField(null=True, blank=True, max_length=200)
    qc_sign                     = models.TextField(null=True, blank=True)
    qc_date                     = models.DateTimeField(null=True, blank=True)
    vendor_pos                  = models.CharField(null=True, blank=True, max_length=200)
    vendor_name                 = models.CharField(null=True, blank=True, max_length=200)
    vendor_sign                 = models.TextField(null=True, blank=True)
    vendor_date                 = models.DateTimeField(null=True, blank=True)
    vendor_opt_pos              = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_name             = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_sign             = models.TextField(null=True, blank=True)
    vendor_opt_date             = models.DateTimeField(null=True, blank=True)
    inline_type                 = models.CharField(null=True, blank=True, max_length=200)
    comment                     = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_inline'
        indexes     = [
            models.Index(fields=['io','id_transaction','result'])
        ]

class V_InspectionInline(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    qty_order                   = models.IntegerField(null=True, blank=True)
    sample_ref_no               = models.CharField(null=True, blank=True, max_length=200)
    qty_output                  = models.IntegerField(null=True, blank=True)
    qty_sample                  = models.IntegerField(null=True, blank=True)
    cutting_report              = models.IntegerField(null=True, blank=True)
    result                      = models.CharField(null=True, blank=True, max_length=200)
    qty_critical                = models.IntegerField(null=True, blank=True)
    qty_minor                   = models.IntegerField(null=True, blank=True)
    qty_major                   = models.IntegerField(null=True, blank=True)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    qc_name                     = models.CharField(null=True, blank=True, max_length=200)
    qc_sign                     = models.TextField(null=True, blank=True)
    qc_date                     = models.DateTimeField(null=True, blank=True)
    vendor_pos                  = models.CharField(null=True, blank=True, max_length=200)
    vendor_name                 = models.CharField(null=True, blank=True, max_length=200)
    vendor_sign                 = models.TextField(null=True, blank=True)
    vendor_date                 = models.DateTimeField(null=True, blank=True)
    vendor_opt_pos              = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_name             = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_sign             = models.TextField(null=True, blank=True)
    vendor_opt_date             = models.DateTimeField(null=True, blank=True)
    activity_code               = models.CharField(null=True, blank=True, max_length=100)
    article                     = models.CharField(null=True, blank=True, max_length=100)
    style_desc                  = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.CharField(null=True, blank=True, max_length=100)
    inline_type                 = models.CharField(null=True, blank=True, max_length=200)
    reason                      = models.TextField(null=True, blank=True)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    parent_to                   = models.IntegerField(blank=True, null=True)
    comment                     = models.TextField(null=True, blank=True)
    article_group               = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_inline'
        managed     = False

class InlineDefectlist(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)
    qty                         = models.IntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_inline_defect'
        indexes     = [
            models.Index(fields=['zone','defect','classification'])
        ]

class V_InlineDefectlist(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)
    qty                         = models.IntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_inline_defect'
        managed     = False

class InlinePointOfFocus(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_inline_pof'
        indexes     = [
            models.Index(fields=['value','focus_type','status'])
        ]

class V_InlinePointOfFocus(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_inline_pof'
        managed     = False


class InlineDefectlistAttachment(models.Model):
    inline                      = models.ForeignKey(InlineDefectlist, on_delete=models.CASCADE)
    defect_img                  = models.ImageField(upload_to="insp/inline/defect/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_inline_defect_attachment'

class V_InlineDefectlistAttachment(models.Model):
    inline                      = models.ForeignKey(InlineDefectlist, on_delete=models.CASCADE)
    defect_img                  = models.ImageField(upload_to="insp/inline/defect/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_inline_defect_attachment'
        managed     = False

class InspectionFinal(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    qty_output                  = models.IntegerField(null=True, blank=True)
    inspection_type             = models.CharField(null=True, blank=True, max_length=200)
    qty_carton                  = models.IntegerField(null=True, blank=True)
    qty_sample                  = models.IntegerField(null=True, blank=True)
    packing_qty                 = models.IntegerField(null=True, blank=True)
    result                      = models.CharField(null=True, blank=True, max_length=200)
    qty_critical                = models.IntegerField(null=True, blank=True)
    qty_minor                   = models.IntegerField(null=True, blank=True)
    qty_major                   = models.IntegerField(null=True, blank=True)
    qty_per_carton              = models.IntegerField(null=True, blank=True)
    grade_b_qty                 = models.IntegerField(null=True, blank=True)
    grade_c_qty                 = models.IntegerField(null=True, blank=True)
    carton_no                   = models.CharField(null=True, blank=True, max_length=200)
    barcode_carton              = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    qc_name                     = models.CharField(null=True, blank=True, max_length=200)
    qc_sign                     = models.TextField(null=True, blank=True)
    qc_date                     = models.DateTimeField(null=True, blank=True)
    vendor_pos                  = models.CharField(null=True, blank=True, max_length=200)
    vendor_name                 = models.CharField(null=True, blank=True, max_length=200)
    vendor_sign                 = models.TextField(null=True, blank=True)
    vendor_date                 = models.DateTimeField(null=True, blank=True)
    vendor_opt_pos              = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_name             = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_sign             = models.TextField(null=True, blank=True)
    vendor_opt_date             = models.DateTimeField(null=True, blank=True)
    final_type                  = models.CharField(null=True, blank=True, max_length=200)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    approval                    = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    discussion                  = models.CharField(null=True, blank=True, max_length=200)
    discussion_remark           = models.TextField(null=True, blank=True)
    approval_remark             = models.TextField(null=True, blank=True)
    comment                     = models.TextField(null=True, blank=True)
    reason                      = models.TextField(null=True, blank=True)
    cutting_report              = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_final'
        indexes     = [
            models.Index(fields=['io','id_transaction','result'])
        ]

class V_InspectionFinal(models.Model):
    io                          = models.IntegerField(null=True, blank=True)
    id_transaction              = models.CharField(null=True, blank=True, max_length=200)
    monitoring_detail           = models.ForeignKey(InspectionMonitoringDetail, on_delete=models.CASCADE)
    inspection_type             = models.CharField(null=True, blank=True, max_length=200)
    qty_output                  = models.IntegerField(null=True, blank=True)
    qty_carton                  = models.IntegerField(null=True, blank=True)
    qty_sample                  = models.IntegerField(null=True, blank=True)
    packing_qty                 = models.IntegerField(null=True, blank=True)
    result                      = models.CharField(null=True, blank=True, max_length=200)
    qty_critical                = models.IntegerField(null=True, blank=True)
    qty_minor                   = models.IntegerField(null=True, blank=True)
    qty_major                   = models.IntegerField(null=True, blank=True)
    qty_per_carton              = models.IntegerField(null=True, blank=True)
    grade_b_qty                 = models.IntegerField(null=True, blank=True)
    grade_c_qty                 = models.IntegerField(null=True, blank=True)
    carton_no                   = models.CharField(null=True, blank=True, max_length=200)
    barcode_carton              = models.CharField(null=True, blank=True, max_length=200)
    created                     = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated                     = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    qc_name                     = models.CharField(null=True, blank=True, max_length=200)
    qc_sign                     = models.TextField(null=True, blank=True)
    qc_date                     = models.DateTimeField(null=True, blank=True)
    vendor_pos                  = models.CharField(null=True, blank=True, max_length=200)
    vendor_name                 = models.CharField(null=True, blank=True, max_length=200)
    vendor_sign                 = models.TextField(null=True, blank=True)
    vendor_date                 = models.DateTimeField(null=True, blank=True)
    vendor_opt_pos              = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_name             = models.CharField(null=True, blank=True, max_length=200)
    vendor_opt_sign             = models.TextField(null=True, blank=True)
    vendor_opt_date             = models.DateTimeField(null=True, blank=True)
    activity_code               = models.IntegerField(null=True, blank=True)
    article                     = models.CharField(null=True, blank=True, max_length=100)
    style_desc                  = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.CharField(null=True, blank=True, max_length=100)
    final_type                  = models.CharField(null=True, blank=True, max_length=200)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=100)
    brand                       = models.CharField(null=True, blank=True, max_length=200)
    factory                     = models.CharField(null=True, blank=True, max_length=200)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    approval                    = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    discussion                  = models.CharField(null=True, blank=True, max_length=200)
    discussion_remark           = models.TextField(null=True, blank=True)
    approval_remark             = models.TextField(null=True, blank=True)
    parent_to                   = models.IntegerField(blank=True, null=True)
    comment                     = models.TextField(null=True, blank=True)
    article_group               = models.TextField(null=True, blank=True)
    reason                      = models.TextField(null=True, blank=True)
    cutting_report              = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final'
        managed     = False

class InspectionFinalAttachment(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    attachment                  = models.ImageField(upload_to="insp/final/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_final_attachment'
        indexes     = [
            models.Index(fields=['attachment'])
        ]

class V_InspectionFinalAttachment(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    attachment                  = models.ImageField(upload_to="insp/final/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_attachment'
        managed     = False

class InspectionFinalChecklist(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    category                    = models.CharField(null=True, blank=True, max_length=200)
    label                       = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.BooleanField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_final_checklist'
        indexes     = [
            models.Index(fields=['category','label'])
        ]

class V_InspectionFinalChecklist(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    category                    = models.CharField(null=True, blank=True, max_length=200)
    label                       = models.CharField(null=True, blank=True, max_length=200)
    value                       = models.BooleanField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_checklist'
        managed     = False


class FinalDefectlist(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)
    qty                         = models.IntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_final_defect'
        indexes     = [
            models.Index(fields=['zone','defect','classification'])
        ]

class V_FinalDefectlist(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    zone                        = models.CharField(null=True, blank=True, max_length=200)
    defect                      = models.CharField(null=True, blank=True, max_length=200)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    classification              = models.CharField(null=True, blank=True, max_length=200)
    qty                         = models.IntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_defect'
        managed     = False

class FinalDefectlistAttachment(models.Model):
    final                      = models.ForeignKey(FinalDefectlist, on_delete=models.CASCADE)
    defect_img                  = models.ImageField(upload_to="insp/final/defect/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_final_defect_attachment'

class V_FinalDefectlistAttachment(models.Model):
    final                      = models.ForeignKey(FinalDefectlist, on_delete=models.CASCADE)
    defect_img                  = models.ImageField(upload_to="insp/final/defect/", null=True, blank=True)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_defect_attachment'
        managed     = False

class MasterToleranceInspection(models.Model):
    brand =  models.CharField(null=True, blank=True, max_length=100)
    type  =  models.CharField(null=True, blank=True, max_length=100)
    category = models.CharField(null=True, blank=True, max_length=100)
    size = models.CharField(null=True, blank=True, max_length=10)
    min_tol = models.CharField(null=True, blank=True, max_length=10)
    max_tol = models.CharField(null=True, blank=True, max_length=10)

    class Meta:
        app_label = 'apps_inspection'
        db_table  = 'inspection_master_tolerance'


class V_InspectionWaitingApprove(models.Model):
    io = models.IntegerField(null=True, blank=True)
    id_transaction = models.CharField(null=True, blank=True, max_length=100)
    created_by     = models.CharField(null=True, blank=True, max_length=200)
    created_date   = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by     = models.CharField(null=True, blank=True, max_length=200)
    updated_date   = models.DateTimeField(editable=True, blank=True, null=True)
    monitoring_detail_id = models.IntegerField(null=True, blank=True)
    workflow_id       = models.IntegerField(null=True, blank=True)
    status_approval   = models.CharField(null=True, blank=True, max_length=200)
    approval          = models.CharField(null=True, blank=True, max_length=200)
    category          = models.CharField(null=True, blank=True, max_length=10)

    class Meta:
        app_label = 'apps_inspection'
        db_table  = 'v_inspection_approve'
        managed   = False

class InspectionDetailLog(models.Model):
    pic_nik = models.CharField(null=True, blank=True, max_length=200)
    title   = models.CharField(null=True, blank=True, max_length=200)
    json    = models.TextField(null=True, blank=True)
    status  = models.CharField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'apps_inspection'
        db_table  = 'inspection_detail_log'

class InspectionInlineActualMeasurement(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val_1                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_2                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_3                = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation_1                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_2                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_3                 = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_inline_measurement'
        indexes     = [
            models.Index(fields=['description','size_code'])
        ]

class V_InspectionInlineActualMeasurement(models.Model):
    inline                      = models.ForeignKey(InspectionInline, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val_1                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_2                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_3                = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation_1                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_2                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_3                 = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_inline_measurement'
        managed   = False


class InspectionFinalActualMeasurement(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val_1                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_2                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_3                = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation_1                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_2                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_3                 = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_final_measurement'
        indexes     = [
            models.Index(fields=['description','size_code'])
        ]

class V_InspectionFinalActualMeasurement(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    description                 = models.CharField(null=True, blank=True, max_length=200)
    size_code                   = models.CharField(null=True, blank=True, max_length=20)
    size_val                    = models.CharField(null=True, blank=True, max_length=200)
    actual_val_1                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_2                = models.CharField(null=True, blank=True, max_length=200)
    actual_val_3                = models.CharField(null=True, blank=True, max_length=200)
    tolerance_min               = models.CharField(null=True, blank=True, max_length=200)
    tolerance_max               = models.CharField(null=True, blank=True, max_length=200)
    deviation_1                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_2                 = models.CharField(null=True, blank=True, max_length=200)
    deviation_3                 = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_measurement'
        managed   = False

class FinalPointOfFocus(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'inspection_actual_final_pof'
        indexes     = [
            models.Index(fields=['value','focus_type','status'])
        ]

class V_FinalPointOfFocus(models.Model):
    final                       = models.ForeignKey(InspectionFinal, on_delete=models.CASCADE)
    value                       = models.CharField(null=True, blank=True, max_length=200)
    focus_type                  = models.CharField(null=True, blank=True, max_length=200)
    remark                      = models.TextField(null=True, blank=True)
    status                      = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_inspection'
        db_table    = 'v_inspection_actual_final_pof'
        managed     = False