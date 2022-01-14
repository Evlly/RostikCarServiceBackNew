from helpers.viewsets import CRUDExtendedModelViewSet, CRUExtendedModelViewSet
from apps.module.models import Module, Config
from api.v1.module.serializers import ModuleSerializer, ConfigSerializer


class ModuleModelViewSet(CRUDExtendedModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ConfigModelViewSet(CRUDExtendedModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
