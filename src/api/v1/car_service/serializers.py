from rest_framework import serializers
from apps.car_service.models import Service, TypeService, Order, OrderStatus
from api.v1.user.serializers import UserCompactSerializer


class ServiceSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField('name', queryset=TypeService.objects.all())
    popularity = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    def get_popularity(self, instance):
        return instance.order_set.count()


class TypeServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeService
        fields = '__all__'


class OrderReadSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField('name', queryset=OrderStatus.objects.all())
    staff = UserCompactSerializer(read_only=True)
    client = UserReadSerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderWriteSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField('name', queryset=OrderStatus.objects.all())

    class Meta:
        model = Order
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'
