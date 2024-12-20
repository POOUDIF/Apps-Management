from rest_framework import serializers
from library.models.apps_office_management import *
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMasterRoom
        fields = '__all__'
        

class V_RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMasterRoom
        fields = '__all__'