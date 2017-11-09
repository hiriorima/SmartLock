from rest_framework import viewsets
from rest_framework import status
from .models import Servo
from .serializer import ServoSerializer
from rest_framework.response import Response

class ServoViewSet(viewsets.ModelViewSet):
    queryset = Servo.objects.all()
    serializer_class = ServoSerializer

    def create(self, request):
        serializer = ServoSerializer(data=request.data)
        if serializer.is_valid():
           servo = Servo(status=serializer.validated_data['status'])
           servo.save()
           return Response(serializer.data)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
