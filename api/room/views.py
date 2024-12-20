from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.db import DatabaseError, transaction
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from library.general.error_log import ErrorLogClass as ErrorLog 
from library.general.responses import JsonResponseMessage
from .serializers import *
from library.models.bbicore import *
from library.models.apps_vendor_management import *
from library.modules.bbi_token.views import *
from library.models.apps_plm import *

from django.utils import timezone
import random
MOD_CODE    = 'Book Room'
DB_NAME  = 'db_book_room'
rsp  = JsonResponseMessage()

class FormMethods(object):
    
    def get_data(self, data):
        msg = None
        isValidationErr = False
        try:
            view_all = data.get('view_all')
            # print('test',view_all)
            if view_all == True:
                objData = RoomMasterRoom.objects.all()
            else:
                # print('test',view_all)
                objData = RoomMasterRoom.objects.filter(status=True)
            return objData
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)

    def post_data(self, data):
        msg = None
        isValidationErr = False  
        try:
            code = FormMethods.generate_unique_code()
            # objChk = Process.objects.filter(Q(status=True)&(Q(code=code) or Q(process_name=data.get('process_name'))))
            objChk = RoomMasterRoom.objects.filter(Q(status=True) & Q(room_name=data.get('room_name')))
            if len(objChk) == 0:
                objData = RoomMasterRoom.objects.create(
                    code = code,
                    room_name = data.get('room_name'),
                    room_desc = data.get('room_desc'),
                    created_by = data.get('created_by'),
                    created_at = timezone.now(),
                    updated_by = data.get('updated_by'),
                    updated_at = None,
                    status = data.get('status')
                )
                objData.save()
            else:
                msg = 'Data has been exist, %s'%(data.get('process_name'))
                isValidationErr = True
        except Exception as ex:
            msg = 'Fail create data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)

    def put_data(self, data):
        msg = None
        isValidationErr = False  
        try:
            # code = FormMethods.generate_unique_code()
            # objChk = Process.objects.filter(Q(status=True)&(Q(code=code) or Q(process_name=data.get('process_name'))))
            objChk = RoomMasterRoom.objects.filter(Q(status=True) & Q(room_name=data.get('room_name'))).exclude(id=data.get('item_id'))
            if len(objChk) == 0:
                objData = RoomMasterRoom.objects.filter(id=data.get('item_id')).first()
                objData.code = objData.code
                objData.room_name = data.get('room_name')
                objData.room_desc = data.get('room_desc')
                objData.updated_by = data.get('updated_by')
                objData.status = data.get('status')
                objData.save()
            else:
                isValidationErr = True
                msg = 'Data has been exist, room name %s'%(data.get('room_name'))
                
        except Exception as ex:
            
            msg = 'Fail update data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)

    def generate_unique_code():
        while True:
            code = str(random.randint(1000, 9999))
            existing_codes = RoomMasterRoom.objects.filter(code=code)
            if len(existing_codes) == 0:
                return code
    # def delete_data(self, request):
    #     pass
    
class RoomView(APIView):
    def post(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        # print(request.data)
        actions = request.data.get('action')
        if actions == 'get':
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = FormMethods()
                objGetForm = objFormMethods.get_data(request.data)
                # Serialize data
                serialized_data = RoomSerializer(objGetForm, many=True).data
                # Lakukan sesuatu dengan data yang diambil, seperti mengembalikan atau memproses lebih lanjut
                isSuccess = True
                jsonPayload = {"data": serialized_data}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to get data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been get', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
        else :
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = FormMethods()
                objGetForm = objFormMethods.post_data(request.data)
                isSuccess = True
                jsonPayload = {"creator": request.data.get('created_by')}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to create data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))
            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been created', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)

    # def post(self, request):
    #     pass

    def put(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        try:
            # Mengambil semua data dari model V_VendorServiceType
            objFormMethods = FormMethods()
            objGetForm = objFormMethods.put_data(request.data)
            isSuccess = True
            jsonPayload = {"creator": request.data.get('updated_by')}
            
        except ValidationError as ex:
            print(str(ex))
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to update data: {str(ex)}')
            
        except Exception as ex:
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

        if isSuccess:
            return rsp.RESPONSE_200_OK(msg='Data has been updated', payload=jsonPayload)
        # print('masuk')
        return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
    
v_room = RoomView.as_view()