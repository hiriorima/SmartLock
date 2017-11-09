from rest_framework import viewsets
from rest_framework import status
from .models import Key
from .serializer import KeySerializer
from rest_framework.response import Response

class KeyViewSet(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer

    def create(self, request):
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
           key = Key(status=serializer.validated_data['status'])
           key.save()
           return Response(serializer.data)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
