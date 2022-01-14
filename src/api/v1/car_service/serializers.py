from rest_framework import serializers
from apps.car_service.models import Service, TypeService


class ServiceSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField('name', queryset=TypeService.objects.all())

    class Meta:
        model = Service
        fields = '__all__'


class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = '__all__'
