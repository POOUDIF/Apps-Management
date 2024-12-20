from rest_framework import serializers
from library.models.apps_office_management import *


class AccessRightSerializer(serializers.Serializer):
    role            = serializers.JSONField(required=False, allow_null=True)

class ViewPageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = V_OfcMgtApplicationPages
        fields = '__all__'