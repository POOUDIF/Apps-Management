from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid


class FinanceTransaction(models.Model):
    activity_type = models.CharField(max_length=255, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    periode = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    created_by_name = models.CharField(max_length=255, null=True, blank=True)
    update_by = models.CharField(max_length=255, null=True, blank=True)
    update_by_name = models.CharField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, editable=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'finance_transaction'
        indexes     = [
            models.Index(fields=['transaction_id', 'created'])
        ]


class FinanceReportTaxReconcile(models.Model):
    activity_type = models.CharField(max_length=255)
    trans_id = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    serial_no = models.CharField(max_length=255, null=True, blank=True)
    debits = models.FloatField(null=True, blank=True)
    credits = models.FloatField(null=True, blank=True)
    ppn_gl = models.FloatField(null=True, blank=True)
    nsfp = models.CharField(max_length=255,null=True, blank=True)
    dpp = models.FloatField(null=True, blank=True)
    ppn = models.FloatField(null=True, blank=True)
    wapu = models.FloatField(null=True, blank=True)
    digunggung = models.FloatField(null=True, blank=True)
    selisih = models.FloatField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'v_finance_report_tax_reconcile'
        managed = False

class FinanceReportTaxReconcileVatIn(models.Model):
    activity_type = models.CharField(max_length=255)
    trans_id = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    serial_no = models.CharField(max_length=255, null=True, blank=True)
    debits = models.FloatField(null=True, blank=True)
    credits = models.FloatField(null=True, blank=True)
    ppn_gl = models.FloatField(null=True, blank=True)
    nsfp = models.CharField(max_length=255,null=True, blank=True)
    dpp = models.FloatField(null=True, blank=True)
    ppn = models.FloatField(null=True, blank=True)
    wapu = models.FloatField(null=True, blank=True)
    digunggung = models.FloatField(null=True, blank=True)
    selisih = models.FloatField(null=True, blank=True)
    dokumen_lain = models.FloatField(null=True, blank=True)
    belum_dikreditkan = models.FloatField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'v_finance_report_tax_reconcile_vatin'
        managed = False

class FinanceReportSalesEqualization(models.Model):
    activity_type = models.CharField(max_length=255)
    trans_id = models.IntegerField(null=True, blank=True)
    periode = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    serial_no = models.CharField(max_length=255, null=True, blank=True)
    debits = models.FloatField(null=True, blank=True)
    credits = models.FloatField(null=True, blank=True)
    ppn_gl = models.FloatField(null=True, blank=True)
    nsfp = models.CharField(max_length=255,null=True, blank=True)
    dpp = models.FloatField(null=True, blank=True)
    ppn = models.FloatField(null=True, blank=True)
    wapu = models.FloatField(null=True, blank=True)
    digunggung = models.FloatField(null=True, blank=True)
    selisih = models.FloatField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'v_finance_report_sales_equalization'
        managed = False

class FinanceTaxReconciNote(models.Model):
    transaction = models.ForeignKey(FinanceTransaction, on_delete=models.CASCADE)
    customer = models.CharField(max_length=255, null=True, blank=True)
    nsfp = models.CharField(max_length=255,null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        app_label = "apps_finance"
        db_table = "finance_tax_reconcile_note"

class FinanceMasterReconcileType(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'finance_master_reconcile_type'

