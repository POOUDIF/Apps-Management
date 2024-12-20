from django.db import models
from django.utils import timezone
from library.models.bbicore.submodels.base import BaseModelApps

class MarketingPlan(models.Model):
    brand       = models.CharField(max_length=50)
    year        = models.CharField(max_length=50)
    status      = models.CharField(max_length=50,null=True)
    total       = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    modifiy_at  = models.DateTimeField(auto_now_add=True)
    created_by  = models.IntegerField()
    modify_by   = models.IntegerField()
    id_workflow = models.IntegerField(null=True)

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'marketing_plan'


class MarketingPlanDetail(models.Model):
    id_marketing_plan = models.ForeignKey(MarketingPlan,on_delete=models.CASCADE)
    sub_brand         = models.CharField(max_length=50)
    collection        = models.CharField(max_length=50)
    total             = models.IntegerField()

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'marketing_plan_detail'


class MarketingPlanMonth(models.Model):
    id_marketing_plan_detail = models.ForeignKey(MarketingPlanDetail,on_delete=models.CASCADE)
    category                 = models.CharField(max_length=50)
    January                  = models.IntegerField(null=True)
    February                 = models.IntegerField(null=True)
    March                    = models.IntegerField(null=True)
    April                    = models.IntegerField(null=True)
    May                      = models.IntegerField(null=True)
    June                     = models.IntegerField(null=True)
    July                     = models.IntegerField(null=True)
    August                   = models.IntegerField(null=True)
    September                = models.IntegerField(null=True)
    October                  = models.IntegerField(null=True)
    November                 = models.IntegerField(null=True)
    December                 = models.IntegerField(null=True)
    January_qty              = models.IntegerField(null=True)
    February_qty             = models.IntegerField(null=True)
    March_qty                = models.IntegerField(null=True)
    April_qty                = models.IntegerField(null=True)
    May_qty                  = models.IntegerField(null=True)
    June_qty                 = models.IntegerField(null=True)
    July_qty                 = models.IntegerField(null=True)
    August_qty               = models.IntegerField(null=True)
    September_qty            = models.IntegerField(null=True)
    October_qty              = models.IntegerField(null=True)
    November_qty             = models.IntegerField(null=True)
    December_qty             = models.IntegerField(null=True)
    rollin_January           = models.IntegerField(null=True)
    rollin_February          = models.IntegerField(null=True)
    rollin_March             = models.IntegerField(null=True)
    rollin_April             = models.IntegerField(null=True)
    rollin_May               = models.IntegerField(null=True)
    rollin_June              = models.IntegerField(null=True)
    rollin_July              = models.IntegerField(null=True)
    rollin_August            = models.IntegerField(null=True)
    rollin_September         = models.IntegerField(null=True)
    rollin_October           = models.IntegerField(null=True)
    rollin_November          = models.IntegerField(null=True)
    rollin_December          = models.IntegerField(null=True)
    rollin_January_qty       = models.IntegerField(null=True)
    rollin_February_qty      = models.IntegerField(null=True)
    rollin_March_qty         = models.IntegerField(null=True)
    rollin_April_qty         = models.IntegerField(null=True)
    rollin_May_qty           = models.IntegerField(null=True)
    rollin_June_qty          = models.IntegerField(null=True)
    rollin_July_qty          = models.IntegerField(null=True)
    rollin_August_qty        = models.IntegerField(null=True)
    rollin_September_qty     = models.IntegerField(null=True)
    rollin_October_qty       = models.IntegerField(null=True)
    rollin_November_qty      = models.IntegerField(null=True)
    rollin_December_qty      = models.IntegerField(null=True)
    actual_January           = models.IntegerField(null=True)
    actual_February          = models.IntegerField(null=True)
    actual_March             = models.IntegerField(null=True)
    actual_April             = models.IntegerField(null=True)
    actual_May               = models.IntegerField(null=True)
    actual_June              = models.IntegerField(null=True)
    actual_July              = models.IntegerField(null=True)
    actual_August            = models.IntegerField(null=True)
    actual_September         = models.IntegerField(null=True)
    actual_October           = models.IntegerField(null=True)
    actual_November          = models.IntegerField(null=True)
    actual_December          = models.IntegerField(null=True)
    actual_January_qty       = models.IntegerField(null=True)
    actual_February_qty      = models.IntegerField(null=True)
    actual_March_qty         = models.IntegerField(null=True)
    actual_April_qty         = models.IntegerField(null=True)
    actual_May_qty           = models.IntegerField(null=True)
    actual_June_qty          = models.IntegerField(null=True)
    actual_July_qty          = models.IntegerField(null=True)
    actual_August_qty        = models.IntegerField(null=True)
    actual_September_qty     = models.IntegerField(null=True)
    actual_October_qty       = models.IntegerField(null=True)
    actual_November_qty      = models.IntegerField(null=True)
    actual_December_qty      = models.IntegerField(null=True)
    rollin_total             = models.IntegerField(null=True)
    actual_total             = models.IntegerField(null=True)
    total                    = models.IntegerField(null=True)
    kode_marketing_plan      = models.CharField(max_length=50)

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'marketing_plan_month'


