from rest_framework import serializers
from .models import Servo


class ServoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servo
        fields = ('status', 'created_at',)
