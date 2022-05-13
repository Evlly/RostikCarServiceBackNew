from api.v1.user import serializers
from helpers.viewsets import CRUDExtendedModelViewSet
from apps.car_service.models import Service, TypeService, Order, OrderStatus, Detail
from api.v1.car_service.serializers import ServiceSerializer, TypeServiceSerializer, OrderReadSerializer, OrderStatusSerializer, OrderWriteSerializer, DetailSerializer


class ServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TypeServiceModelViewSet(CRUDExtendedModelViewSet):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer


class OrderStatusModelViewSet(CRUDExtendedModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class DetailModelViewSet(CRUDExtendedModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class OrderModelViewSet(CRUDExtendedModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    serializer_class_map = {
        'list': OrderReadSerializer,
        'retrieve': OrderReadSerializer,
    }