class MarketingPlanCalCheckPoint(models.Model):
    id_marketing_plan_detail = models.ForeignKey(MarketingPlan,on_delete=models.CASCADE)
    description              = models.CharField(max_length=100, null=True)
    check_point              = models.CharField(max_length=150, null=True)
    collection               = models.CharField(max_length=150, null=True)
    year                     = models.CharField(max_length=50, null=True)
    month                    = models.CharField(max_length=50, null=True)
    dept                     = models.CharField(max_length=50, null=True)
    total_per_month          = models.IntegerField(null=True)
    lead_time_notif          = models.CharField(max_length=50, null=True)
    lead_time                = models.CharField(max_length=50, null=True)
    id_master                = models.IntegerField(null=True)
    type                     = models.CharField(max_length=150, null=True)
    step                     = models.IntegerField(null=True)

    class Meta:
        app_label = 'apps_plm'
        db_table  = 'marketing_plan_calc_checkpoint'


class V_MarketingPlanMonth(models.Model):
    # id                      = models.IntegerField(null=True)
    brand                       = models.CharField(max_length=100, null=True)
    year                        = models.IntegerField(null=True)
    status                      = models.CharField(max_length=100, null=True)
    total                       = models.IntegerField(null=True)
    id_workflow                 = models.IntegerField(null=True)
    sub_brand                   = models.CharField(max_length=100, null=True)
    category                    = models.CharField(max_length=100, null=True)
    total_per_sub_brand         = models.IntegerField(null=True)
    total_per_category          = models.IntegerField(null=True)
    rollin_total_per_category   = models.IntegerField(null=True)
    actual_total_per_category   = models.IntegerField(null=True)
    id_marketing_plan_id        = models.IntegerField(null=True)
    id_marketing_plan_month     = models.IntegerField(null=True)
    id_marketing_plan_detail    = models.IntegerField(null=True)
    January                     = models.IntegerField(null=True)
    February                    = models.IntegerField(null=True)
    March                       = models.IntegerField(null=True)
    April                       = models.IntegerField(null=True)
    May                         = models.IntegerField(null=True)
    June                        = models.IntegerField(null=True)
    July                        = models.IntegerField(null=True)
    August                      = models.IntegerField(null=True)
    September                   = models.IntegerField(null=True)
    October                     = models.IntegerField(null=True)
    November                    = models.IntegerField(null=True)
    December                    = models.IntegerField(null=True)
    January_qty                 = models.IntegerField(null=True)
    February_qty                = models.IntegerField(null=True)
    March_qty                   = models.IntegerField(null=True)
    April_qty                   = models.IntegerField(null=True)
    May_qty                     = models.IntegerField(null=True)
    June_qty                    = models.IntegerField(null=True)
    July_qty                    = models.IntegerField(null=True)
    August_qty                  = models.IntegerField(null=True)
    September_qty               = models.IntegerField(null=True)
    October_qty                 = models.IntegerField(null=True)
    November_qty                = models.IntegerField(null=True)
    December_qty                = models.IntegerField(null=True)
    rollin_January              = models.IntegerField(null=True)
    rollin_February             = models.IntegerField(null=True)
    rollin_March                = models.IntegerField(null=True)
    rollin_April                = models.IntegerField(null=True)
    rollin_May                  = models.IntegerField(null=True)
    rollin_June                 = models.IntegerField(null=True)
    rollin_July                 = models.IntegerField(null=True)
    rollin_August               = models.IntegerField(null=True)
    rollin_September            = models.IntegerField(null=True)
    rollin_October              = models.IntegerField(null=True)
    rollin_November             = models.IntegerField(null=True)
    rollin_December             = models.IntegerField(null=True)
    rollin_January_qty          = models.IntegerField(null=True)
    rollin_February_qty         = models.IntegerField(null=True)
    rollin_March_qty            = models.IntegerField(null=True)
    rollin_April_qty            = models.IntegerField(null=True)
    rollin_May_qty              = models.IntegerField(null=True)
    rollin_June_qty             = models.IntegerField(null=True)
    rollin_July_qty             = models.IntegerField(null=True)
    rollin_August_qty           = models.IntegerField(null=True)
    rollin_September_qty        = models.IntegerField(null=True)
    rollin_October_qty          = models.IntegerField(null=True)
    rollin_November_qty         = models.IntegerField(null=True)
    rollin_December_qty         = models.IntegerField(null=True)
    actual_January              = models.IntegerField(null=True)
    actual_February             = models.IntegerField(null=True)
    actual_March                = models.IntegerField(null=True)
    actual_April                = models.IntegerField(null=True)
    actual_May                  = models.IntegerField(null=True)
    actual_June                 = models.IntegerField(null=True)
    actual_July                 = models.IntegerField(null=True)
    actual_August               = models.IntegerField(null=True)
    actual_September            = models.IntegerField(null=True)
    actual_October              = models.IntegerField(null=True)
    actual_November             = models.IntegerField(null=True)
    actual_December             = models.IntegerField(null=True)
    actual_January_qty          = models.IntegerField(null=True)
    actual_February_qty         = models.IntegerField(null=True)
    actual_March_qty            = models.IntegerField(null=True)
    actual_April_qty            = models.IntegerField(null=True)
    actual_May_qty              = models.IntegerField(null=True)
    actual_June_qty             = models.IntegerField(null=True)
    actual_July_qty             = models.IntegerField(null=True)
    actual_August_qty           = models.IntegerField(null=True)
    actual_September_qty        = models.IntegerField(null=True)
    actual_October_qty          = models.IntegerField(null=True)
    actual_November_qty         = models.IntegerField(null=True)
    actual_December_qty         = models.IntegerField(null=True)
    total_month                 = models.IntegerField(null=True)

    class Meta:
        managed     = False
        app_label   = 'apps_plm'
        db_table    = 'v_marketing_plan_month'


