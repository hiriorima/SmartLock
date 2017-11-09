from rest_framework import viewsets
from .models import Servo
from .serializer import ServoSerializer


class ServoViewSet(viewsets.ModelViewSet):
    queryset = Servo.objects.all()
    serializer_class = ServoSerializer
