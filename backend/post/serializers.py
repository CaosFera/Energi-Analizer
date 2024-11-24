from rest_framework import serializers
from .models import CurrentData, Location, Hub, Post, MaintenanceHistory
from users.models import Employee
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class CurrentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentData
        fields = ['id', 'lifespan', 'power', 'voltage', 'current']


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "point"
        id_field = 'id'
        fields = ['id', 'street', 'district', 'city', 'point']


class HubSerializer(serializers.ModelSerializer):
    hub_location = LocationSerializer()  # Nested serializer for detailed location info
    
    class Meta:
        model = Hub
        fields = ['id', 'hub_location', 'installation_date']


class PostSerializer(serializers.ModelSerializer):
    post_location = LocationSerializer()  # Nested serializer for detailed location info
    current_data = CurrentDataSerializer()  # Nested serializer for detailed current data

    class Meta:
        model = Post
        fields = [
            'id', 
            'installation_date', 
            'type_lamp', 
            'active', 
            'post_location', 
            'current_data'
        ]


class MaintenanceHistorySerializer(serializers.ModelSerializer):
    post = PostSerializer()  # Nested serializer for detailed post info
    user = serializers.StringRelatedField()  # Assuming Employee model has a __str__ method for display

    class Meta:
        model = MaintenanceHistory
        fields = [
            'id', 
            'date', 
            'description', 
            'post', 
            'user'
        ]
