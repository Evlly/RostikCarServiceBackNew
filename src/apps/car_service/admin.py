from django.contrib import admin
from apps.car_service.models import TypeService, Service, Order, OrderStatus, Detail


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    pass
