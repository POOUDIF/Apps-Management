from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid
from .master import *


class CustomerScreening(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name_customer               = models.CharField(null=True, blank=True, max_length=200)
    group_customer              = models.CharField(null=True, blank=True, max_length=200)
    company                     = models.ForeignKey(MasterCompany, on_delete=models.CASCADE)
    type                        = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.ForeignKey(MasterCustomerCategory, on_delete=models.CASCADE)
    screening_date              = models.DateField(null=True, blank=True)
    period_year                 = models.IntegerField(null=True, blank=True)
    period                      = models.ForeignKey(MasterReportingPeriod, on_delete=models.CASCADE)
    period_day                  = models.CharField(null=True, blank=True, max_length=200)
    result_total                = models.CharField(null=True, blank=True, max_length=200)
    total                       = models.BigIntegerField(null=True, blank=True)
    persediaan                  = models.BigIntegerField(null=True, blank=True)
    piutang_usaha               = models.BigIntegerField(null=True, blank=True)
    hutang_usaha                = models.BigIntegerField(null=True, blank=True)
    aset_lancar                 = models.BigIntegerField(null=True, blank=True)
    hutang_lancar               = models.BigIntegerField(null=True, blank=True)
    pendapatan                  = models.BigIntegerField(null=True, blank=True)
    harga_pokok_jual            = models.BigIntegerField(null=True, blank=True)
    file_laporan_keuangan       = models.FileField(upload_to='screening-keuangan',blank=True, null=True)
    file_name_keuangan          = models.CharField(null=True, blank=True, max_length=250)
    nilai_order_customer        = models.BigIntegerField(null=True, blank=True)
    est_gp_order                = models.BigIntegerField(null=True, blank=True)
    total_order                 = models.BigIntegerField(null=True, blank=True)
    standard_gp                 = models.BigIntegerField(null=True, blank=True)
    standard_gp_val             = models.BigIntegerField(null=True, blank=True)
    dp_val                      = models.BigIntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)
    file_perhitungan            = models.FileField(upload_to='screening-perhitungan',blank=True, null=True)
    file_perhitungan_name       = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    approver                    = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_screening'
        indexes     = [
            models.Index(fields=['code', 'name_customer','screening_date','period_year','result_total','total'])
        ]


class CustomerScreeningLog(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name_customer               = models.CharField(null=True, blank=True, max_length=200)
    group_customer              = models.CharField(null=True, blank=True, max_length=200)
    company                     = models.ForeignKey(MasterCompany, on_delete=models.CASCADE)
    type                        = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.ForeignKey(MasterCustomerCategory, on_delete=models.CASCADE)
    screening_date              = models.DateField(null=True, blank=True)
    period_year                 = models.IntegerField(null=True, blank=True)
    period                      = models.ForeignKey(MasterReportingPeriod, on_delete=models.CASCADE)
    period_day                  = models.CharField(null=True, blank=True, max_length=200)
    result_total                = models.CharField(null=True, blank=True, max_length=200)
    total                       = models.BigIntegerField(null=True, blank=True)
    persediaan                  = models.BigIntegerField(null=True, blank=True)
    piutang_usaha               = models.BigIntegerField(null=True, blank=True)
    hutang_usaha                = models.BigIntegerField(null=True, blank=True)
    aset_lancar                 = models.BigIntegerField(null=True, blank=True)
    hutang_lancar               = models.BigIntegerField(null=True, blank=True)
    pendapatan                  = models.BigIntegerField(null=True, blank=True)
    harga_pokok_jual            = models.BigIntegerField(null=True, blank=True)
    file_name_keuangan          = models.CharField(null=True, blank=True, max_length=250)
    nilai_order_customer        = models.BigIntegerField(null=True, blank=True)
    est_gp_order                = models.BigIntegerField(null=True, blank=True)
    total_order                 = models.BigIntegerField(null=True, blank=True)
    standard_gp                 = models.BigIntegerField(null=True, blank=True)
    standard_gp_val             = models.BigIntegerField(null=True, blank=True)
    dp_val                      = models.BigIntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)
    file_perhitungan_name       = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)
    workflow_id                 = models.IntegerField(null=True, blank=True)
    approver                    = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_screening_log'
        indexes     = [
            models.Index(fields=['code', 'name_customer','screening_date','period_year','result_total','total'])
        ]

