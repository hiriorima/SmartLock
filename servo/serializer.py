from rest_framework import serializers
from .models import Servo

class ServoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servo
        fields = ('status', 'created_at',)
        extra_kwargs = {'status': {'required': 'True'}}
        validators = []

    def validate_status(self, value):
        data = self.get_initial()
        status = data.get('status')

        if status != 'open' and status != 'close':
           raise serializers.ValidationError("incorrect status parameters")
        return value
