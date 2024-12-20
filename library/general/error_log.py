from library.models.apps_general.submodels.apps import ErrorLog

class ErrorLogClass(object):
    def createErrLog(self,appName,errorLog,dataLog,urlLog):
        objectErrorLog = ErrorLog(
            app_name    = appName,
            error_log   = errorLog,
            data_log    = dataLog,
            url_log     = urlLog
        )

        objectErrorLog.save()
