from rest_framework import serializers
from .models import StatusActivity, Device




class DeviceStatusListSerializer(serializers.ModelSerializer):

    ids = serializers.CharField(source='device_id.id')
    device_names = serializers.DateTimeField(source='device_id.device_name')
    class Meta:
        model = StatusActivity
        fields = ['ids', 'device_names', 'modified_at', 'status']


class DeviceStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusActivity
        fields = '__all__'