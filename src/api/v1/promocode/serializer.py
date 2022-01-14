from rest_framework import serializers
from apps.promocode.models import Activation, Promocode


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = '__all__'


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation
        fields = '__all__'
