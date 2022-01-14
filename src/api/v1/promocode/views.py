from gc import get_objects
from itertools import permutations
from urllib import request
from helpers.viewsets import CRUDExtendedModelViewSet
from apps.promocode.models import Promocode, Activation
from api.v1.promocode.serializer import PromocodeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema, no_body


class PromocodeModelViewSet(CRUDExtendedModelViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request=no_body)
    @action(methods=['post'], detail=True)
    def activation(self, request, pk):
        promocode = self.get_object()
        Activation.objects.create(user=request.user, promocode=promocode)
        return super().retrieve(request)
