# source : https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477
from os import system
from django.conf import settings


APP_DB_MAPPING  = {
    # Format = "apps_name / module_name" : "db_name" (based on env)
    "bbicore" : "db_coreapps",
    "bbi_token" : "db_auth",
    "apps_form" : "db_form",
    "apps_plm" : "db_plm",
    "apps_reporting" : "db_reporting",
    "apps_dms" : "db_dms",
    "apps_workflow" : "db_wf",
    "apps_salesforce" : "db_salesforce",
    "apps_inspection" : "db_inspection",
    "apps_master" : "db_master",
    "apps_warehouse" : "db_warehouse",
    "apps_integration" : "db_integration",
    "hris_master" : "db_hrismaster",
    "hris_warehouse" : "db_hriswarehouse",
    "apps_etl" : "etl",
    "apps_notification" : "db_notif",
    "apps_odoo_addons" : "db_odoo_addons",
    "apps_old" : "db_old",
    "apps_finance" : "db_finance",
    "apps_lms" : "db_lms",
    "apps_vendor_management" : "db_vendor_management",
    "apps_master": "db_master",
    "bbi_api": "db_bbi_api",
    "apps_customer_management":"db_customer_management",
    "apps_e2e" : "db_e2e",
    "apps_office_management" : "db_office_management",

}

class DatabaseRouter(object):
    # DB READ : Point all operations on to their respective db setting
    def db_for_read(self, model, **hints):
        return APP_DB_MAPPING.get(model._meta.app_label, 'default')

    # DB CREATE/UPDATE/DELETE : Point all operations on to their respective db setting
    def db_for_write(self, model, **hints):
        return APP_DB_MAPPING.get(model._meta.app_label, 'default')

    # Allow any relation if a both models within same database
    def allow_relation(self, obj1, obj2, **hints):
        # print("\n\nTESTTTT\n\n")
        if  APP_DB_MAPPING.get(obj1._meta.app_label, 'default') == APP_DB_MAPPING.get(obj2._meta.app_label, 'default'):
            return True
        elif  obj1._meta.app_label in ["auth",'bbicore'] and obj2._meta.app_label in ["auth","bbicore"]:
            return True
        return False

    # to filter migration on their respective database if target_db == app_db
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        db_key1     = db
        db_key2     = APP_DB_MAPPING.get(app_label, 'default')
        db_name1    = settings.DATABASES[db_key1]['NAME']
        db_name2    = settings.DATABASES[db_key2]['NAME']
        # print("model_name: " + model_name + ", APP: " + app_label + ", db: " + db + ", app_mapping : " + APP_DB_MAPPING.get(app_label, 'default') )
        # print("DB Name = " + db_name + ", DB Name 2 = " + db_name2)
        return db_name1 == db_name2