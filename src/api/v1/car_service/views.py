from api.v1.user import serializers
from helpers.viewsets import CRUDExtendedModelViewSet
from apps.car_service.models import Service, TypeService, Order, OrderStatus
from api.v1.car_service.serializers import ServiceSerializer, TypeServiceSerializer, OrderReadSerializer, OrderStatusSerializer, OrderWriteSerializer


class ServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TypeServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer


class OrderStatusModelViewSet(CRUDExtendedModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrderModelViewSet(CRUDExtendedModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    serializer_class_map = {
        'list': OrderReadSerializer,
        'retrieve': OrderReadSerializer,
    }