class CustomerScreeningApproval(models.Model):
    screening                   = models.ForeignKey(CustomerScreening, on_delete=models.CASCADE)
    approver                    = models.CharField(null=True, blank=True, max_length=200)
    approver_name               = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    comment                     = models.TextField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_screening_approval'
        indexes     = [
            models.Index(fields=['approver', 'status','comment'])
        ]

class CustomerScreeningTableCriteria(models.Model):
    screening                   = models.ForeignKey(CustomerScreening, on_delete=models.CASCADE)
    no                          = models.IntegerField(null=True, blank=True)
    criteria                    = models.CharField(null=True, blank=True, max_length=200)
    criteria_det                = models.CharField(null=True, blank=True, max_length=200)
    var_2                       = models.CharField(null=True, blank=True, max_length=200)
    var_1                       = models.CharField(null=True, blank=True, max_length=200)
    var_0                       = models.CharField(null=True, blank=True, max_length=200)
    value_input                 = models.CharField(null=True, blank=True, max_length=200)
    val_score                   = models.CharField(null=True, blank=True, max_length=200)
    type_data                   = models.CharField(null=True, blank=True, max_length=200)
    condition                   = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'cm_screening_table_criteria'
        indexes     = [
            models.Index(fields=['criteria', 'criteria_det','value_input','val_score'])
        ]


class V_CustomerScreening(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name_customer               = models.CharField(null=True, blank=True, max_length=200)
    group_customer              = models.CharField(null=True, blank=True, max_length=200)
    company                     = models.ForeignKey(MasterCompany, on_delete=models.CASCADE)
    company_name                = models.CharField(null=True, blank=True, max_length=200)
    type                        = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.ForeignKey(MasterCustomerCategory, on_delete=models.CASCADE)
    screening_date              = models.DateField(null=True, blank=True)
    period_year                 = models.IntegerField(null=True, blank=True)
    period                      = models.ForeignKey(MasterReportingPeriod, on_delete=models.CASCADE)
    period_day                  = models.CharField(null=True, blank=True, max_length=200)
    result_total                = models.CharField(null=True, blank=True, max_length=200)
    total                       = models.BigIntegerField(null=True, blank=True)
    persediaan                  = models.BigIntegerField(null=True, blank=True)
    piutang_usaha               = models.BigIntegerField(null=True, blank=True)
    hutang_usaha                = models.BigIntegerField(null=True, blank=True)
    aset_lancar                 = models.BigIntegerField(null=True, blank=True)
    hutang_lancar               = models.BigIntegerField(null=True, blank=True)
    pendapatan                  = models.BigIntegerField(null=True, blank=True)
    harga_pokok_jual            = models.BigIntegerField(null=True, blank=True)
    file_laporan_keuangan       = models.FileField(upload_to='screening-keuangan',blank=True, null=True)
    file_name_keuangan          = models.CharField(null=True, blank=True, max_length=250)
    nilai_order_customer        = models.BigIntegerField(null=True, blank=True)
    est_gp_order                = models.BigIntegerField(null=True, blank=True)
    total_order                 = models.BigIntegerField(null=True, blank=True)
    standard_gp                 = models.BigIntegerField(null=True, blank=True)
    standard_gp_val             = models.BigIntegerField(null=True, blank=True)
    dp_val                      = models.BigIntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)
    file_perhitungan            = models.FileField(upload_to='screening-perhitungan',blank=True, null=True)
    file_perhitungan_name       = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)
    approver                    = models.CharField(null=True, blank=True, max_length=200)
    workflow_id                 = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_screening'
        managed     = False

