from django.db.models import Case, When, Value, IntegerField, Q
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.db import DatabaseError, transaction
from django.db.models import Q
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from django.shortcuts import get_object_or_404

from library.models.apps_office_management import *
from library.general.responses import JsonResponseMessage
from library.modules.bbi_token.views import *
from .serializers import *
from library.general.error_log import ErrorLogClass as ErrorLog


MOD_CODE    = 'BBICORE'
rsp  = JsonResponseMessage()

class FormMethods(object):
    def get_access_right(self, objRole):
        # Array for app access
        acc_group       = []
        for value in objRole:
            objGroup            = value['app'].upper()

            # INSP Only For INSPECTION
            if (objGroup == 'OFFICE MANAGEMENT')or (objGroup == 'DEFAULT'):
                data                        = []
                for roleList in value['role_list']:
                    data                    = {'page_code': [], 'access_right': []}
                    objAccess               = V_OfcMgtAccessRight.objects.filter(access_name__iexact=roleList.upper())
                    for acc in objAccess:
                        ADD                 = True
                        page                = acc.page_code
                        page_access         = acc.access_right.split(",")
                        accPageCode         = ''
                        if (len(acc_group) == 0):
                            accPageCode     = data['page_code']
                            if (not page in accPageCode):
                                data        = {'page_code': page, 'access_right': []}
                                for access in page_access:
                                    data['access_right'].append(access)
                        else:
                            accPageCode     = acc_group
                            for pageList in accPageCode:
                                pageCheck   = pageList['page_code']
                                if (page == pageCheck):
                                    ADD = False
                                    for access in page_access:
                                        if (not access in pageList['access_right']):
                                            pageList['access_right'].append(access)
                            if (ADD):
                                data        = {'page_code': page, 'access_right': []}
                                for access in page_access:
                                    if (not access in data['access_right']):
                                        data['access_right'].append(access)
                        if(ADD):
                            acc_group.append(data)

        # Array for rpt access
        arrRptGroup       = []
        # for valueRpt in objRptAccess.all():
        #     objGroupRpt         = str(valueRpt.rpt_group)
        #     # objGroupRptName     = str(valueRpt.name)

        #     objRptRoleNameData  = objRptAccess.filter(rpt_group=objGroupRpt)

        #     rpt_group           = {'rpt': objGroupRpt, 'rpt_role_list': []}

        #     for rptRolesName in objRptRoleNameData:
        #         objRptRoleName         = str(rptRolesName.name)
        #         rpt_group['rpt_role_list'].append(objRptRoleName)

        #     if not any(objRptGroup['rpt'] == objGroupRpt for objRptGroup in arrRptGroup):
        #         arrRptGroup.append(rpt_group.copy())

        json_result     = {'roles': acc_group, 'roles_rpt': arrRptGroup}

        return json_result
    
    def get_pages_list(self, roles):
        app_pages = []
        for role in roles:
            objAccess = V_OfcMgtApplicationPages.objects.filter(access_name=role)
            for page in objAccess:
                if not page in app_pages:
                    app_pages.append(page)

        slrz = ViewPageListSerializer(app_pages, many=True)
        return slrz.data
methods = FormMethods()
# @permission_classes((AllowAny,))
@permission_classes((IsAuthenticated,))
class AccessRight(APIView):
    """[POST] Access Right
    """
    formCode    = 'ACC_RGHT'
    def post(self, request):
        formSerializer      = AccessRightSerializer(data=request.data)
        errMsg              = ''
        isSuccess           = False
        rsp                 = JsonResponseMessage()
        inspResultResult            = []
        try:
            if formSerializer.is_valid():
                objRptMethods           = FormMethods()
                objRole                 = formSerializer.data.get('role')
                ObjResult               = objRptMethods.get_access_right(objRole=objRole)
                isSuccess = True
            else:
                return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE, 'Unsupported form data')
        except Exception as ex:
            return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

        if isSuccess:
            if len(ObjResult) > 0:
                return rsp.RESPONSE_200_OK('Success', ObjResult)
            else:
                return rsp.RESPONSE_200_OK('No Data', ObjResult)

        return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)

@permission_classes([IsAuthenticated])
class PageList(APIView):
     def post(self, request):
        formSerializer = AccessRightSerializer(data=request.data)
        result = []
        try:
            if formSerializer.is_valid():
                objRole = formSerializer.data.get('role')
                result = methods.get_pages_list(objRole)
                if len(result) > 0:
                    return rsp.RESPONSE_200_OK('Success', result)
                else:
                    return rsp.RESPONSE_200_OK('No Data', result)
            else:
                ErrorLog.createErrLog(self,'LMS Document', str(formSerializer.errors), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE, formSerializer.errors)
        except Exception as ex:
            ErrorLog.createErrLog(self,'LMS Document', str(ex), request.data, request.path)
            return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

v_access_right                  = AccessRight.as_view()
v_page_list = PageList.as_view()