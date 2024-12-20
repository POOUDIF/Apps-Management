from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid
from .report import FinanceTransaction

class FinanceTaxReconcile(models.Model):
    tax_code = models.CharField(max_length=255, null=True, blank=True)
    tax_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    transaction = models.ForeignKey(FinanceTransaction, on_delete=models.CASCADE)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'finance_transaction_tax_reconcile'

class FinanceReconcileGLDetail(models.Model):
    reconcile = models.ForeignKey(FinanceTaxReconcile, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True)
    accounting = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    serial_no = models.CharField(max_length=255, null=True, blank=True)
    doc_num = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    debits = models.FloatField(null=True, blank=True)
    credits = models.FloatField(null=True, blank=True)
    customer_type = models.CharField(max_length=255, null=True, blank=True)
    supplier_type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'finance_reconcile_gl_detail'

class FinanceReconcileEfakturDetail(models.Model):
    reconcile = models.ForeignKey(FinanceTaxReconcile, on_delete=models.CASCADE)
    npwp = models.CharField(max_length=255, null=True, blank=True)
    customer = models.CharField(max_length=255, null=True, blank=True)
    code_faktur = models.CharField(max_length=255, null=True, blank=True)
    nsfp = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    masa = models.CharField(max_length=255, null=True, blank=True)
    tahun = models.CharField(max_length=255, null=True, blank=True)
    tgl_faktur = models.DateField(null=True, default=None)
    status = models.CharField(max_length=255, null=True, blank=True)
    dpp = models.FloatField(null=True, blank=True)
    ppn = models.FloatField(null=True, blank=True)

    class Meta:
        app_label = 'apps_finance'
        db_table = 'finance_reconcile_efaktur_detail'