class V_CustomerScreeningLog(models.Model):
    code                        = models.CharField(null=True, blank=True, max_length=200)
    name_customer               = models.CharField(null=True, blank=True, max_length=200)
    group_customer              = models.CharField(null=True, blank=True, max_length=200)
    company                     = models.ForeignKey(MasterCompany, on_delete=models.CASCADE)
    type                        = models.CharField(null=True, blank=True, max_length=200)
    category                    = models.ForeignKey(MasterCustomerCategory, on_delete=models.CASCADE)
    screening_date              = models.DateField(null=True, blank=True)
    period_year                 = models.IntegerField(null=True, blank=True)
    period                      = models.ForeignKey(MasterReportingPeriod, on_delete=models.CASCADE)
    period_day                  = models.CharField(null=True, blank=True, max_length=200)
    result_total                = models.CharField(null=True, blank=True, max_length=200)
    total                       = models.BigIntegerField(null=True, blank=True)
    persediaan                  = models.BigIntegerField(null=True, blank=True)
    piutang_usaha               = models.BigIntegerField(null=True, blank=True)
    hutang_usaha                = models.BigIntegerField(null=True, blank=True)
    aset_lancar                 = models.BigIntegerField(null=True, blank=True)
    hutang_lancar               = models.BigIntegerField(null=True, blank=True)
    pendapatan                  = models.BigIntegerField(null=True, blank=True)
    harga_pokok_jual            = models.BigIntegerField(null=True, blank=True)
    file_laporan_keuangan       = models.FileField(upload_to='screening-keuangan',blank=True, null=True)
    file_name_keuangan          = models.CharField(null=True, blank=True, max_length=250)
    nilai_order_customer        = models.BigIntegerField(null=True, blank=True)
    est_gp_order                = models.BigIntegerField(null=True, blank=True)
    total_order                 = models.BigIntegerField(null=True, blank=True)
    standard_gp                 = models.BigIntegerField(null=True, blank=True)
    standard_gp_val             = models.BigIntegerField(null=True, blank=True)
    dp_val                      = models.BigIntegerField(null=True, blank=True)
    remark                      = models.TextField(null=True, blank=True)
    file_perhitungan            = models.FileField(upload_to='screening-perhitungan',blank=True, null=True)
    file_perhitungan            = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    status_approval             = models.CharField(null=True, blank=True, max_length=200)
    is_active                   = models.BooleanField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_screening_log'
        managed     = False

class V_CustomerScreeningApproval(models.Model):
    screening                   = models.ForeignKey(CustomerScreening, on_delete=models.CASCADE)
    approver                    = models.CharField(null=True, blank=True, max_length=200)
    approver_name               = models.CharField(null=True, blank=True, max_length=250)
    status                      = models.CharField(null=True, blank=True, max_length=200)
    comment                     = models.TextField(null=True, blank=True)
    created_by                  = models.CharField(null=True, blank=True, max_length=200)
    created_at                  = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated_by                  = models.CharField(null=True, blank=True, max_length=200)
    updated_at                  = models.DateTimeField(editable=True, blank=True, null=True)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_screening_approval'
        managed     = False

class V_CustomerScreeningTableCriteria(models.Model):
    screening                   = models.ForeignKey(CustomerScreening, on_delete=models.CASCADE)
    no                          = models.IntegerField(null=True, blank=True)
    criteria                    = models.CharField(null=True, blank=True, max_length=200)
    criteria_det                = models.CharField(null=True, blank=True, max_length=200)
    var_2                       = models.CharField(null=True, blank=True, max_length=200)
    var_1                       = models.CharField(null=True, blank=True, max_length=200)
    var_0                       = models.CharField(null=True, blank=True, max_length=200)
    value_input                 = models.CharField(null=True, blank=True, max_length=200)
    val_score                   = models.CharField(null=True, blank=True, max_length=200)
    type_data                   = models.CharField(null=True, blank=True, max_length=200)
    condition                   = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        app_label   = 'apps_customer_management'
        db_table    = 'v_cm_screening_table_criteria'
        managed     = False