class TrMarketingPlan(BaseModelApps):
    marketing_plan              = models.IntegerField(null=True)
    year                        = models.IntegerField(null=True)
    month                       = models.CharField(null=True, max_length=50)
    doc_src                     = models.FileField(upload_to="doc-mktplan/", blank=True, null=True)
    doc_name                    = models.TextField(null=True)
    status                      = models.CharField(null=True, max_length=100)
    brand                       = models.CharField(null=True, max_length=100)
        
    class Meta:
        app_label = 'apps_plm'
        db_table  = 'tr_marketing_plan'


class TrMarketingPlanFile(BaseModelApps):
    tr_marketing_plan           = models.ForeignKey(TrMarketingPlan,on_delete=models.CASCADE)
    doc_src                     = models.FileField(upload_to="doc-mktplan/", blank=True, null=True)
    doc_name                    = models.TextField(null=True)
    status                      = models.CharField(null=True, max_length=100)
        
    class Meta:
        app_label = 'apps_plm'
        db_table  = 'tr_marketing_plan_file'


class HistoryMktPlan(BaseModelApps):
    id_transaction              = models.IntegerField()
    brand                       = models.CharField(null=True, max_length=100)
    subbrand                    = models.CharField(null=True, max_length=100)
    category                    = models.CharField(null=True, max_length=100)
    type                        = models.CharField(null=True, max_length=100)
    from_dt                     = models.TextField(null=True)
    to_dt                       = models.TextField(null=True)
    name                        = models.CharField(null=True, max_length=200)
        
    class Meta:
        app_label = 'apps_plm'
        db_table  = 'history_mkt_plan'


class RemarkHistoryMktPlan(BaseModelApps):
    id_transaction    = models.IntegerField()
    data              = models.TextField(null=True)
        
    class Meta:
        app_label = 'apps_plm'
        db_table  = 'remark_history_mkt_plan'
