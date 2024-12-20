from __future__ import unicode_literals
from django.db import models, transaction, IntegrityError
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os
import uuid

class ScanFaktur(models.Model):
    kd_jenis_trx = models.CharField(max_length=5, null=True)
    fg_pengganti = models.CharField(max_length=5, null=True)
    no_faktur = models.CharField(max_length=20, null=True)
    tgl_faktur = models.DateField(default=None, null=True, blank=True)
    npwp_penjual = models.CharField(max_length=20, null=True)
    nama_penjual = models.CharField(max_length=300, null=True)
    alamat_penjual = models.CharField(max_length=300, null=True)
    npwp_lawan_trx = models.CharField(max_length=20, null=True)
    nama_lawan_trx = models.CharField(max_length=300, null=True)
    alamat_lawan_trx = models.CharField(max_length=300, null=True)
    jmlh_dpp = models.FloatField(default=0, null=True)
    jmlh_ppn = models.FloatField(default=0, null=True)
    jmlh_ppnbm = models.FloatField(default=0, null=True)
    status_approval = models.CharField(max_length=50, null=True)
    status_faktur = models.CharField(max_length=50, null=True)
    is_credit = models.BooleanField(default=True)
    refrensi = models.CharField(max_length=50, null=True)
    scan_by = models.CharField(max_length=50, null=True)
    scan_at = models.DateTimeField(default=None, null=True, blank=True)
    export_by = models.CharField(max_length=50, null=True)
    export_at = models.DateTimeField(default=None, null=True, blank=True)
    masa_pajak_month = models.CharField(max_length=50, null=True)
    masa_pajak_year = models.CharField(max_length=50, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label = 'apps_finance'
        db_table = 'scan_faktur'
class ScanFakturDashboard(models.Model):
    kd_jenis_trx = models.CharField(max_length=5, null=True)
    fg_pengganti = models.CharField(max_length=5, null=True)
    no_faktur = models.CharField(max_length=20, null=True)
    tgl_faktur = models.DateField(default=None, null=True, blank=True)
    npwp_penjual = models.CharField(max_length=20, null=True)
    nama_penjual = models.CharField(max_length=300, null=True)
    alamat_penjual = models.CharField(max_length=300, null=True)
    npwp_lawan_trx = models.CharField(max_length=20, null=True)
    nama_lawan_trx = models.CharField(max_length=300, null=True)
    alamat_lawan_trx = models.CharField(max_length=300, null=True)
    jmlh_dpp = models.FloatField(default=0, null=True)
    jmlh_ppn = models.FloatField(default=0, null=True)
    jmlh_ppnbm = models.FloatField(default=0, null=True)
    status_approval = models.CharField(max_length=50, null=True)
    status_faktur = models.CharField(max_length=50, null=True)
    is_credit = models.BooleanField(default=True)
    refrensi = models.CharField(max_length=50, null=True)
    scan_by = models.CharField(max_length=50, null=True)
    scan_at = models.DateTimeField(default=None, null=True, blank=True)
    export_by = models.CharField(max_length=50, null=True)
    export_at = models.DateTimeField(default=None, null=True, blank=True)
    masa_pajak_month = models.CharField(max_length=50, null=True)
    masa_pajak_year = models.CharField(max_length=50, null=True)
    no_seri = models.CharField(max_length=50, null=True)
    pengganti = models.CharField(max_length=50, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        managed = False
        app_label = 'apps_finance'
        db_table = 'v_dashboard_faktur'
class DetailTransaksi(models.Model):
    faktur = models.ForeignKey(ScanFaktur, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length=300, null=True)
    harga_satuan = models.FloatField(default=0, null=True)
    jmlh_barang = models.IntegerField(default=0, null=True)
    harga_total = models.FloatField(default=0, null=True)
    diskon = models.FloatField(default=0, null=True)
    dpp = models.FloatField(default=0, null=True)
    ppn = models.FloatField(default=0, null=True)
    tarif_ppnbm = models.FloatField(default=0, null=True)
    ppnbm = models.FloatField(default=0, null=True)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=None, null=True, blank=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_by = models.CharField(max_length=50, null=True, default=None)
    deleted_at = models.DateTimeField(null=True, default=None)
    class Meta:
        app_label = 'apps_finance'
        db_table = 'detail_transaksi'