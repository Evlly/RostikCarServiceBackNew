from rest_framework import serializers
from apps.module.models import Module, Config


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class ConfigSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField('name', queryset=Module.objects.all())


    class Meta:
        model = Config
        fields = ('id', 'module', 'enable', 'user')
