from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # Adicionando autenticação se necessário
from .models import CurrentData, Location, Hub, Post, MaintenanceHistory
from .serializers import CurrentDataSerializer, LocationSerializer, HubSerializer, PostSerializer, MaintenanceHistorySerializer


class CurrentDataViewSet(viewsets.ModelViewSet):
    queryset = CurrentData.objects.all()
    serializer_class = CurrentDataSerializer
    permission_classes = [IsAuthenticated]  # Caso queira adicionar controle de acesso


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class HubViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class MaintenanceHistoryViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceHistory.objects.all()
    serializer_class = MaintenanceHistorySerializer
    permission_classes = [IsAuthenticated]
