from api.v1.user import serializers
from helpers.viewsets import CRUDExtendedModelViewSet
from apps.car_service.models import Service, TypeService
from api.v1.car_service.serializers import ServiceSerializer, TypeServiceSerializer


class ServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TypeServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer
