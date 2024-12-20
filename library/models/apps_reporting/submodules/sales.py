from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver


class SalesSummary(models.Model):
    order_date              = models.DateField(primary_key=True)
    transaksi_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_pos        = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_dep_store  = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_ecom       = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_transaksi         = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty               = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier            = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)

    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'sales_summary'
        managed     = False

class SalesSummaryCN(models.Model):
    order_date              = models.DateTimeField(primary_key=True)
    total_qty               = models.IntegerField()
    nett_cashier            = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)

    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'report_odoo_ssr'
        managed     = False

class SalesMonthlySummary(models.Model):
    order_month              = models.CharField(max_length=220,primary_key=True)
    transaksi_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_pos        = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_dep_store  = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_ecom       = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_transaksi         = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty               = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier            = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)

    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'sales_summary_monthly'
        managed     = False

class SalesYearlySummary(models.Model):
    # order_year              = models.CharField(max_length=220)
    order_year              = models.CharField(max_length=220,primary_key=True)
    transaksi_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_pos        = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_dep_store  = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_ecom       = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_transaksi         = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty               = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier            = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)

    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'sales_summary_yearly'
        managed     = False

class SalesQuarterlySummary(models.Model):
    get_quarter             = models.CharField(max_length=220,primary_key=True)
    order_year              = models.CharField(max_length=220)
    quarterly                = models.CharField(max_length=220)
    transaksi_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    transaksi_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_pos           = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_dep_store     = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty_ecom          = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_pos        = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_dep_store  = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier_ecom       = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_transaksi         = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    total_qty               = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)
    nett_cashier            = models.DecimalField(decimal_places=2,max_digits=9, null=True, blank=True)

    class Meta:
        app_label   = 'apps_warehouse'
        db_table    = 'sales_summary_quarterly'
        managed     = False

