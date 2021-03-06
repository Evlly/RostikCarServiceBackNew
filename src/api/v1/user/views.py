from django.contrib.auth import get_user_model, authenticate
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from helpers.serializers import ErrorResponseSerializer, EmptySerializer
from helpers.viewsets import RUDExtendedModelViewSet
from rest_framework.exceptions import AuthenticationFailed
from api.v1.module.serializers import ConfigSerializer
from apps.module.models import Config

from api.v1.user import serializers

User = get_user_model()


class UserViewSet(RUDExtendedModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserReadSerializer
    serializer_class_map = {
        'list': serializers.UserReadSerializer,
        'retrieve': serializers.UserReadSerializer,
        'me': serializers.UserReadSerializer,
        'change_password': serializers.UserChangePasswordSerializer,
        'compact': serializers.UserReadSerializer,
        'login': serializers.AuthUserSerializer,
        'refresh_token': EmptySerializer,
        'registration': serializers.UserWriteSerializer,
        'config': ConfigSerializer,
    }
    permission_map = {
        'login': permissions.AllowAny,
    }
    search_fields = ('first_name', 'middle_name', 'last_name')
    ordering_fields = ('first_name', 'middle_name', 'last_name')
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    @action(methods=['post'], detail=False)
    def registration(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializers.UserReadSerializer(instance=user, context=self.get_serializer_context()).data  # noqa: WPS110
        return Response(data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def me(self, request, **kwargs):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: serializers.UserChangePasswordSerializer, 400: ErrorResponseSerializer})
    @action(methods=['post'], detail=False, url_path='change-password')
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializers.UserReadSerializer(instance=user).data
        return Response(data)

    @swagger_auto_schema(responses={200: serializers.UserTokenSerializer})
    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.data)
        if not user:
            raise AuthenticationFailed()
        token, _ = Token.objects.get_or_create(user=user)

        return Response(serializers.UserTokenSerializer(token).data)

    @swagger_auto_schema(responses={200: serializers.UserTokenSerializer})
    @action(methods=['post'], detail=False)
    def refresh_token(self, request):
        Token.objects.filter(user=request.user).delete()
        token = Token.objects.create(user=request.user)

        return Response(serializers.UserTokenSerializer(token).data)

    @swagger_auto_schema(responses={200: ConfigSerializer})
    @action(methods=['get'], detail=True)
    def config(self, request, pk):
        user = self.get_object()
        queryset = Config.objects.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

