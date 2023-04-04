from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Client, ClientAddress
from .serializers import ClientSerializer, ClientAddressSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [IsAuthenticated]
