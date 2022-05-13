from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from api.v1.user.views import UserViewSet
from api.v1.car_service.views import ServiceModelViewSet, TypeServiceModelViewSet, OrderModelViewSet, OrderStatusModelViewSet, DetailModelViewSet
from api.v1.promocode.views import PromocodeModelViewSet
from api.v1.module.views import ModuleModelViewSet, ConfigModelViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('service', ServiceModelViewSet, basename='service')
router.register('service_types', TypeServiceModelViewSet, basename='type_service')
router.register('order', OrderModelViewSet, basename='type_service')
router.register('oder_status', OrderStatusModelViewSet, basename='type_service')
router.register('promocode', PromocodeModelViewSet, basename='promocode')
router.register('module', ModuleModelViewSet, basename='module')
router.register('config', ConfigModelViewSet, basename='config')
router.register('detail', DetailModelViewSet, basename='detail')


schema_view = get_schema_view(
    openapi.Info(title='Always data API', default_version='v1', description='Routes of Always data project'),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('', include((router.urls, 'api-root')), name='api-root'),
]
