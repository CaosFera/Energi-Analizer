from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrentDataViewSet, LocationViewSet, HubViewSet, PostViewSet, MaintenanceHistoryViewSet

# Criação do router para mapear automaticamente as rotas dos ViewSets
router = DefaultRouter()
router.register(r'current_data', CurrentDataViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'hubs', HubViewSet)
router.register(r'posts', PostViewSet)
router.register(r'maintenance_history', MaintenanceHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Inclui todas as rotas geradas pelo router
]
