from rest_framework import serializers
from library.models.apps_office_management import *

class RoomMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBookMail
        fields = '__all__'