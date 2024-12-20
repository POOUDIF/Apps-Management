from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver


class PnlSummary(models.Model):
    periode                         = models.CharField(max_length=500, blank=True, null=True,primary_key=True)
    counter                         = models.CharField(max_length=500, blank=True, null=True)
    brand                           = models.CharField(max_length=500, blank=True, null=True)
    new_channel                     = models.CharField(max_length=500, blank=True, null=True)
    qty                             = models.CharField(max_length=500, blank=True, null=True)
    gross                           = models.CharField(max_length=500, blank=True, null=True)
    dpp                             = models.CharField(max_length=500, blank=True, null=True)
    ppn                             = models.CharField(max_length=500, blank=True, null=True)
    nett                            = models.CharField(max_length=500, blank=True, null=True)
    nett_cashier                    = models.CharField(max_length=500, blank=True, null=True)
    gross_margin                    = models.CharField(max_length=500, blank=True, null=True)
    cogs                            = models.CharField(max_length=500, blank=True, null=True)
    gross_profit                    = models.CharField(max_length=500, blank=True, null=True)
    amount_salaries                 = models.CharField(max_length=500, blank=True, null=True)
    amount_overtime                 = models.CharField(max_length=500, blank=True, null=True)
    amount_allowance                = models.CharField(max_length=500, blank=True, null=True)
    amount_commision_insentive      = models.CharField(max_length=500, blank=True, null=True)
    amount_jamsostek_jkk_jkm        = models.CharField(max_length=500, blank=True, null=True)
    amount_jamsostek_jht            = models.CharField(max_length=500, blank=True, null=True)
    amount_pension_expense          = models.CharField(max_length=500, blank=True, null=True)
    amount_bpjs_kesehatan           = models.CharField(max_length=500, blank=True, null=True)
    amount_trans_travell            = models.CharField(max_length=500, blank=True, null=True)
    amount_advertising_promotion    = models.CharField(max_length=500, blank=True, null=True)
    amount_repair_maintenance       = models.CharField(max_length=500, blank=True, null=True)
    amount_utilities_energy         = models.CharField(max_length=500, blank=True, null=True)
    amount_communication            = models.CharField(max_length=500, blank=True, null=True)
    amount_office_expense           = models.CharField(max_length=500, blank=True, null=True)
    amount_handling                 = models.CharField(max_length=500, blank=True, null=True)
    amount_handling_document        = models.CharField(max_length=500, blank=True, null=True)
    amount_proffesional_fee         = models.CharField(max_length=500, blank=True, null=True)
    amount_tax_licence              = models.CharField(max_length=500, blank=True, null=True)
    amount_rent_expense             = models.CharField(max_length=500, blank=True, null=True)
    amount_indirect_material        = models.CharField(max_length=500, blank=True, null=True)
    amount_house_hold               = models.CharField(max_length=500, blank=True, null=True)
    amount_depreciation             = models.CharField(max_length=500, blank=True, null=True)
    # amount_dep_hak_asset_guna       = models.CharField(max_length=500, blank=True, null=True)
    total_opex                      = models.CharField(max_length=500, blank=True, null=True)
    npam                            = models.CharField(max_length=500, blank=True, null=True)
    other_expense                   = models.CharField(max_length=500, blank=True, null=True)
    
    
    class Meta:
        # app_label   = 'apps_etl'
        # db_table    = 'v_report_pnl'
        app_label   = 'apps_warehouse'
        db_table    = 'v_report_pnl'
        managed     = False
