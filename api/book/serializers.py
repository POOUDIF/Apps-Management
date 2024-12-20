from rest_framework import serializers
from library.models.apps_office_management import *

class RoomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBook
        fields = '__all__'
        
class RoomSwitchBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomSwitchBook
        fields = '__all__'