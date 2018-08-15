from rest_framework import viewsets
from rest_framework import status
from .models import Key
from .serializer import KeySerializer
from rest_framework.response import Response
import sys,os
from .ncmb import ncmb_post

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer

    def create(self, request):
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            key = Key(status=serializer.validated_data['status'])
            key.save()

            if serializer.validated_data['status'] == 'open':
                os.system("sudo python ./key/servo_motor.py 50")
                ncmb_post.post('open', 'smartphone')
            elif serializer.validated_data['status'] == 'close':
                os.system("sudo python ./key/servo_motor.py 200")
                ncmb_post.post('close', 'smartphone')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
