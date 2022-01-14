from django.contrib import admin
from apps.car_service.models import TypeService, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    pass
