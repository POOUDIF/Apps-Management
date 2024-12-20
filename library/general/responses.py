from json import JSONEncoder, dumps
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class JsonResponseMessage(object):
    def RESPONSE_200_OK(self, msg="Success", payload=None):
        rspMsg  = "Success"
        if msg is not None:
            rspMsg = msg
        return Response({"status": HTTP_200_OK, "message": rspMsg, "payload": payload}, status=HTTP_200_OK)
        
    def RESPONSE_400_BAD_REQUEST(self, mod_code=None, msg="Can not process your request", payload=None):
        if mod_code is None:
            return Response({"status": HTTP_400_BAD_REQUEST, "message": msg, "payload": payload}, status=HTTP_400_BAD_REQUEST)
        return Response({"status": HTTP_400_BAD_REQUEST, "message": (mod_code + ': ' + msg), "payload": payload}, status=HTTP_400_BAD_REQUEST)
        
    def RESPONSE_401_UNAUTHORIZED(self, msg="You are not authorized to process this request", payload=None):
        return Response({"status": HTTP_401_UNAUTHORIZED, "message": msg, "payload": payload}, status=HTTP_401_UNAUTHORIZED)
        
    def RESPONSE_401_TOKEN_EXPIRED(self, msg="Unauthorized token, please login", payload=None):
        return Response({"status": HTTP_401_UNAUTHORIZED, "message": msg, "payload": payload}, status=HTTP_401_UNAUTHORIZED)
        
    def RESPONSE_403_FORBIDDEN(self, msg="", payload=None):
        return Response({"status": HTTP_403_FORBIDDEN, "message": msg, "payload": payload}, status=HTTP_403_FORBIDDEN)
        
    def RESPONSE_404_NOT_FOUND(self, msg="", payload=None):
        return Response({"status": HTTP_404_NOT_FOUND, "message": msg, "payload": payload}, status=HTTP_404_NOT_FOUND)
        
    def RESPONSE_500_INTERNAL_SERVER_ERROR(self, mod_code=None, msg="Error processing your request", payload=None):
        if mod_code is None:
            return Response({"status": HTTP_400_BAD_REQUEST, "message": msg, "payload": payload}, status=HTTP_400_BAD_REQUEST)
        return Response({"status": HTTP_500_INTERNAL_SERVER_ERROR, "message": (mod_code + ': ' + msg), "payload": payload}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class JsonPivotTableResponses(object):
    @staticmethod
    def PIVOTTABLE_RESPONSES(pivotData, vals=[], rows=[], cols=[], aggregatorName='Sum', rendererName='Table', disabledFromDragDrop=[], hiddenFromDragDrop=[]):
        jsonData = {"pivotData": pivotData, "vals":vals, "rows":rows, "cols":cols, "aggregatorName":aggregatorName, "rendererName":rendererName, "disabledFromDragDrop":disabledFromDragDrop, "hiddenFromDragDrop":hiddenFromDragDrop}
        
        return jsonData
